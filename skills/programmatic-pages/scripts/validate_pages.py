#!/usr/bin/env python3
"""Validate generated Markdown pages before they go into a CMS. Standard library only.

Checks each file for:
  - leaked process language ("based on the official website", "use this table", ...)
  - unfilled placeholders ({field}, [TODO], TBD, lorem ipsum)
  - Markdown or HTML tables, when --no-tables is set (some rich-text fields break them)
  - empty sections (a heading followed by a same- or higher-level heading)
  - near-duplicate pages (word 5-gram Jaccard similarity above --max-similarity)

Usage:
  python3 scripts/validate_pages.py pages/*.md [--no-tables] [--banned extra.txt] [--max-similarity 0.8]

Exit code 0 = pass, 1 = findings, 2 = usage error.
"""
import argparse
import re
import sys
from itertools import combinations
from pathlib import Path

DEFAULT_BANNED = [
    (r"based on the official (?:web)?site", "process language leaked into public copy"),
    (r"according to (?:the )?official (?:web)?site", "process language leaked into public copy"),
    (r"\buse this table\b", "refers to a table the reader may not see"),
    (r"\bour (?:api|database) (?:has|shows) a matching record\b", "internal coverage note in public copy"),
    (r"\bas an ai\b", "assistant phrasing in public copy"),
    (r"\blorem ipsum\b", "placeholder text"),
    (r"\bTBD\b|\bTODO\b|\[TODO[^\]]*\]", "unfilled placeholder"),
    (r"\{[a-z_]+\}", "unfilled template variable"),
    (r"\bstrong fit\b|\bgreat fit\b", "vague fit language instead of facts"),
]


def load_banned(path):
    rules = list(DEFAULT_BANNED)
    if path:
        for line in Path(path).read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#"):
                rules.append((re.escape(line), "custom banned phrase"))
    return rules


def shingles(text, size=5):
    words = re.findall(r"[a-z0-9]+", text.lower())
    return {" ".join(words[i:i + size]) for i in range(max(len(words) - size + 1, 0))}


def check_file(path, text, banned, no_tables):
    findings = []
    for pattern, reason in banned:
        for match in re.finditer(pattern, text, re.IGNORECASE):
            line = text.count("\n", 0, match.start()) + 1
            findings.append(f"{path}:{line}: '{match.group(0)}' ({reason})")
    lines = text.splitlines()
    if no_tables:
        for number, line in enumerate(lines, start=1):
            stripped = line.strip()
            if (stripped.startswith("|") and "|" in stripped[1:]) or re.search(r"</?table\b", stripped, re.I):
                findings.append(f"{path}:{number}: table not allowed in this field")
    previous = None  # (line number, level) of a heading with no content yet
    for number, line in enumerate(lines, start=1):
        if not line.strip():
            continue
        heading = re.match(r"^\s*(#{1,6})\s", line)
        if heading:
            level = len(heading.group(1))
            if previous is not None and level <= previous[1]:
                findings.append(f"{path}:{previous[0]}: empty section (no content before the next heading)")
            previous = (number, level)
        else:
            previous = None
    return findings


def main():
    parser = argparse.ArgumentParser(description="Validate generated Markdown pages.")
    parser.add_argument("files", nargs="+", type=Path)
    parser.add_argument("--no-tables", action="store_true")
    parser.add_argument("--banned", help="file with extra banned phrases, one per line")
    parser.add_argument("--max-similarity", type=float, default=0.8)
    args = parser.parse_args()
    banned = load_banned(args.banned)
    findings, texts = [], {}
    for path in args.files:
        if not path.exists():
            print(f"{path}: file not found", file=sys.stderr)
            return 2
        text = path.read_text(encoding="utf-8")
        texts[path] = shingles(text)
        findings += check_file(path, text, banned, args.no_tables)
    for (a, sa), (b, sb) in combinations(texts.items(), 2):
        if sa and sb:
            similarity = len(sa & sb) / len(sa | sb)
            if similarity > args.max_similarity:
                findings.append(f"{a} ~ {b}: {similarity:.0%} similar (thin or duplicate content risk)")
    for finding in findings:
        print(finding)
    print(f"{'FAIL' if findings else 'PASS'}: {len(args.files)} files, {len(findings)} findings")
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
