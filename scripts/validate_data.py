#!/usr/bin/env python3
"""Validate catalog, candidate, and related-tool data."""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from datetime import date, datetime
from pathlib import Path
from urllib.parse import unquote, urlparse

import yaml


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DATA = ROOT / "data" / "skills.yaml"
DEFAULT_STARS = ROOT / "data" / "stars.json"
REQUIRED_CATEGORIES = {"editable-pptx", "html-slides", "image-first"}
EDITABILITY = {"native-editable", "source-editable", "partially-editable", "image-based"}
VERIFICATION = {"source-verified"}
RUNTIME = {"not-tested", "tested"}
SECURITY = {"not-reviewed", "reviewed"}
SHA_RE = re.compile(r"^[0-9a-f]{40}$")
ID_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def iso_date(value: object) -> str | None:
    if isinstance(value, date):
        return value.isoformat()
    if isinstance(value, str):
        try:
            return date.fromisoformat(value).isoformat()
        except ValueError:
            return None
    return None


def is_https_github(value: object) -> bool:
    if not isinstance(value, str):
        return False
    parsed = urlparse(value)
    return parsed.scheme == "https" and parsed.netloc.lower() == "github.com"


def non_empty_string(item: dict[str, object], field: str, prefix: str, errors: list[str]) -> None:
    if not isinstance(item.get(field), str) or not str(item[field]).strip():
        errors.append(f"{prefix}.{field} must be a non-empty string")


def string_list(item: dict[str, object], field: str, prefix: str, errors: list[str]) -> None:
    value = item.get(field)
    if not isinstance(value, list) or not value or not all(
        isinstance(entry, str) and entry.strip() for entry in value
    ):
        errors.append(f"{prefix}.{field} must be a non-empty string list")


def load_yaml(path: Path) -> tuple[object, list[str]]:
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8")), []
    except (OSError, yaml.YAMLError) as exc:
        return None, [f"cannot load {path}: {exc}"]


def validate_catalog(path: Path) -> list[str]:
    data, errors = load_yaml(path)
    if errors:
        return errors
    if not isinstance(data, dict):
        return ["catalog root must be a mapping"]
    if data.get("schema_version") != 1:
        errors.append("schema_version must be 1")

    catalog_date = iso_date(data.get("last_verified"))
    if not catalog_date:
        errors.append("last_verified must be an ISO date")

    categories = data.get("categories")
    if not isinstance(categories, list):
        return errors + ["categories must be a list"]
    category_ids = [entry.get("id") for entry in categories if isinstance(entry, dict)]
    if len(category_ids) != len(set(category_ids)):
        errors.append("category ids must be unique")
    if set(category_ids) != REQUIRED_CATEGORIES:
        errors.append(
            "category set mismatch; "
            f"missing={sorted(REQUIRED_CATEGORIES - set(category_ids))}, "
            f"extra={sorted(set(category_ids) - REQUIRED_CATEGORIES)}"
        )
    for index, category in enumerate(categories):
        prefix = f"categories[{index}]"
        if not isinstance(category, dict):
            errors.append(f"{prefix} must be a mapping")
            continue
        for field in ("id", "name_zh", "name_en", "description_zh", "description_en"):
            non_empty_string(category, field, prefix, errors)

    skills = data.get("skills")
    if not isinstance(skills, list):
        return errors + ["skills must be a list"]
    if len(skills) < 12:
        errors.append(f"catalog must contain at least 12 verified skills, got {len(skills)}")

    seen_ids: set[str] = set()
    seen_entries: set[tuple[str, str]] = set()
    counts: Counter[str] = Counter()
    required_strings = (
        "id", "category", "repository", "repository_url", "license",
        "source_ref", "skill", "skill_path", "source_url", "install_url",
        "purpose_zh", "purpose_en", "editability", "verification_status",
        "runtime_status", "security_status",
    )

    for index, item in enumerate(skills):
        prefix = f"skills[{index}]"
        if not isinstance(item, dict):
            errors.append(f"{prefix} must be a mapping")
            continue
        for field in required_strings:
            non_empty_string(item, field, prefix, errors)
        for field in ("platforms", "outputs", "capabilities"):
            string_list(item, field, prefix, errors)

        skill_id = item.get("id")
        if isinstance(skill_id, str):
            if not ID_RE.fullmatch(skill_id):
                errors.append(f"{prefix}.id must use lowercase kebab-case")
            if skill_id in seen_ids:
                errors.append(f"duplicate skill id: {skill_id}")
            seen_ids.add(skill_id)

        category = item.get("category")
        if category not in REQUIRED_CATEGORIES:
            errors.append(f"{prefix}.category is unknown: {category!r}")
        elif isinstance(category, str):
            counts[category] += 1

        if item.get("editability") not in EDITABILITY:
            errors.append(f"{prefix}.editability is invalid: {item.get('editability')!r}")
        if item.get("verification_status") not in VERIFICATION:
            errors.append(f"{prefix}.verification_status must be source-verified")
        if item.get("runtime_status") not in RUNTIME:
            errors.append(f"{prefix}.runtime_status is invalid")
        if item.get("security_status") not in SECURITY:
            errors.append(f"{prefix}.security_status is invalid")

        for field in ("repository_url", "source_url", "install_url"):
            if not is_https_github(item.get(field)):
                errors.append(f"{prefix}.{field} must be an https://github.com URL")

        source_ref = item.get("source_ref")
        if not isinstance(source_ref, str) or not SHA_RE.fullmatch(source_ref):
            errors.append(f"{prefix}.source_ref must be a full 40-character commit SHA")
        else:
            for field in ("source_url", "install_url"):
                if source_ref not in str(item.get(field, "")):
                    errors.append(f"{prefix}.{field} must be pinned to source_ref")

        skill_path = item.get("skill_path")
        if isinstance(skill_path, str):
            if not skill_path.endswith("SKILL.md"):
                errors.append(f"{prefix}.skill_path must point to SKILL.md")
            if skill_path not in unquote(str(item.get("source_url", ""))):
                errors.append(f"{prefix}.source_url must contain skill_path")

        verified_at = iso_date(item.get("verified_at"))
        if not verified_at:
            errors.append(f"{prefix}.verified_at must be an ISO date")
        elif catalog_date and verified_at > catalog_date:
            errors.append(f"{prefix}.verified_at must not be after last_verified")

        if item.get("license") == "NOASSERTION":
            if not item.get("notes_zh") or not item.get("notes_en"):
                errors.append(f"{prefix} with NOASSERTION license needs bilingual notes")

        entry_key = (str(item.get("repository")), str(item.get("skill_path")))
        if entry_key in seen_entries:
            errors.append(f"duplicate repository/skill_path pair: {entry_key}")
        seen_entries.add(entry_key)

    uncovered = sorted(REQUIRED_CATEGORIES - set(counts))
    if uncovered:
        errors.append(f"categories without entries: {uncovered}")
    return errors


def validate_supplement(path: Path, list_field: str) -> list[str]:
    data, errors = load_yaml(path)
    if errors:
        return errors
    if not isinstance(data, dict):
        return [f"{path.name} root must be a mapping"]
    if data.get("schema_version") != 1:
        errors.append(f"{path.name}: schema_version must be 1")
    entries = data.get(list_field)
    if not isinstance(entries, list):
        return errors + [f"{path.name}: {list_field} must be a list"]
    seen: set[str] = set()
    for index, entry in enumerate(entries):
        prefix = f"{path.name}:{list_field}[{index}]"
        if not isinstance(entry, dict):
            errors.append(f"{prefix} must be a mapping")
            continue
        non_empty_string(entry, "id", prefix, errors)
        entry_id = entry.get("id")
        if isinstance(entry_id, str):
            if not ID_RE.fullmatch(entry_id):
                errors.append(f"{prefix}.id must use lowercase kebab-case")
            if entry_id in seen:
                errors.append(f"{prefix}.id is duplicated")
            seen.add(entry_id)
    return errors


def validate_stars(catalog_path: Path = DEFAULT_DATA, stars_path: Path = DEFAULT_STARS) -> list[str]:
    errors: list[str] = []
    try:
        catalog = yaml.safe_load(catalog_path.read_text(encoding="utf-8"))
        payload = json.loads(stars_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError, yaml.YAMLError) as exc:
        return [f"cannot load Stars cache: {exc}"]
    if not isinstance(payload, dict):
        return ["Stars cache root must be a mapping"]
    if payload.get("schema_version") != 1:
        errors.append("Stars cache schema_version must be 1")
    if payload.get("source") != "github-rest-api":
        errors.append("Stars cache source must be github-rest-api")
    updated_at = payload.get("updated_at")
    try:
        datetime.fromisoformat(str(updated_at).replace("Z", "+00:00"))
    except ValueError:
        errors.append("Stars cache updated_at must be an ISO timestamp")
    stars = payload.get("stars")
    if not isinstance(stars, dict):
        return errors + ["Stars cache stars must be a mapping"]
    repositories = {str(item["repository"]) for item in catalog["skills"]}
    cached = set(stars)
    if repositories != cached:
        errors.append(
            "Stars cache repository mismatch; "
            f"missing={sorted(repositories - cached)}, extra={sorted(cached - repositories)}"
        )
    for repository, value in stars.items():
        if not isinstance(value, int) or value < 0:
            errors.append(f"Stars cache value for {repository} must be a non-negative integer")
    return errors


def validate_all(catalog_path: Path = DEFAULT_DATA) -> list[str]:
    errors = validate_catalog(catalog_path)
    errors.extend(validate_stars(catalog_path))
    errors.extend(validate_supplement(ROOT / "data" / "candidates.yaml", "candidates"))
    errors.extend(validate_supplement(ROOT / "data" / "related-tools.yaml", "tools"))
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", type=Path, default=DEFAULT_DATA)
    args = parser.parse_args()
    errors = validate_all(args.path)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(f"Validation failed with {len(errors)} error(s).", file=sys.stderr)
        return 1
    data = yaml.safe_load(args.path.read_text(encoding="utf-8"))
    print(
        f"OK: {len(data['skills'])} verified skills across "
        f"{len(data['categories'])} categories ({data['last_verified']})."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
