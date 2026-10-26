# Content classification

Fetch each cited URL and classify it on three dimensions.

## 1. Source type

| Type | Signal | Example |
|---|---|---|
| Competitor site | The domain is a competitor's product or landing page | A competitor's own comparison page |
| Review aggregator | Rating and review sites | A product page on a software review site |
| Community / UGC | Reddit, Quora, Hacker News, forums | A thread in a marketing subreddit |
| Blog / tutorial | Independent blogger or publication how-to or opinion | "How to do X" on a marketing blog |
| News / media | News sites, trade press | A launch story in tech press |
| Docs / help center | A tool's documentation rather than a marketing page | A vendor help article |
| Video | Review or tutorial videos | "{Competitor} alternatives" video |

Video citations are not rare (often 2-3 in a batch of 15). One occurrence is an observation. Several in one batch are a signal to evaluate video content; raise it in the report's findings.

## 2. Content structure

| Structure | Signal |
|---|---|
| Comparison table | Options side by side on features, price or criteria |
| Q&A / FAQ | Questions as headings with direct answers |
| Narrative | Case story, first-person experience, timeline |
| Listicle | "Top 10 X" numbered list |
| Data / research | Report built around data or survey results |

## 3. Freshness

Look for the published or updated date: URL date, footer, "Last updated", outdated screenshots or prices. Over 18 months without an update counts as stale; stale winners are good targets because engines tend to replace them. If no date is visible, write "date unknown". Do not guess.

## Edge cases

- A URL fits several types (a Reddit post with a comparison table): classify by the main carrier of information.
- The citation is an aggregation page (a search results page): record it as "aggregator, unclassifiable", exclude it from type counts, but mention it.
- Fetch failed (login wall, CDN block, obvious content farm): record "fetch failed". Do not describe content you did not see.
