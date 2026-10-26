# Workflow: paid search launch

**Goal:** a search campaign that spends only on proven intent, measured by a conversion signal you trust.
**Stage:** first customers onward, once the offer is clear.
**Time box:** setup in week 1; judge after the learning period; weekly reviews.

| Step | Skill | Input | Hand-off artifact |
|---|---|---|---|
| 1 | [google-ads](../../google-ads/SKILL.md), conversion tracking check first | Conversion actions, tags, goals | Tracking health table and fixes |
| 2 | [offer-design](../../offer-design/SKILL.md) | Intent levels | Offer and CTA per ad group |
| 3 | [landing-page](../../landing-page/SKILL.md) | Offer, keywords | Page per intent, tracking tested |
| 4 | [google-ads](../../google-ads/SKILL.md) | Keyword clusters from [seo](../../seo/SKILL.md) if available | Campaign structure, negatives, bid strategy fitted to conversion volume |
| 5 | [ad-creative](../../ad-creative/SKILL.md) | Angles | RSA headlines and descriptions with character counts |
| 6 | [campaign-review](../../campaign-review/SKILL.md) + [prepublish-qa](../../prepublish-qa/SKILL.md) | Steps 3-5 | Ship call, page QA |
| 7 | Approval by `approvals.spend`, then launch | | Change log |
| 8 | [google-ads](../../google-ads/SKILL.md) weekly | Search terms, conversions | Keep, watch, pause and negatives |
| 9 | [performance-diagnosis](../../performance-diagnosis/SKILL.md) | After the measurement window | Diagnosis and next test |

**Gates:** no bid strategy change on a broken conversion signal; no CAC or ROAS without verified attribution ([metrics-definitions](../policies/metrics-definitions.md)); live edits per [approval-gates](../policies/approval-gates.md).

**Done when:** the campaign has a healthy primary conversion, a clean keep/watch/pause state, and a decision on scaling or stopping with evidence.
