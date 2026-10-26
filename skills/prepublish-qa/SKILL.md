---
name: prepublish-qa
description: Review a rendered page or CMS preview before publishing (articles, landing pages, programmatic pages) for structure, table of contents, CTA rendering, links and UTMs, tracking, raw code leaks, mobile layout and claim risk, and report findings by severity with exact fixes. Use when asking whether a page or blog post is ready to publish, for preview QA, or after a CMS import.
---

# Prepublish QA

Checks what visitors will actually see, not the draft. Many failures only appear after the CMS renders the content: broken tables, raw code, duplicated CTAs, links with leaked parameters.

## When to use

- A draft is in the CMS and someone asks "is it ready?".
- After importing or patching content into a CMS.
- Before switching an ad or email to a new landing page.

## Inputs

- The preview or staging URL (or rendered HTML), and the source draft for comparison.
- Profile: `content.article`, `offer` (CTA label, URL, UTM rules), `claims`, `measurement.conversion_events`.

## Process

Check in this order so structural failures surface first:

1. **Structure:** required sections present (for articles, the profile's first H2 and FAQ rules); headings in order; no empty sections; no leftover old content lower on the page.
2. **Table of contents:** lists only real content sections; no CTA, FAQ or promotional headings if the template excludes them.
3. **CTA:** appears where the template intends, once; renders as a button, not text; label and destination match `offer`; heading size matches the design.
4. **Links and UTMs:** every link resolves; CTA links carry the right UTMs; UTMs do not leak into navigation or footer links; no staging hosts, test parameters or private document links.
5. **Rich-text integrity:** no visible script or style fragments, no broken tables, lists and headings survived the import, images have alt text.
6. **Tracking:** the conversion event fires once on a test submission; forms reach their destination.
7. **Mobile:** readable text, tappable buttons, no horizontal scroll, images not cropped badly.
8. **Claims:** nothing banned or unsupported crept in during edits.

## Output

Findings first, no praise:

```markdown
| Severity | Problem | Where (section or selector) | Blocks publish? | Exact fix |
Verdict: ready for publishing approval / blocked
Checks not run (and why)
```

Severity: blocker (wrong claim, broken CTA or form, missing required section, visible code), major (tracking or UTM error, TOC pollution, mobile breakage), minor (polish).

## Gates

- Any blocker means "blocked", whatever the deadline.
- A pass is a quality verdict, not permission; publishing follows [approval-gates](../b2b-growth-kit/policies/approval-gates.md).
- Claim checks follow [evidence-and-claims](../b2b-growth-kit/policies/evidence-and-claims.md). Checks you could not run are reported as not run.

## References

- Fixing the CMS draft: [cms-draft-patcher](../cms-draft-patcher/SKILL.md)
