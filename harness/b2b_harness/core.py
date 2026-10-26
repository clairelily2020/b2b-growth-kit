"""Evidence checks and deterministic draft workflows. No network or credential access."""
import hashlib
import json
import math
from datetime import date
from urllib.parse import urlparse

WORKFLOWS = ("signal", "ads", "landing", "handoff")
ROLES = {"signal": "growth-strategy", "ads": "demand-generation", "landing": "content-conversion",
         "handoff": "revenue-operations"}
LIFECYCLE = ("subscriber", "lead", "mql", "sql", "opportunity", "customer")
FIT = ("fit", "partial", "not_fit", "unknown")
INTENT = ("stated", "inferred", "none", "unknown")

def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False).encode()).hexdigest()

def required(obj, names):
    if not isinstance(obj, dict):
        raise ValueError("Expected an object")
    missing = [n for n in names if obj.get(n) is None or obj.get(n) == ""]
    if missing:
        raise ValueError("Missing fields: " + ", ".join(missing))

def number(value, name):
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value) or value < 0:
        raise ValueError(name + " must be a finite non-negative number")
    return value

def evidence_context(records, as_of):
    today = date.fromisoformat(as_of)
    if not isinstance(records, list):
        raise ValueError("evidence must be a list")
    result, ids, claims, conflicts = [], set(), {}, []
    for record in records:
        required(record, ("id", "claim_key", "statement", "source", "observed_at", "expires_at"))
        if record["id"] in ids:
            raise ValueError("Duplicate evidence id: " + record["id"])
        ids.add(record["id"])
        observed = date.fromisoformat(record["observed_at"])
        expires = date.fromisoformat(record["expires_at"])
        if observed > today or expires < observed:
            raise ValueError("Invalid evidence date interval")
        review = record.get("review", {})
        status = "unreviewed"
        if review:
            required(review, ("reviewer", "reviewed_at", "source_checked", "decision"))
            reviewed = date.fromisoformat(review["reviewed_at"])
            if reviewed > today or reviewed < observed:
                raise ValueError("Invalid review date")
            if review["decision"] not in ("accepted", "rejected"):
                raise ValueError("Invalid review decision")
            if review["source_checked"] is not True:
                raise ValueError("Review must explicitly record source_checked=true")
            status = "reviewed" if review["decision"] == "accepted" else "rejected"
        if expires < today:
            status = "stale"
        # Explicit claim-key differences only; this is not semantic contradiction detection.
        if status != "stale" and status != "rejected":
            previous = claims.setdefault(record["claim_key"], record["statement"])
            if previous != record["statement"]:
                conflicts.append(record["claim_key"])
        result.append({**record, "status": status, "content_hash": digest(record)})
    return {"as_of": as_of, "records": result, "conflicts": sorted(set(conflicts)),
            "verification": "Review metadata is user-supplied; sources are not fetched or independently verified."}

def analyze(workflow, data, profile, as_of):
    if workflow not in WORKFLOWS:
        raise ValueError("Unknown workflow")
    required(profile, ("company", "icp", "offer", "cta_url"))
    required(data, ("evidence",))
    context = evidence_context(data["evidence"], as_of)
    reasons = []
    usable = [r for r in context["records"] if r["status"] == "reviewed"]
    if not usable:
        reasons.append("no_current_reviewed_evidence")
    if context["conflicts"]:
        reasons.append("conflicting_claim_values")
    result = {"workflow": workflow, "owner": ROLES[workflow], "company": profile["company"],
              "synthetic": data.get("synthetic") is True, "as_of": as_of,
              "evidence_ids": [r["id"] for r in usable], "context": context,
              "external_actions": [], "delivery": "local_only", "reasons": reasons}
    if workflow == "signal":
        required(data, ("signal", "hypothesis", "experiment", "metric", "stop_rule", "measurement_window"))
        result["draft"] = {k: data[k] for k in ("signal", "hypothesis", "experiment", "metric", "stop_rule", "measurement_window")}
        result["next_action"] = "Review the hypothesis and validate relevance before proposing a live experiment."
    elif workflow == "ads":
        required(data, ("metrics", "period", "currency", "timezone"))
        metrics = data["metrics"]
        required(metrics, ("spend", "clicks", "impressions"))
        for key in ("spend", "clicks", "impressions"):
            number(metrics[key], key)
        for key in ("clicks", "impressions", "signups", "customers"):
            if metrics.get(key) is not None:
                value = number(metrics[key], key)
                if int(value) != value:
                    raise ValueError(key + " must be an integer count")
        if metrics["clicks"] > metrics["impressions"]:
            raise ValueError("Clicks cannot exceed impressions")
        if metrics.get("attributed_revenue") is not None:
            number(metrics["attributed_revenue"], "attributed_revenue")
        identity = data.get("attribution", {})
        join_evidence = [r for r in usable if r["id"] == identity.get("evidence_id")
                         and r["claim_key"] == "attribution.identity_join"]
        valid = (identity.get("identity_join_verified") is True
                 and identity.get("same_cohort_and_window") is True
                 and bool(join_evidence) and not context["conflicts"])
        result["metrics"] = {
            "spend": metrics["spend"], "clicks": metrics["clicks"],
            "impressions": metrics["impressions"], "signups": metrics.get("signups"),
            "cpc": metrics["spend"] / metrics["clicks"] if metrics["clicks"] else None,
            "ctr": metrics["clicks"] / metrics["impressions"] if metrics["impressions"] else None,
            "paid_media_cac": metrics["spend"] / metrics["customers"] if valid and metrics.get("customers") else None,
            "roas": metrics.get("attributed_revenue") / metrics["spend"]
                    if valid and metrics.get("attributed_revenue") is not None and metrics["spend"] else None}
        result["period"] = data["period"]
        result["currency"] = data["currency"]
        result["timezone"] = data["timezone"]
        if not valid:
            reasons.append("attribution_not_verified")
        result["next_action"] = "Reconcile attribution and downstream qualification before proposing spend changes."
    elif workflow == "handoff":
        handoff(data, usable, context, reasons, result)
    else:
        required(data, ("slug", "folder", "headline", "cta_label", "proof_claim_keys", "primary_metric", "qa"))
        if not isinstance(data["proof_claim_keys"], list):
            raise ValueError("proof_claim_keys must be a list")
        if data["folder"] != "landing-pages" or not data["slug"].strip("/") or ".." in data["slug"]:
            reasons.append("page_not_isolated")
        qa = data["qa"]
        for check in ("homepage_unchanged", "scoped_styles", "mobile_readable", "cta_tested", "tracking_tested"):
            if qa.get(check) is not True:
                reasons.append("qa_missing:" + check)
        parsed = urlparse(profile["cta_url"])
        if parsed.scheme != "https" or not parsed.netloc:
            reasons.append("invalid_cta_url")
        known = {r["claim_key"] for r in usable}
        if not data["proof_claim_keys"] or set(data["proof_claim_keys"]) - known:
            reasons.append("unsupported_product_claim")
        result["draft"] = {"headline": data["headline"], "audience": profile["icp"],
                           "offer": profile["offer"], "cta_label": data["cta_label"],
                           "cta_url": profile["cta_url"], "slug": data["slug"],
                           "folder": data["folder"], "primary_metric": data["primary_metric"]}
        result["next_action"] = "Review the local delivery pack. Publishing is a separate authorized action."
    result["status"] = "needs_review" if reasons else "draft_ready"
    result["run_id"] = digest({"workflow": workflow, "data": data, "profile": profile, "as_of": as_of})[:16]
    return result

def handoff(data, usable, context, reasons, result):
    """Revenue handoff checks: fit, intent, permission and lifecycle changes stay evidence-based."""
    required(data, ("account", "contact_role", "fit", "intent", "permission", "current_stage", "proposed_stage"))
    fit, intent, permission = data["fit"], data["intent"], data["permission"]
    for obj in (fit, intent, permission):
        if not isinstance(obj, dict):
            raise ValueError("fit, intent and permission must be objects")
    if fit.get("status") not in FIT:
        raise ValueError("fit.status must be one of " + ", ".join(FIT))
    if intent.get("status") not in INTENT:
        raise ValueError("intent.status must be one of " + ", ".join(INTENT))
    if data["current_stage"] not in LIFECYCLE or data["proposed_stage"] not in LIFECYCLE:
        raise ValueError("stages must be one of " + ", ".join(LIFECYCLE))
    usable_ids = {r["id"]: r for r in usable}
    if not data.get("owner_role"):
        reasons.append("missing_owner")
    if permission.get("suppression_checked") is not True:
        reasons.append("suppression_unknown")
    if permission.get("contact_basis") in (None, "", "unknown"):
        reasons.append("permission_unknown")
    intent_ids = intent.get("evidence_ids") or []
    if intent["status"] == "stated" and (not intent_ids or not set(intent_ids) <= set(usable_ids)):
        reasons.append("intent_not_evidenced")
    promoted = LIFECYCLE.index(data["proposed_stage"]) > LIFECYCLE.index(data["current_stage"])
    stage_ids = data.get("stage_evidence_ids") or []
    if promoted:
        if not stage_ids or not set(stage_ids) <= set(usable_ids):
            reasons.append("stage_promotion_without_evidence")
        if fit["status"] in ("not_fit", "unknown"):
            reasons.append("promotion_without_confirmed_fit")
        if data["proposed_stage"] == "customer" and not any(
                usable_ids[i]["claim_key"] == "revenue.payment" for i in stage_ids if i in usable_ids):
            reasons.append("customer_without_payment_evidence")
    result["draft"] = {"account": data["account"], "contact_role": data["contact_role"],
                       "owner_role": data.get("owner_role"), "fit": fit, "intent": intent,
                       "permission": permission, "current_stage": data["current_stage"],
                       "proposed_stage": data["proposed_stage"], "stage_evidence_ids": stage_ids,
                       "next_action": data.get("next_action"), "next_action_date": data.get("next_action_date")}
    result["next_action"] = "Hand the note to the owner. CRM changes and replies are separate authorized actions."


def approval_check(action, approval, as_of):
    """Advisory check only. Does not execute, authenticate approvers or grant permission."""
    required(action, ("target", "action", "version"))
    reasons = []
    if not approval:
        return {"allowed": False, "reasons": ["missing_approval"], "execution_supported": False}
    required(approval, ("target", "action", "version", "approved_by", "message_ref", "expires_at"))
    if any(action[k] != approval[k] for k in ("target", "action", "version")):
        reasons.append("scope_mismatch")
    if approval.get("revoked") is True:
        reasons.append("revoked")
    if date.fromisoformat(approval["expires_at"]) < date.fromisoformat(as_of):
        reasons.append("expired")
    return {"allowed": not reasons, "reasons": reasons, "execution_supported": False}

def render(result, language):
    zh = language == "zh"
    title = "营销交付简报" if zh else "Marketing delivery brief"
    fields = [("公司" if zh else "Company", result["company"]),
              ("负责人" if zh else "Owner", result["owner"]),
              ("状态" if zh else "Status", result["status"]),
              ("资料日期" if zh else "As of", result["as_of"]),
              ("示例数据" if zh else "Synthetic", result["synthetic"])]
    lines = ["# " + title, ""] + [f"- {k}: {v}" for k, v in fields]
    lines += ["", "## " + ("交付内容" if zh else "Draft"), "",
              "```json", json.dumps(result.get("draft", result.get("metrics")), indent=2, ensure_ascii=False), "```",
              "", "## " + ("检查结果" if zh else "Checks"), ""]
    lines += ["- " + r for r in result["reasons"]] or ["- " + ("未发现规则检查问题。" if zh else "No rule-check issues found.")]
    lines += ["", ("这是本地草案，未发布、发送或调整预算。输入证据与审核声明未经过联网核验。"
                       if zh else "Local draft only. Nothing was published, sent or spent. Source and review assertions were not independently verified."),
              "", ("下一步：审阅交付内容，优先处理以上检查问题。" if zh else "Next: " + result["next_action"]), ""]
    return "\n".join(lines)
