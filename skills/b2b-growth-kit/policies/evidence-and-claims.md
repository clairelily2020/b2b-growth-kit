# Evidence and claims

Marketing work fails quietly when a guess becomes a "fact" three documents later. These rules keep every claim traceable.

## Evidence records

Any fact that a decision or a piece of copy depends on is recorded as:

| Field | Meaning |
|---|---|
| `id` | Unique ID |
| `claim_key` | What the fact is about, e.g. `product.capability`, `competitor.pricing`, `attribution.identity_join` |
| `statement` | The fact in one sentence |
| `source` | URL, file, export or person, specific enough to re-check |
| `observed_at` | When it was observed |
| `expires_at` | When it must be re-checked (pricing and competitor facts expire fast) |
| `review` | Optional: reviewer role, review date, `source_checked: true`, decision accepted or rejected |

Status follows from the fields: `unreviewed`, `reviewed`, `rejected`, or `stale` (expired, overrides the others). Only `reviewed` evidence supports a published claim. The harness computes these statuses deterministically.

## Rules

1. **Unknown is not zero.** A missing number is reported as unknown. Never write 0, "none" or "not significant" for data you did not see.
2. **Unverified is not rejected.** A login wall, rate limit or blocked page means the item is unverified. Do not drop it as a reject and do not mark it verified.
3. **Separate the three kinds of statements.** Label each as fact (with source), inference (what you conclude from facts), or recommendation (what to do). Do not let an inference read like a fact.
4. **Conflicts stay visible.** If two current sources disagree on the same `claim_key`, report both and stop relying on either until resolved.
5. **Date everything time-sensitive.** Prices, rankings, feature lists, event dates and headcounts carry the date they were observed.
6. **Vendor statements are assertions.** A company's own page proves what the company says, not that it is true.
7. **Engagement is not demand.** Likes, opens and impressions are signals of attention, not of buying intent.
8. **No invented specifics.** Do not make up customer names, quotes, logos, statistics, case results or testimonials. Use a clearly marked placeholder such as `[CUSTOMER QUOTE NEEDED]`.

## Claims in copy

- Product claims must map to `positioning.proof_points` in the profile, which map to reviewed evidence.
- Anything in `claims.banned` is never written, including softened paraphrases.
- Superlatives (best, leading, #1, fastest) need a cited, dated ranking or are removed.
- Comparisons with competitors follow `competitors.mention_policy` and cite the competitor's public page with a date.
