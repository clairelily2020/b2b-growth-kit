# Security and privacy

## What this repository contains

Instructions, templates, a fictional example company and offline checking code. No credentials, customer data or private company information should ever be committed.

## Scripts that call external services

- `skills/geo-citation-scout/scripts/query_perplexity.py` reads `PERPLEXITY_API_KEY` from the environment.
- `skills/cms-draft-patcher/scripts/webflow_draft_patch.py` reads `WEBFLOW_API_TOKEN` from the environment or a local `.env`. It runs as a dry run unless `--apply` and `--approval-ref` are given, and only writes drafts.

Neither script stores or prints secrets. The harness makes no network calls.

## Keeping your data private

- Put real company profiles under `profiles/private/`, which is git-ignored.
- Keep a local `.denylist.local` with names that must never be published; `tools/check_repo.py` blocks them.
- Review generated content for customer names, contact details and internal links before publishing it anywhere.

## Reporting a problem

If you find a leaked secret or personal data in this repository, open an issue without including the sensitive value, or contact the maintainer through GitHub at [clairelily2020](https://github.com/clairelily2020).
