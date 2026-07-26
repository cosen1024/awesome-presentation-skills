#!/usr/bin/env python3
"""Refresh the generated GitHub Stars cache for verified repositories."""

from __future__ import annotations

import json
import os
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable

import yaml


ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT / "data" / "skills.yaml"
STARS_PATH = ROOT / "data" / "stars.json"
MAX_RETRIES = 2


def catalog_repositories() -> list[str]:
    data = yaml.safe_load(CATALOG_PATH.read_text(encoding="utf-8"))
    return sorted({str(item["repository"]) for item in data["skills"]})


def github_stars(repository: str) -> int:
    request = urllib.request.Request(
        f"https://api.github.com/repos/{repository}",
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "awesome-presentation-skills-stars/0.1",
            "X-GitHub-Api-Version": "2022-11-28",
        },
    )
    token = os.getenv("GITHUB_TOKEN")
    if token:
        request.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(request, timeout=20) as response:
        payload = json.load(response)
    value = payload.get("stargazers_count")
    if not isinstance(value, int) or value < 0:
        raise ValueError(f"{repository}: stargazers_count is missing or invalid")
    return value


def fetch_with_retry(repository: str) -> int:
    last_error: Exception | None = None
    for attempt in range(MAX_RETRIES + 1):
        try:
            return github_stars(repository)
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, ValueError) as exc:
            last_error = exc
            if attempt < MAX_RETRIES:
                time.sleep(2 * (attempt + 1))
    raise RuntimeError(f"{repository}: {last_error}")


def refresh(
    repositories: list[str],
    previous: dict[str, object],
    fetcher: Callable[[str], int],
    now: str,
) -> tuple[dict[str, object], bool, dict[str, str]]:
    previous_stars = previous.get("stars", {}) if isinstance(previous, dict) else {}
    if not isinstance(previous_stars, dict):
        previous_stars = {}
    stars: dict[str, int] = {}
    failures: dict[str, str] = {}
    for repository in repositories:
        try:
            stars[repository] = fetcher(repository)
        except RuntimeError as exc:
            old_value = previous_stars.get(repository)
            if isinstance(old_value, int) and old_value >= 0:
                stars[repository] = old_value
            failures[repository] = str(exc)

    if stars == previous_stars and previous.get("schema_version") == 1:
        return previous, False, failures
    payload: dict[str, object] = {
        "schema_version": 1,
        "updated_at": now,
        "source": "github-rest-api",
        "stars": dict(sorted(stars.items())),
    }
    return payload, True, failures


def main() -> int:
    previous: dict[str, object] = {}
    if STARS_PATH.exists():
        previous = json.loads(STARS_PATH.read_text(encoding="utf-8"))
    now = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    repositories = catalog_repositories()
    payload, changed, failures = refresh(repositories, previous, fetch_with_retry, now)
    missing = sorted(set(repositories) - set(payload.get("stars", {})))
    if missing:
        print(f"ERROR: no Stars value for: {', '.join(missing)}", file=sys.stderr)
        return 1
    if changed:
        STARS_PATH.write_text(
            json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        print(f"Updated Stars cache for {len(repositories)} repositories.")
    else:
        print(f"No Stars changes across {len(repositories)} repositories.")
    for repository, error in failures.items():
        print(f"WARNING: kept cached value for {repository}: {error}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
