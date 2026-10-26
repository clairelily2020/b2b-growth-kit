# Engine querying

Engines differ in reliability and access. Use the methods below, and label anything you could not retrieve as "not retrieved". Never borrow another engine's result to fill a gap.

## Perplexity

Three paths, in order of preference for a full batch:

**A. API (when a key exists).** Run [`scripts/query_perplexity.py`](../scripts/query_perplexity.py):

```bash
python3 scripts/query_perplexity.py "{Competitor} alternatives for {your ICP}"
```

Needs `PERPLEXITY_API_KEY`. Output is JSON: `{"query", "answer", "citations": [{"url", "title"}]}`. API citations may differ from the consumer product because models and retrieval can differ. Spot-check one or two questions against the web UI the first time.

**B. Browser automation (spot checks only).** Navigating and reading perplexity.ai with a browser tool works for one or two questions. Repeated automated navigation tends to trigger human-verification challenges and read restrictions. Do not try to get around them; stop and use path C.

**C. Manual run plus Markdown export (most reliable for a batch).**

1. The user pastes the questions into perplexity.ai one by one. They can be follow-ups in one thread, so one export covers several questions.
2. The user exports the thread as Markdown (or shares the link).
3. Read the exported file. It contains footnote citations with the full URL list and which sentence used which source, which is more detailed than the on-page links tab.

This path needs the user's time but carries no automation risk.

## ChatGPT search

1. **API:** with an OpenAI API key, the Responses API web-search tool returns structured source URLs. Suitable for scale.
2. **Browser:** in the user's own logged-in browser, enable search, submit the question, and read the source cards. Keep the pace slow; expect occasional verification prompts or limits.

If neither path is available, report "ChatGPT citations not retrieved". Do not substitute another engine's results.

## Google AI Overviews

No official API. In order of reliability:

1. **Third-party SERP API** (for example SerpApi or DataForSEO) if the user already has an account. Do not push them to buy one.
2. **Manual search.** AI Overviews do not trigger every time; it depends on login, region and history, and automated browsers often do not see them. Record what you see; "not triggered this time, re-check manually" is not the same as "Google has no answer".

When this column is thin, say the gap comes from engine access limits.

## Rate limits

- Batch the work (15-25 questions times 3 engines); do not fire dozens of requests at one engine in a burst.
- Follow the Perplexity API rate limits of the user's plan.
- Space out browser queries.
- Read-only throughout: no posting, no high-frequency scraping.
