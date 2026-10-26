---
name: cms-draft-patcher
description: Write approved article bodies or field fixes into existing CMS items as drafts only, from clean local sources, with a dry run by default, explicit approval reference for writes, cleanup of code fragments and a post-write verification checklist. Includes a Webflow adapter script. Use when repairing a corrupted rich-text field, replacing a repeated CTA across items, updating a field on selected items, or loading an approved draft into the CMS.
---

# CMS draft patcher

Narrow, reversible CMS edits. Fetch the item, change only the named field, save it as a draft, verify. The live page stays untouched until someone publishes it.

## When to use

- An approved article or page body needs to go into an existing CMS item.
- A rich-text field shows raw code, broken tables or a duplicated CTA.
- One field must be corrected on a known list of items.
- Not for creating collections, changing schemas, bulk edits of unknown items, or publishing.

## Inputs

- The exact items: collection ID and item ID for each, from the CMS.
- A clean local source for each change (exported HTML, approved Markdown converted to HTML, or a field value).
- The field slugs to write. Never guess a field slug; read it from the item.
- For writes: the approval reference for these items and this version.

## Process

1. **Write an ops file** describing each change. The Webflow format is documented at the top of [scripts/webflow_draft_patch.py](scripts/webflow_draft_patch.py). Use `assert_contains` to require text that must be present, so a wrong source fails loudly.
2. **Clean the source.** Strip inline `<svg><style>` fragments, unwanted template sections by class, and any repeated junk with narrow patterns. The script refuses sources containing `<script>`.
3. **Dry run:** `python3 scripts/webflow_draft_patch.py --ops ops.json --report dry-run.json`. Check each item's name and slug match what you expect, and that `changed` and lengths make sense.
4. **Apply after approval:** `python3 scripts/webflow_draft_patch.py --ops ops.json --apply --approval-ref "<where it was approved>" --report applied.json`. Items are written with `isDraft: true`.
5. **Verify in the CMS:** each item shows changes in draft; the body starts with real content, not CSS or code; prepended or appended snippets sit in the right place; nothing else on the item changed. Then run [prepublish-qa](../prepublish-qa/SKILL.md) on the preview.

Other CMSs: follow the same pattern (fetch, change one field, save as draft, report). See [references/adapter-pattern.md](references/adapter-pattern.md).

## Output

```markdown
## Ops summary
| Label | Item (name / slug) | Field | Change | Dry-run result |
## Applied (only after approval): status per item, approval reference, report path
## Verification checklist results
```

## Gates

- Dry run first, always. Writing requires an approval for these exact items and version; see [approval-gates](../b2b-growth-kit/policies/approval-gates.md).
- Draft only. Publishing is a separate approval and a separate action.
- Tokens come from the environment; never print or store them in files that get committed.

## References

- [references/adapter-pattern.md](references/adapter-pattern.md)
