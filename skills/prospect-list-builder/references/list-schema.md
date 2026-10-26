# List schema

## Account columns

```text
company_name, domain, company_page_url, country, region, segment, category,
source, source_type, source_date, source_confidence,
identity_status, icp_score, icp_reason, contactability, tier, reject_reason,
research_angle, trigger, recommended_next_step, suppression_status, notes
```

| Column | Values |
|---|---|
| `source_type` | official_table, first_party, database, directory, search, ocr_or_logo, user_list |
| `source_confidence` | high, medium, low |
| `identity_status` | verified, unverified, rejected |
| `icp_score` | 0-5 with `icp_reason` in one line |
| `contactability` | known_contact_path, role_found, unknown |
| `tier` | A, B, C, reject |
| `suppression_status` | clear, suppressed, unknown (unknown blocks outreach) |

Event-specific optional columns: `event_name`, `booth`, `hall_or_zone`, `exhibitor_category`.

## Contact columns (add only when contacts are in scope)

```text
contact_name, title, seniority, role_in_buying (user, champion, economic_buyer),
contact_profile_url, contact_source, contact_source_date,
email_status (unknown, found, verified), contact_verification_status
```

Never fill an email by guessing a pattern. Never include personal (non-work) email addresses.

## Quality rules

- `verification_status` style fields are required on every row; a list without them is not research-ready.
- OCR or logo matches need a second source before tier A.
- If fewer than the target number of usable rows remain, report the shortfall and suggest sources; do not pad.
- If more than 20% of an input file is rejected, add a short note explaining why.

## Summary block

```text
Input rows:
Tier A / B / C:
Unverified (kept):
Rejected:
Top rejection reasons:
Suppressed:
Shortfall vs target:
Recommended next step:
```
