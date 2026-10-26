#!/usr/bin/env python3
"""Query Perplexity's Sonar API and print the answer + citations as JSON.

Usage:
    python3 scripts/query_perplexity.py "{Competitor} alternatives for {your ICP}"
    python3 scripts/query_perplexity.py "some query" --model sonar-pro

Requires the PERPLEXITY_API_KEY environment variable.

Output (stdout, JSON):
    {
        "query": "...",
        "answer": "...",
        "citations": [
            {"url": "...", "title": "..."},  # title may be null if the API didn't provide one
            ...
        ]
    }

On failure, prints a JSON object with an "error" field to stdout and exits non-zero.
No citation data is fabricated: if the API returns none, "citations" is an empty list.
"""

import argparse
import json
import os
import sys
import urllib.error
import urllib.request

API_URL = "https://api.perplexity.ai/chat/completions"


def query_perplexity(query: str, model: str, timeout: int) -> dict:
    api_key = os.environ.get("PERPLEXITY_API_KEY")
    if not api_key:
        return {"error": "PERPLEXITY_API_KEY environment variable is not set."}

    payload = {
        "model": model,
        "messages": [{"role": "user", "content": query}],
    }
    req = urllib.request.Request(
        API_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            body = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", errors="replace")
        return {"error": f"HTTP {e.code} from Perplexity API: {detail}"}
    except urllib.error.URLError as e:
        return {"error": f"Network error reaching Perplexity API: {e}"}
    except Exception as e:  # noqa: BLE001 - surface any parse/runtime error as data, not a crash
        return {"error": f"Unexpected error: {e}"}

    answer = ""
    try:
        answer = body["choices"][0]["message"]["content"]
    except (KeyError, IndexError, TypeError):
        pass

    citations = []
    # Newer API responses use "search_results" (structured); older ones used a
    # flat "citations" list of URL strings. Handle both without assuming either exists.
    for item in body.get("search_results", []) or []:
        url = item.get("url")
        if url:
            citations.append({"url": url, "title": item.get("title")})
    if not citations:
        for url in body.get("citations", []) or []:
            citations.append({"url": url, "title": None})

    return {"query": query, "answer": answer, "citations": citations}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", help="The question to ask Perplexity")
    parser.add_argument(
        "--model",
        default="sonar",
        help="Perplexity model to use (default: sonar)",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=60,
        help="Request timeout in seconds (default: 60)",
    )
    args = parser.parse_args()

    result = query_perplexity(args.query, args.model, args.timeout)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if "error" in result else 0


if __name__ == "__main__":
    sys.exit(main())
