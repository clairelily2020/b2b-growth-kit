# Contributing

Issues and pull requests are welcome at [clairelily2020/b2b-growth-kit](https://github.com/clairelily2020/b2b-growth-kit).

## Before adding a skill

- Does an existing skill already cover this job? Extending it is usually better than a near-duplicate.
- Is it one job with a clear output? "Do marketing" is a workflow, not a skill.
- Which profile fields does it need? Add missing fields to the schema instead of hardcoding facts.

## Skill template

Save as `skills/<name>/SKILL.md`. The folder name and `name` must match, in kebab-case.

```markdown
---
name: your-skill-name
description: What it does in one or two sentences, then "Use for ..." with the requests and phrases that should trigger it. 40-1024 characters, no angle brackets.
---

# Title

One short paragraph on why this job matters and what good looks like.

## When to use

- Situations that call for it.
- Where a neighbouring skill is the better fit.

## Inputs

- Profile: the sections it reads.
- Other material the user supplies.

## Process

1. Judgment criteria and decisions, not keystroke instructions.
2. Link `references/` files from the step that needs them.

## Output

A template of the deliverable.

## Gates

- What must be true before handing off, linking the relevant policy under ../b2b-growth-kit/policies/.

## References

- Related skills and reference files.
```

Rules the checker enforces (`python3 tools/check_repo.py`):

- Frontmatter has only `name` and `description`.
- Sections `When to use`, `Inputs`, `Process`, `Output` and `Gates` exist.
- At least one link to a policy.
- Links resolve and never leave `skills/`.
- Body over 150 lines warns; over 220 fails.
- No private data patterns, and nothing from your local `.denylist.local`.

## Playbook changes

Mark advice as a practice record, a working suggestion or a hypothesis. Use dated sources for anything that changes over time. Do not publish customer names, contact data, internal links or prices.

## Harness changes

Keep it offline and standard-library only. Every new check gets a test in `harness/tests/` and, if it is a new workflow, an example in `harness/examples/`.
