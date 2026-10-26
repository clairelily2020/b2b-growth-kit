# Page contracts

Each page type has a field contract. Collect into a local CSV first; the CSV is internal and can use tables freely.

## Event or trade show guide

| Field | Meaning |
|---|---|
| `entity_name` | Public event name |
| `date_start`, `date_end` | Event days |
| `city`, `country`, `venue` | Location |
| `organizer` | Organizer name |
| `official_url` | Official homepage |
| `exhibitor_url` | Official exhibitor list or directory, if any |
| `registration_url`, `agenda_url`, `speaker_url` | If published |
| `last_checked` | Date the official pages were checked |
| `internal_id` | Matching record in your own data, or blank |
| `internal_status` | covered / not_covered / auth_blocked / timeout / empty / not_checked |
| `priority_source` | How the entity entered the list: search / customer request / competitor coverage / manual |

Typical sections (include only those with verified facts): What is {event}; Dates and location; Who attends or exhibits; Exhibitors and sponsors; Agenda and speakers; Registration; How {product} helps prepare; FAQ.

Run window: events starting in the next 90 days, refreshed monthly.

## Industry or use-case page

`entity_name`, `definition`, `buyer_roles`, `top_jobs`, `common_alternatives`, `proof_point_keys` (from the profile), `sources`, `last_checked`.

## Integration page

`entity_name`, `integration_type` (native, API, export), `what_syncs`, `setup_steps_url`, `limitations`, `last_verified_version`, `last_checked`.

## Location page

`entity_name`, `region`, `local_specifics` (regulation, language, market facts with sources), `offices_or_partners` (only if real), `last_checked`. Skip location pages that would differ only by the city name.

## Glossary term

`term`, `plain_definition`, `example`, `related_terms`, `source` (for formal definitions), `last_checked`.

## Copy rules for every type

Do:
- State facts directly, with dates for anything time-bound.
- Say plainly when something is not published yet.
- Tie the CTA to a concrete next step from `offer`.

Do not:
- Expose process ("based on the official website", "our database has a matching record").
- Use vague fit language ("strong fit for", "great opportunity") in place of facts.
- Claim data categories you do not have, or private contact access, verified buyer lists or guaranteed meetings.
- Leave placeholder or table residue from internal planning sheets.

## Known CMS failure modes

1. Empty Markdown table cells render as blank rows.
2. HTML table embeds render as plain inline text in some rich-text fields.
3. Items written to the wrong collection.
4. Internal planning text left in public copy.
5. Filler written to make a section look complete.

The validator catches 1, 2, 4 and most of 5; check the collection by hand.
