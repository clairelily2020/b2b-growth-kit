"""Load a company profile. TOML profiles (the kit's format) are mapped to the four fields
the harness checks; flat JSON profiles with those fields are accepted as they are."""
import json
import tomllib
from pathlib import Path

FIELDS = ("company", "icp", "offer", "cta_url")
DEFAULT_PROFILE = Path(__file__).resolve().parents[2] / "skills" / "b2b-growth-kit" / "profile" / "example-company.toml"


def load_profile(path=None):
    path = Path(path) if path else DEFAULT_PROFILE
    if path.suffix == ".toml":
        with path.open("rb") as handle:
            data = tomllib.load(handle)
        return {
            "company": data.get("company", {}).get("name"),
            "icp": data.get("icp", {}).get("summary"),
            "offer": data.get("offer", {}).get("primary"),
            "cta_url": data.get("offer", {}).get("cta_url"),
        }
    data = json.loads(path.read_text(encoding="utf-8"))
    return {key: data.get(key) for key in FIELDS}
