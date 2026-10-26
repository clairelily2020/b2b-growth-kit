# Harness

Deterministic, offline checks for marketing drafts. The skills tell an agent how to do the work; the harness checks the result the same way every time. It never browses, sends, publishes, spends or writes to a CRM.

Python 3.11 or newer, standard library only.

## Run

```bash
cd harness
python3 -m b2b_harness signal  --input examples/signal.json  --as-of 2026-09-17
python3 -m b2b_harness ads     --input examples/ads.json     --as-of 2026-09-17
python3 -m b2b_harness landing --input examples/landing.json --as-of 2026-09-17
python3 -m b2b_harness handoff --input examples/handoff.json --as-of 2026-09-17
```

Options:

- `--profile path` uses your company profile (`.toml` from the kit, or a flat `.json`). Default: the DemoCo example in `skills/b2b-growth-kit/profile/`.
- `--as-of YYYY-MM-DD` is required, so freshness checks are reproducible.
- `--output DIR` writes `result.json` and `brief.md` into a new directory and refuses to overwrite an existing one.
- `--lang zh` translates the brief's headings.

Exit code 0 means the analysis finished; read `status` and `reasons` for the verdict. Exit code 2 means invalid input.

## Workflows

| Workflow | Checks | Matching skill |
|---|---|---|
| `signal` | Hypothesis, smallest test, metric, stop rule and window are present; evidence is current and reviewed | [market-signal-brief](../skills/market-signal-brief/SKILL.md) |
| `ads` | Metrics are valid numbers; CPC and CTR recomputed; CAC and ROAS only with a verified, current, unconflicted identity join | [google-ads](../skills/google-ads/SKILL.md), [marketing-reporting](../skills/marketing-reporting/SKILL.md) |
| `landing` | Page is isolated from the homepage; QA items passed; CTA URL valid; every proof claim backed by reviewed evidence | [landing-page](../skills/landing-page/SKILL.md) |
| `handoff` | Owner present; permission and suppression known; stated intent evidenced; stage promotion backed by reviewed evidence and confirmed fit; customer stage needs payment evidence | [revenue-handoff](../skills/revenue-handoff/SKILL.md) |

`approval_check(action, approval, as_of)` in `b2b_harness/core.py` checks that an approval matches the exact target, action and version, and is not revoked or expired. It is a library function; it never executes anything.

## Contracts

The rules the harness enforces are written once, in the kit's policies:

- Evidence records and statuses: [evidence-and-claims](../skills/b2b-growth-kit/policies/evidence-and-claims.md)
- Metric definitions and the attribution gate: [metrics-definitions](../skills/b2b-growth-kit/policies/metrics-definitions.md)
- Approvals and draft vs executed vs worked: [approval-gates](../skills/b2b-growth-kit/policies/approval-gates.md)

Every result carries `external_actions: []` and `delivery: "local_only"`. Review metadata in evidence is user-supplied; sources are not fetched or verified.

## Test

```bash
cd harness
python3 -m unittest discover -s tests -v
```
