import argparse
import json
import sys
from pathlib import Path
from .core import WORKFLOWS, analyze, render
from .profile import DEFAULT_PROFILE, load_profile


def main():
    parser = argparse.ArgumentParser(description="Local, deterministic checks for B2B marketing drafts")
    parser.add_argument("workflow", choices=WORKFLOWS)
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--profile", type=Path, default=DEFAULT_PROFILE,
                        help="company profile (.toml or .json); defaults to the kit's DemoCo example")
    parser.add_argument("--as-of", required=True, help="YYYY-MM-DD; explicit for reproducible freshness checks")
    parser.add_argument("--lang", choices=("en", "zh"), default="en")
    parser.add_argument("--output", type=Path, help="Create a NEW output directory; never overwrite existing output")
    args = parser.parse_args()
    try:
        result = analyze(args.workflow, json.loads(args.input.read_text()), load_profile(args.profile), args.as_of)
        if args.output:
            args.output.mkdir(parents=True, exist_ok=False)
            (args.output / "result.json").write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n")
            (args.output / "brief.md").write_text(render(result, args.lang))
            print(str(args.output / "brief.md"))
        else:
            print(render(result, args.lang))
        return 0
    except (ValueError, OSError, TypeError, KeyError) as exc:
        print("Input/output error: " + str(exc), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
