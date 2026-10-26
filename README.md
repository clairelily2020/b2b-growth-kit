# b2b-growth-kit

A B2B marketing operating kit for small teams working with AI agents: a playbook that says what to do at each stage, workflows that sequence the work, 39 skills that each do one job, and a harness that checks the results.

[中文说明](README.zh-CN.md)

## How it fits together

```
playbook/          what to do at each stage, and why            (read by people)
   |
skills/b2b-growth-kit/workflows/   multi-step jobs: which skills, in which order, with which hand-offs
   |
skills/<name>/     one job each: inputs, process, output contract, gates   (read by agents)
   |
skills/b2b-growth-kit/policies/    rules written once: approvals, evidence, metrics, outreach
skills/b2b-growth-kit/profile/     your company's facts in one TOML file
   |
harness/           deterministic checks on drafts: evidence, metrics, attribution, landing pages, handoffs
```

Dependencies point one way. Skills never hardcode company facts (they read the profile) and never restate a policy (they link it). Change a rule in one place; change companies by swapping one file.

## Quick start

1. **Install the skills** into your agent's skills folder:

   ```bash
   git clone https://github.com/clairelily2020/b2b-growth-kit.git
   cp -R b2b-growth-kit/skills/* ~/.claude/skills/      # Claude Code
   cp -R b2b-growth-kit/skills/* ~/.codex/skills/       # Codex
   ```

   Policies, workflows and the profile schema live inside `skills/b2b-growth-kit/`, so they install with the skills and every link keeps working.

2. **Create your company profile.** Copy `skills/b2b-growth-kit/profile/example-company.toml` to `profiles/private/<your-company>/company.toml` in your working repo (git-ignored), or ask the agent: "set up a b2b-growth-kit profile for our company from our website".

3. **Ask for work, not for advice:** "Audit our Google Ads conversion tracking", "Build a prospect list from this exhibitor CSV", "Write a comparison page for '{competitor} alternatives'", "Run this week's growth review".

## Workflows

| Job | Workflow |
|---|---|
| Who we sell to and what we say | [positioning-sprint](skills/b2b-growth-kit/workflows/positioning-sprint.md) |
| Book meetings from a target list | [account-based-outbound](skills/b2b-growth-kit/workflows/account-based-outbound.md) |
| Meetings from a trade show or conference | [event-abm](skills/b2b-growth-kit/workflows/event-abm.md) |
| Win buyer questions in search and AI assistants | [content-to-citation](skills/b2b-growth-kit/workflows/content-to-citation.md) |
| Launch or fix search ads | [paid-search-launch](skills/b2b-growth-kit/workflows/paid-search-launch.md) |
| Founder and brand social presence | [founder-led-social](skills/b2b-growth-kit/workflows/founder-led-social.md) |
| Launch a product or feature | [product-launch](skills/b2b-growth-kit/workflows/product-launch.md) |
| The weekly marketing loop | [weekly-growth-review](skills/b2b-growth-kit/workflows/weekly-growth-review.md) |

## Skills

| Area | Skills |
|---|---|
| Hub | [b2b-growth-kit](skills/b2b-growth-kit/SKILL.md): loads the profile and policies, routes requests |
| Strategy | [icp-and-positioning](skills/icp-and-positioning/SKILL.md) · [offer-design](skills/offer-design/SKILL.md) · [competitive-intel](skills/competitive-intel/SKILL.md) · [market-signal-brief](skills/market-signal-brief/SKILL.md) · [voice-of-customer](skills/voice-of-customer/SKILL.md) |
| Content, SEO, GEO | [seo](skills/seo/SKILL.md) · [answer-engine-content](skills/answer-engine-content/SKILL.md) · [geo-citation-scout](skills/geo-citation-scout/SKILL.md) · [article-writer](skills/article-writer/SKILL.md) · [programmatic-pages](skills/programmatic-pages/SKILL.md) · [link-acquisition](skills/link-acquisition/SKILL.md) · [landing-page](skills/landing-page/SKILL.md) · [prepublish-qa](skills/prepublish-qa/SKILL.md) · [cms-draft-patcher](skills/cms-draft-patcher/SKILL.md) |
| Paid | [google-ads](skills/google-ads/SKILL.md) · [linkedin-ads](skills/linkedin-ads/SKILL.md) · [reddit-ads](skills/reddit-ads/SKILL.md) · [ad-creative](skills/ad-creative/SKILL.md) |
| Outbound and sales | [prospect-list-builder](skills/prospect-list-builder/SKILL.md) · [cold-email](skills/cold-email/SKILL.md) · [linkedin-outbound](skills/linkedin-outbound/SKILL.md) · [send-preflight](skills/send-preflight/SKILL.md) · [revenue-handoff](skills/revenue-handoff/SKILL.md) |
| Social and community | [founder-led-content](skills/founder-led-content/SKILL.md) · [brand-social-content](skills/brand-social-content/SKILL.md) · [social-engagement](skills/social-engagement/SKILL.md) · [content-calendar](skills/content-calendar/SKILL.md) · [creator-partnerships](skills/creator-partnerships/SKILL.md) · [reddit-community](skills/reddit-community/SKILL.md) |
| Campaigns | [campaign-brief](skills/campaign-brief/SKILL.md) · [campaign-review](skills/campaign-review/SKILL.md) · [launch-campaign](skills/launch-campaign/SKILL.md) |
| Data and operations | [marketing-data-ops](skills/marketing-data-ops/SKILL.md) · [marketing-reporting](skills/marketing-reporting/SKILL.md) · [performance-diagnosis](skills/performance-diagnosis/SKILL.md) · [growth-plan](skills/growth-plan/SKILL.md) · [ops-brief](skills/ops-brief/SKILL.md) · [martech-scouting](skills/martech-scouting/SKILL.md) |

Every skill follows the same shape: When to use, Inputs (including which profile fields it reads), Process, Output, Gates, References.

## Playbook

[playbook/](playbook/README.md) starts from where you are stuck (validation, first customers, repeatability, retention, scale), with practices, 15 channel cards, templates and field notes. Each chapter ends with the workflows and skills that execute it.

## Harness

```bash
cd harness && python3 -m b2b_harness ads --input examples/ads.json --as-of 2026-09-17
```

Four deterministic checks (`signal`, `ads`, `landing`, `handoff`) plus an approval-scope check. Offline, standard library only. Details in [harness/README.md](harness/README.md).

## Principles

- **Drafts, not side effects.** Skills research, draft and analyze freely. Publishing, sending, spending, editing live ads and writing to a CRM need a scoped approval ([approval-gates](skills/b2b-growth-kit/policies/approval-gates.md)).
- **Evidence over confidence.** Unknown is not zero; unverified is not rejected; no invented customers, quotes or numbers ([evidence-and-claims](skills/b2b-growth-kit/policies/evidence-and-claims.md)).
- **Honest channels.** No fake accounts, undisclosed promotion, bought reviews or attempts to evade platform rules ([outreach-compliance](skills/b2b-growth-kit/policies/outreach-compliance.md)).
- **Done means three different things:** draft ready, executed with a receipt, worked after the measurement window.

## Repository checks

```bash
python3 tools/check_repo.py
```

Checks links (including that skill links never leave `skills/`, so they survive installation), skill frontmatter and required sections, CSV shape, and private-data patterns. Add a local, git-ignored `.denylist.local` with names that must never appear (your company, customers, people) and the check enforces it. CI runs the same checks and the harness tests.

## Contributing and license

See [CONTRIBUTING.md](CONTRIBUTING.md) for the skill template and the rules for new skills. MIT licensed. Created by Claire.
