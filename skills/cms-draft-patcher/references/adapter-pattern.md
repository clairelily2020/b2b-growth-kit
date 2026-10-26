# Adapter pattern for other CMSs

The Webflow script is one adapter. Any CMS adapter should keep the same contract so the skill's gates still hold.

## Contract

1. **Fetch before write.** Read the current item and keep a copy of the old field value in the report.
2. **Change only named fields.** Merge the change into the fetched data; never send a partial object that could blank other fields.
3. **Draft state only.** Use the CMS's draft, staged or unpublished state. If the CMS has no draft state, the adapter must refuse to write and say so.
4. **Dry run by default.** Writing needs an explicit flag plus an approval reference recorded in the report.
5. **Report every item:** identifier, human-readable name, field, changed or unchanged, old and new length, status, approval reference.
6. **Secrets from the environment.** Never hardcode tokens or account IDs in the script or ops files.
7. **Refuse unsafe content.** No scripts in rich text; validate required text is present.

## Mapping notes

| CMS | Draft mechanism to use |
|---|---|
| Webflow (API v2) | `PATCH /collections/{id}/items/{item}` with `isDraft: true` |
| WordPress (REST) | Update with `status: draft` on unpublished posts; for published posts create a revision or pending copy instead of editing live |
| Contentful | Update the entry without calling publish |
| Sanity | Write to the `drafts.` document ID |
| HubSpot CMS | Update the draft buffer, not the live version |

Check the current API documentation of your CMS before relying on these; the table is a starting point, not a guarantee.
