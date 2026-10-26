import copy
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from b2b_harness.core import analyze, approval_check, evidence_context, render
from b2b_harness.profile import DEFAULT_PROFILE, load_profile

ROOT = Path(__file__).resolve().parents[1]
DAY = "2026-09-17"

def fixture(name):
    return json.loads((ROOT / "examples" / (name + ".json")).read_text())

def profile():
    return load_profile(DEFAULT_PROFILE)

class RuntimeTests(unittest.TestCase):
    def test_signal_ready(self):
        result = analyze("signal", fixture("signal"), profile(), DAY)
        self.assertEqual(result["status"], "draft_ready")
        self.assertEqual(result["external_actions"], [])
        self.assertEqual(result["delivery"], "local_only")

    def test_unknown_attribution(self):
        result = analyze("ads", fixture("ads"), profile(), DAY)
        self.assertIsNone(result["metrics"]["paid_media_cac"])
        self.assertIsNone(result["metrics"]["roas"])
        self.assertEqual(result["metrics"]["cpc"], 2)

    def test_attributed_metrics(self):
        data = fixture("ads")
        data["evidence"][0]["claim_key"] = "attribution.identity_join"
        data["metrics"].update(customers=2, attributed_revenue=1000)
        data["attribution"] = dict(identity_join_verified=True, same_cohort_and_window=True, evidence_id="e1")
        result = analyze("ads", data, profile(), DAY)
        self.assertEqual(result["metrics"]["paid_media_cac"], 120)
        self.assertAlmostEqual(result["metrics"]["roas"], 1000 / 240)

    def test_stale_join_cannot_support_cac(self):
        data = fixture("ads")
        data["evidence"][0]["claim_key"] = "attribution.identity_join"
        data["metrics"]["customers"] = 2
        data["attribution"] = dict(identity_join_verified=True, same_cohort_and_window=True, evidence_id="e1")
        result = analyze("ads", data, profile(), "2026-10-02")
        self.assertIsNone(result["metrics"]["paid_media_cac"])

    def test_unrelated_evidence_cannot_support_cac(self):
        data = fixture("ads")
        data["metrics"]["customers"] = 2
        data["attribution"] = dict(identity_join_verified=True, same_cohort_and_window=True, evidence_id="e1")
        self.assertIsNone(analyze("ads", data, profile(), DAY)["metrics"]["paid_media_cac"])

    def test_conflicting_attribution_withholds_cac(self):
        data = fixture("ads")
        data["metrics"]["customers"] = 2
        data["evidence"][0]["claim_key"] = "attribution.identity_join"
        other = copy.deepcopy(data["evidence"][0])
        other.update(id="e2", statement="Identity reconciliation failed")
        data["evidence"].append(other)
        data["attribution"] = dict(identity_join_verified=True, same_cohort_and_window=True, evidence_id="e1")
        self.assertIsNone(analyze("ads", data, profile(), DAY)["metrics"]["paid_media_cac"])

    def test_zero_denominators(self):
        data = fixture("ads")
        data["metrics"].update(spend=0, clicks=0, impressions=0)
        result = analyze("ads", data, profile(), DAY)
        self.assertIsNone(result["metrics"]["ctr"])
        self.assertIsNone(result["metrics"]["cpc"])

    def test_missing_is_not_zero(self):
        data = fixture("ads")
        del data["metrics"]["signups"]
        self.assertIsNone(analyze("ads", data, profile(), DAY)["metrics"]["signups"])

    def test_invalid_numbers(self):
        for value in (-1, True, "100", float("nan"), float("inf")):
            with self.subTest(value=value):
                data = fixture("ads")
                data["metrics"]["spend"] = value
                with self.assertRaises(ValueError):
                    analyze("ads", data, profile(), DAY)

    def test_no_automatic_verification(self):
        data = fixture("signal")
        del data["evidence"][0]["review"]
        result = analyze("signal", data, profile(), DAY)
        self.assertEqual(result["context"]["records"][0]["status"], "unreviewed")
        self.assertIn("no_current_reviewed_evidence", result["reasons"])

    def test_conflict(self):
        records = fixture("signal")["evidence"]
        other = copy.deepcopy(records[0])
        other.update(id="e2", statement="A different capability")
        result = evidence_context(records + [other], DAY)
        self.assertEqual(result["conflicts"], ["product.capability"])

    def test_duplicate_evidence_ids(self):
        records = fixture("signal")["evidence"]
        with self.assertRaises(ValueError):
            evidence_context(records + records, DAY)

    def test_invalid_dates(self):
        records = fixture("signal")["evidence"]
        records[0]["observed_at"] = "2027-01-01"
        with self.assertRaises(ValueError):
            evidence_context(records, DAY)

    def test_rejected_evidence_not_usable(self):
        data = fixture("signal")
        data["evidence"][0]["review"]["decision"] = "rejected"
        self.assertEqual(analyze("signal", data, profile(), DAY)["evidence_ids"], [])

    def test_landing_incomplete(self):
        result = analyze("landing", fixture("landing"), profile(), DAY)
        self.assertIn("qa_missing:mobile_readable", result["reasons"])
        self.assertEqual(result["status"], "needs_review")

    def test_homepage_is_not_campaign(self):
        data = fixture("landing")
        data.update(slug="/", folder="home")
        self.assertIn("page_not_isolated", analyze("landing", data, profile(), DAY)["reasons"])

    def test_unsubstantiated_claim(self):
        data = fixture("landing")
        data["proof_claim_keys"] = ["guaranteed-revenue"]
        self.assertIn("unsupported_product_claim", analyze("landing", data, profile(), DAY)["reasons"])

    def test_complete_landing_still_not_published(self):
        data = fixture("landing")
        data["qa"] = {key: True for key in data["qa"]}
        result = analyze("landing", data, profile(), DAY)
        self.assertEqual(result["status"], "draft_ready")
        self.assertEqual(result["external_actions"], [])

    def test_approval_scope_revocation_expiry(self):
        action = dict(target="example-page", action="publish", version="v1")
        approval = dict(**action, approved_by="example-owner", message_ref="example-message", expires_at="2026-10-01")
        self.assertTrue(approval_check(action, approval, DAY)["allowed"])
        self.assertFalse(approval_check(action, approval, DAY)["execution_supported"])
        for update in ({"revoked": True}, {"version": "v2"}, {"expires_at": "2026-09-01"}):
            self.assertFalse(approval_check(action, {**approval, **update}, DAY)["allowed"])
        self.assertFalse(approval_check(action, None, DAY)["allowed"])

    def test_reproducibility(self):
        self.assertEqual(analyze("signal", fixture("signal"), profile(), DAY), analyze("signal", fixture("signal"), profile(), DAY))

    def test_language_wrappers(self):
        result = analyze("signal", fixture("signal"), profile(), DAY)
        self.assertIn("营销交付简报", render(result, "zh"))
        self.assertIn("Marketing delivery brief", render(result, "en"))

    def test_cli_no_overwrite(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "result"
            command = [sys.executable, "-m", "b2b_harness", "signal", "--input", "examples/signal.json", "--as-of", DAY, "--output", str(output)]
            first = subprocess.run(command, cwd=ROOT, capture_output=True)
            self.assertEqual(first.returncode, 0, first.stderr)
            before = (output / "result.json").read_bytes()
            second = subprocess.run(command, cwd=ROOT, capture_output=True)
            self.assertEqual(second.returncode, 2)
            self.assertEqual((output / "result.json").read_bytes(), before)

    def test_toml_profile_maps_required_fields(self):
        data = profile()
        self.assertEqual(data["company"], "DemoCo")
        self.assertTrue(data["cta_url"].startswith("https://"))
        self.assertTrue(all(data[key] for key in ("company", "icp", "offer", "cta_url")))

    def test_profile_missing_field_is_an_error(self):
        data = profile()
        data["offer"] = ""
        with self.assertRaises(ValueError):
            analyze("signal", fixture("signal"), data, DAY)

    def test_json_profile_still_accepted(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "company.json"
            path.write_text(json.dumps(profile()))
            self.assertEqual(load_profile(path), profile())

    def test_handoff_ready(self):
        result = analyze("handoff", fixture("handoff"), profile(), DAY)
        self.assertEqual(result["status"], "draft_ready", result["reasons"])
        self.assertEqual(result["owner"], "revenue-operations")
        self.assertEqual(result["external_actions"], [])

    def test_handoff_unknown_permission_is_not_a_pass(self):
        data = fixture("handoff")
        data["permission"] = {"contact_basis": "unknown", "suppression_checked": False}
        reasons = analyze("handoff", data, profile(), DAY)["reasons"]
        self.assertIn("permission_unknown", reasons)
        self.assertIn("suppression_unknown", reasons)

    def test_handoff_promotion_needs_evidence(self):
        data = fixture("handoff")
        data["stage_evidence_ids"] = []
        self.assertIn("stage_promotion_without_evidence", analyze("handoff", data, profile(), DAY)["reasons"])

    def test_handoff_unreviewed_evidence_cannot_promote(self):
        data = fixture("handoff")
        del data["evidence"][0]["review"]
        reasons = analyze("handoff", data, profile(), DAY)["reasons"]
        self.assertIn("stage_promotion_without_evidence", reasons)
        self.assertIn("intent_not_evidenced", reasons)

    def test_handoff_customer_needs_payment_evidence(self):
        data = fixture("handoff")
        data["proposed_stage"] = "customer"
        self.assertIn("customer_without_payment_evidence", analyze("handoff", data, profile(), DAY)["reasons"])

    def test_handoff_poor_fit_blocks_promotion(self):
        data = fixture("handoff")
        data["fit"] = {"status": "not_fit", "reason": "B2C brand"}
        self.assertIn("promotion_without_confirmed_fit", analyze("handoff", data, profile(), DAY)["reasons"])

    def test_handoff_no_promotion_needs_no_stage_evidence(self):
        data = fixture("handoff")
        data.update(proposed_stage="mql", stage_evidence_ids=[])
        self.assertNotIn("stage_promotion_without_evidence", analyze("handoff", data, profile(), DAY)["reasons"])

    def test_handoff_invalid_stage(self):
        data = fixture("handoff")
        data["proposed_stage"] = "won"
        with self.assertRaises(ValueError):
            analyze("handoff", data, profile(), DAY)

if __name__ == "__main__":
    unittest.main()
