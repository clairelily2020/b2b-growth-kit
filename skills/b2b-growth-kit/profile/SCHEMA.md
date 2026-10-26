# Company profile schema

A profile is one TOML file that holds every company-specific fact the skills need. Skills never hardcode company facts; they read this file. Changing companies means swapping the profile, nothing else.

- Example: [`example-company.toml`](example-company.toml) (DemoCo, fictional)
- Your real profile: `profiles/private/<company>/company.toml` in your working repo (git-ignored), or any path you give the agent

## Rules for skills that read a profile

1. Read only the sections listed in the skill's **Inputs**.
2. An empty string or missing key means **unknown**. Say it is unknown; never fill it with a plausible guess.
3. A claim in generated copy must trace to `positioning.proof_points` (and from there to an evidence record) or be labelled as an opinion.
4. Anything in `claims.banned` must not appear, paraphrased or not.
5. Use roles from `approvals`, never personal names, when stating who must approve.

## Sections

| Section | Key fields | Used by |
|---|---|---|
| `company` | `name`, `website`, `one_liner`, `category`, `stage`, `team_size` | all |
| `icp` | `summary`, `segments`, `regions`, `economic_buyer`, `champion`, `users`, `triggers`, `exclusions` | positioning, prospecting, ads, content |
| `positioning` | `category_frame`, `problem`, `alternatives`, `differentiators`, `proof_points[{claim_key, statement}]` | copy, landing pages, ads, sales |
| `offer` | `primary`, `entry_offer`, `pricing_policy`, `pricing_url`, `cta_label`, `cta_url`, `utm.*` | every skill that writes a CTA or link |
| `claims` | `banned`, `claim_boundary` | every skill that writes copy |
| `competitors` | `mention_policy`, `named[{name, positioning, our_angle}]` | competitive intel, comparison pages, ads |
| `voice` | `tone`, `avoid`, `language`, `personas[{role, display_name, signature, topics}]` | social, email, articles |
| `channels` | `active`, account URLs and handles | router, calendar, social |
| `outreach` | `sending_domains`, `suppression_source`, `daily_cap_*` | cold email, LinkedIn, send preflight |
| `content.article` | `first_h2`, `body_h2_min`, `body_h2_max`, `faq_last`, `cta_injected_by_template`, `tables_allowed` | article writer, prepublish QA |
| `measurement` | `timezone`, `currency`, tool categories, `conversion_events[{name, stage, primary}]` | data ops, reporting, ads, landing pages |
| `approvals` | role per action: `publish`, `send`, `spend`, `ads_edit`, `crm_write` | every gate |

## Harness mapping

The harness (`harness/` in the repo) reads the same file and needs only four values: `company.name`, `icp.summary`, `offer.primary`, `offer.cta_url`. It fails with exit code 2 if any is missing.
