# Instructions for agents working in this repository

## Using the kit for marketing work

1. Read [skills/b2b-growth-kit/SKILL.md](skills/b2b-growth-kit/SKILL.md) first. It defines the load order: profile, then policies, then a workflow or a single skill.
2. Use the profile the user names; otherwise `profiles/private/*/company.toml`; otherwise the DemoCo example, and say so.
3. Read only the skill files the task needs, not every skill.
4. Follow the user's language; skill files are in English.
5. Research, drafts, analysis and local files need no approval. Publishing, sending, spending, editing live ads and CRM writes follow [approval-gates](skills/b2b-growth-kit/policies/approval-gates.md).

## Changing the kit itself

- One job per skill. Before adding a skill, check whether an existing one should grow instead.
- Never put company facts in a skill; add a profile field and document it in [profile/SCHEMA.md](skills/b2b-growth-kit/profile/SCHEMA.md).
- Never restate a policy in a skill; link it.
- Links inside `skills/` must stay inside `skills/`, or they break after installation.
- Keep each SKILL.md body under about 150 lines; move detail into `references/` and link it from the step that needs it.
- Run `python3 tools/check_repo.py` and the harness tests before committing.
- Never commit private profiles, credentials, customer data, exports or the local denylist.
