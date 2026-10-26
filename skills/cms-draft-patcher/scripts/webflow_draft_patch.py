#!/usr/bin/env python3
"""Patch existing Webflow CMS items as drafts from clean local sources. Standard library only.

Safe by default:
  - Without --apply it only fetches each item and reports what would change (dry run).
  - With --apply it requires --approval-ref (where the approval was given) and records it.
  - Items are always written with isDraft=true. Nothing is published.

Token: WEBFLOW_API_TOKEN from the environment, or from a .env file in the current directory.

Ops file: a JSON array. Each op:
  {"label": "...", "collection_id": "...", "item_id": "...", "kind": "rich_text_from_html",
   "target_field": "<rich text field slug>", "local_html": "path/to/export.html",
   "source_regex": "<optional regex with one group; default: the first w-richtext article>",
   "whole_file": false, "prepend_html": "", "append_html": "",
   "strip_svg_style_blocks": true, "strip_sections_by_class": ["cta-block"],
   "strip_patterns": ["regex"], "assert_contains": ["text that must be present"]}
  {"label": "...", "collection_id": "...", "item_id": "...", "kind": "set_field",
   "field": "<field slug>", "value": "..."}

Usage:
  python3 scripts/webflow_draft_patch.py --ops ops.json [--report out.json]
  python3 scripts/webflow_draft_patch.py --ops ops.json --apply --approval-ref "ticket-123"
"""
import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

API = "https://api.webflow.com/v2"
DEFAULT_SOURCE = r'<article[^>]*class="[^"]*\bw-richtext\b[^"]*"[^>]*>(.*?)</article>'


def token():
    value = os.environ.get("WEBFLOW_API_TOKEN")
    env_file = Path.cwd() / ".env"
    if not value and env_file.is_file():
        for line in env_file.read_text(encoding="utf-8").splitlines():
            key, _, val = line.strip().partition("=")
            if key == "WEBFLOW_API_TOKEN" and val:
                value = val.strip().strip("'\"")
    if not value:
        raise SystemExit("WEBFLOW_API_TOKEN is not set (environment or ./.env)")
    return value


def request(method, path, secret, payload=None):
    headers = {"Authorization": f"Bearer {secret}", "accept": "application/json"}
    data = None
    if payload is not None:
        data = json.dumps(payload).encode("utf-8")
        headers["content-type"] = "application/json"
    req = urllib.request.Request(API + path, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            return resp.status, json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        raise RuntimeError(f"{method} {path} failed: {exc.code} {exc.read().decode('utf-8', 'ignore')}") from exc


def clean_html(html, op):
    if op.get("strip_svg_style_blocks"):
        html = re.sub(r"<svg\b[^>]*>\s*<style\b[^>]*>.*?</style>\s*</svg>", "", html, flags=re.S | re.I)
    for name in op.get("strip_sections_by_class", []):
        pattern = (r"<section\b(?=[^>]*\bclass=(['\"])[^'\"]*\b" + re.escape(name)
                   + r"\b[^'\"]*\1)[^>]*>.*?</section>")
        html = re.sub(pattern, "", html, flags=re.S | re.I)
    for pattern in op.get("strip_patterns", []):
        html = re.sub(pattern, "", html, flags=re.S | re.I)
    return html.strip()


def source_html(op):
    text = Path(op["local_html"]).read_text(encoding="utf-8")
    if op.get("whole_file"):
        html = text
    else:
        match = re.search(op.get("source_regex") or DEFAULT_SOURCE, text, flags=re.S)
        if not match:
            raise ValueError(f"{op['label']}: source block not found in {op['local_html']}")
        html = match.group(1)
    html = clean_html(html, op)
    if op.get("prepend_html"):
        html = op["prepend_html"].strip() + "\n" + html
    if op.get("append_html"):
        html = html + "\n" + op["append_html"].strip()
    for needle in op.get("assert_contains", []):
        if needle not in html:
            raise ValueError(f"{op['label']}: expected text missing from source: {needle!r}")
    if re.search(r"<script\b", html, re.I):
        raise ValueError(f"{op['label']}: source contains <script>; refusing to write it into rich text")
    return html


def run(op, secret, apply):
    for key in ("label", "collection_id", "item_id", "kind"):
        if not op.get(key):
            raise ValueError(f"op missing '{key}'")
    _, payload = request("GET", f"/collections/{op['collection_id']}/items/{op['item_id']}", secret)
    item = payload.get("item", payload) if isinstance(payload, dict) else None
    if not item or item.get("id") != op["item_id"]:
        raise ValueError(f"{op['label']}: item not found")
    fields = dict(item.get("fieldData", {}))
    if op["kind"] == "rich_text_from_html":
        field = op.get("target_field")
        if not field:
            raise ValueError(f"{op['label']}: rich_text_from_html needs target_field")
        new_value = source_html(op)
    elif op["kind"] == "set_field":
        field, new_value = op.get("field"), op.get("value")
        if not field:
            raise ValueError(f"{op['label']}: set_field needs field")
    else:
        raise ValueError(f"{op['label']}: unsupported kind {op['kind']}")
    old_value = fields.get(field)
    result = {"label": op["label"], "item_id": op["item_id"], "name": fields.get("name"),
              "slug": fields.get("slug"), "field": field,
              "changed": old_value != new_value,
              "old_length": len(str(old_value or "")), "new_length": len(str(new_value or "")),
              "status": "dry_run"}
    if apply and result["changed"]:
        fields[field] = new_value
        status, _ = request("PATCH", f"/collections/{op['collection_id']}/items/{op['item_id']}", secret,
                            {"isArchived": False, "isDraft": True, "fieldData": fields})
        result.update(status="patched_as_draft", http_status=status)
    elif apply:
        result["status"] = "unchanged"
    return result


def main():
    parser = argparse.ArgumentParser(description="Patch Webflow CMS items as drafts (dry run by default).")
    parser.add_argument("--ops", required=True, type=Path)
    parser.add_argument("--apply", action="store_true", help="write changes as drafts")
    parser.add_argument("--approval-ref", default="", help="required with --apply")
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    if args.apply and not args.approval_ref.strip():
        raise SystemExit("--apply requires --approval-ref (where the approval for these exact items was given)")
    ops = json.loads(args.ops.read_text(encoding="utf-8"))
    if not isinstance(ops, list):
        raise SystemExit("ops file must be a JSON array")
    secret = token()
    results = [run(op, secret, args.apply) for op in ops]
    output = {"applied": args.apply, "approval_ref": args.approval_ref or None, "results": results}
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(output, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
