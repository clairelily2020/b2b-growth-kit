#!/usr/bin/env python3
"""Repository checks for b2b-growth-kit. Standard library only.

Checks:
  1. Relative Markdown links resolve.
  2. Text files end with a newline.
  3. CSV rows match their header width.
  4. Each skill has valid frontmatter (name = folder, description present),
     the required sections, a length budget, and at least one policy link.
  5. No private data patterns (tokens, keys, local paths, real emails, phone numbers).
  6. No term from the local, untracked .denylist.local file (company names, people,
     internal IDs). The denylist is never committed. One term per line; append
     "@allow path1 path2" to permit the term in specific files (e.g. the author name
     in LICENSE).

Usage: python3 tools/check_repo.py [--strict]
  --strict  also fail on warnings (skill body over the soft line budget)
"""
import csv
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent.parent
TEXT_SUFFIXES = {".md", ".csv", ".toml", ".py", ".json", ".yml", ".yaml", ".txt", ".sh"}
SKIP_DIRS = {".git", "__pycache__", "outputs", "private"}
HUB = "b2b-growth-kit"
REQUIRED_SECTIONS = ("## When to use", "## Inputs", "## Process", "## Output", "## Gates")
SOFT_LINES, HARD_LINES = 150, 220
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
LINK_RE = re.compile(r"\]\(([^)\s]+)\)")
PRIVATE_PATTERNS = {
    "github token": re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}"),
    "secret key": re.compile(r"\bsk-[A-Za-z0-9_-]{16,}"),
    "local user path": re.compile(r"/Users/[A-Za-z0-9._-]+|C:\\Users\\"),
    "email address": re.compile(r"\b[A-Za-z0-9._%+-]+@(?!example\.(?:com|org|net)\b)[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"),
    "phone number": re.compile(r"(?<!\d)1[3-9]\d{9}(?!\d)|\+\d{1,3}[ -]?\(?\d{2,4}\)?[ -]?\d{3,4}[ -]?\d{3,4}"),
}
ALLOWED_EMAILS = {"noreply@anthropic.com"}


def files():
    for path in sorted(ROOT.rglob("*")):
        if path.is_file() and not any(part in SKIP_DIRS for part in path.relative_to(ROOT).parts):
            yield path


def rel(path):
    return path.relative_to(ROOT).as_posix()


def parse_frontmatter(text):
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return None, text
    block, body = text[4:end], text[end + 5:]
    data, key = {}, None
    for line in block.splitlines():
        match = re.match(r"^([A-Za-z_-]+):\s*(.*)$", line)
        if match:
            key, value = match.group(1), match.group(2).strip()
            data[key] = "" if value in (">", "|", ">-", "|-") else value.strip("'\"")
        elif key and line.startswith((" ", "\t")):
            data[key] = (data[key] + " " + line.strip()).strip()
    return data, body


def check_links(path, text, errors):
    for target in LINK_RE.findall(text):
        if re.match(r"^[a-z][a-z0-9+.-]*:", target) or target.startswith("#"):
            continue
        clean = unquote(target.split("#", 1)[0])
        if clean and not (path.parent / clean).exists():
            errors.append(f"{rel(path)}: broken link -> {target}")
        elif clean and rel(path).startswith("skills/"):
            resolved = (path.parent / clean).resolve()
            if not resolved.is_relative_to(ROOT / "skills"):
                errors.append(f"{rel(path)}: link leaves skills/ and breaks after install -> {target}")


def check_skill(skill_dir, errors, warnings):
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.exists():
        errors.append(f"{rel(skill_dir)}: missing SKILL.md")
        return
    text = skill_file.read_text(encoding="utf-8")
    meta, body = parse_frontmatter(text)
    where = rel(skill_file)
    if meta is None:
        errors.append(f"{where}: missing or malformed frontmatter")
        return
    extra = set(meta) - {"name", "description"}
    if extra:
        errors.append(f"{where}: unexpected frontmatter keys {sorted(extra)}")
    name, description = meta.get("name", ""), meta.get("description", "")
    if name != skill_dir.name or not NAME_RE.match(name):
        errors.append(f"{where}: name '{name}' must equal folder name and be kebab-case")
    if not 40 <= len(description) <= 1024:
        errors.append(f"{where}: description length {len(description)} not in 40..1024")
    if "<" in description or ">" in description:
        errors.append(f"{where}: description must not contain angle brackets")
    lines = body.strip().count("\n") + 1
    if lines > HARD_LINES:
        errors.append(f"{where}: body has {lines} lines (hard limit {HARD_LINES}); move detail to references/")
    elif lines > SOFT_LINES:
        warnings.append(f"{where}: body has {lines} lines (soft budget {SOFT_LINES})")
    if skill_dir.name == HUB:
        return
    for section in REQUIRED_SECTIONS:
        if not re.search(rf"^{re.escape(section)}\b", body, re.M):
            errors.append(f"{where}: missing section '{section}'")
    if f"../{HUB}/policies/" not in body:
        errors.append(f"{where}: Gates must link at least one policy under ../{HUB}/policies/")


def load_denylist():
    path = ROOT / ".denylist.local"
    if not path.exists():
        return []
    terms = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        term, _, allowed = line.partition("@allow")
        terms.append((term.strip(), set(allowed.split())))
    return terms


def main():
    strict = "--strict" in sys.argv
    errors, warnings = [], []
    denylist = load_denylist()
    deny_res = [(t, allow, re.compile(r"(?<![A-Za-z0-9])" + re.escape(t) + r"(?![A-Za-z0-9])", re.I))
                for t, allow in denylist]
    counts = {"md": 0, "csv": 0, "skills": 0}
    for path in files():
        if path.suffix not in TEXT_SUFFIXES:
            continue
        text = path.read_text(encoding="utf-8")
        where = rel(path)
        if text and not text.endswith("\n"):
            errors.append(f"{where}: missing final newline")
        if path.suffix == ".md":
            counts["md"] += 1
            check_links(path, text, errors)
        if path.suffix == ".csv":
            counts["csv"] += 1
            rows = list(csv.reader(text.splitlines()))
            if not rows:
                errors.append(f"{where}: empty CSV")
            for number, row in enumerate(rows[1:], start=2):
                if len(row) != len(rows[0]):
                    errors.append(f"{where}:{number}: {len(row)} columns, header has {len(rows[0])}")
        if path.name != "check_repo.py":
            for label, pattern in PRIVATE_PATTERNS.items():
                for match in pattern.finditer(text):
                    if label == "email address" and match.group(0).lower() in ALLOWED_EMAILS:
                        continue
                    line = text.count("\n", 0, match.start()) + 1
                    errors.append(f"{where}:{line}: possible {label}")
        for term, allow, pattern in deny_res:
            if where in allow:
                continue
            for match in pattern.finditer(text):
                line = text.count("\n", 0, match.start()) + 1
                errors.append(f"{where}:{line}: denylisted term '{term}'")
    skills_root = ROOT / "skills"
    if skills_root.exists():
        for skill_dir in sorted(p for p in skills_root.iterdir() if p.is_dir()):
            counts["skills"] += 1
            check_skill(skill_dir, errors, warnings)
    for warning in warnings:
        print("WARN  " + warning)
    for error in errors:
        print("FAIL  " + error)
    summary = (f"{counts['skills']} skills, {counts['md']} Markdown, {counts['csv']} CSV, "
               f"denylist {'loaded (' + str(len(denylist)) + ' terms)' if denylist else 'not found'}")
    if errors or (strict and warnings):
        print(f"\nFAILED: {len(errors)} errors, {len(warnings)} warnings. {summary}")
        return 1
    print(f"PASS: {summary}, {len(warnings)} warnings")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
