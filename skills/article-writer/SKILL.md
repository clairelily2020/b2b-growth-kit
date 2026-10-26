---
name: article-writer
description: Draft or rewrite B2B blog articles and guides that follow the house structure set in the company profile (opening, short answer, body sections, FAQ, template-injected CTA), stay inside the claim boundary and are clean for a CMS rich-text field. Use for blog drafts, article rewrites, adding an FAQ, cleaning a post for the CMS, or keeping a table of contents tidy.
---

# Article writer

Produces long-form articles that read well, keep a tidy table of contents, and drop cleanly into a CMS template. Structure rules come from the profile, so each company can set its own.

## When to use

- New article or guide, or a rewrite of an existing one.
- Adding or fixing an FAQ.
- Cleaning an article body for a CMS rich-text field.
- For a page built to win one AI-search question, start with [answer-engine-content](../answer-engine-content/SKILL.md); this skill handles the long-form house style.

## Inputs

- Profile: `content.article` (structure rules), `voice`, `claims`, `positioning`, `offer`.
- Topic or existing draft, the target reader and question, and source material.

## Process

1. **One problem, one answer.** Write the reader's problem and the article's answer in two sentences before drafting. If you cannot, the topic is too broad.
2. **Apply the profile structure.** Typical shape: 2-4 opening paragraphs; the `first_h2` (for example "Short answer") with the conclusion; `body_h2_min` to `body_h2_max` substantive H2 sections; FAQ as the last H2 with 4-6 questions as H3s if `faq_last` is true. Need more detail? Use H3 under an existing H2 instead of adding H2s.
3. **Keep the table of contents useful.** H2s are real content sections only. No H2s for notes, placeholders, "CTA" or promotions.
4. **Respect the template.** If `cta_injected_by_template` is true, end the body at the FAQ and do not write a CTA block. Say so in the handoff if the user asks for an exception.
5. **Write product mentions as positive, specific outputs.** Describe what the product helps the reader review, decide or prepare, inside the `claims.claim_boundary`. Do not lead with what it cannot do, and do not inflate.
6. **Summary or excerpt field.** If the CMS has one, write 2-4 sentences stating the reader's problem, the answer and the product angle. Never reuse the title, the meta description or the heading list.
7. **Clean the body for the CMS:** semantic HTML or clean Markdown, no scripts or inline styles, no pasted plain text with broken line breaks.
8. **Run the handoff checks** below, then the fact check in [answer-engine-content](../answer-engine-content/references/fact-check-gates.md).

## Output

```markdown
Title / meta description (under 155 characters) / summary field
## Draft
## Handoff checklist (each item pass or fail)
## Claims used, with the proof point or source for each
```

## Gates

- Handoff checklist: first H2 matches `first_h2`; H2 count within range; body ends with FAQ when required; no handwritten CTA unless approved as an exception; nothing outside the claim boundary; no banned phrases.
- Claims follow [evidence-and-claims](../b2b-growth-kit/policies/evidence-and-claims.md).
- A finished draft is not a published article; see [approval-gates](../b2b-growth-kit/policies/approval-gates.md).

## References

- Rendered checks after the draft is in the CMS: [prepublish-qa](../prepublish-qa/SKILL.md)
- Writing the draft into the CMS: [cms-draft-patcher](../cms-draft-patcher/SKILL.md)
