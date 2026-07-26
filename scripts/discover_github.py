#!/usr/bin/env python3
"""Discover GitHub repository leads and write a candidate observation artifact.

This script never reads or writes data/skills.yaml. Its output is unverified input
for human curation, not a catalog update.
"""

from __future__ import annotations

import argparse
import json
import os
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

import yaml


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG = ROOT / "config" / "discovery.yaml"
DEFAULT_OUTPUT = ROOT / "build" / "discovery" / "github-observations.json"
API = "https://api.github.com/search/repositories"
USER_AGENT = "awesome-presentation-skills-discovery/0.1 (+https://github.com/cosen1024)"


def normalize_item(item: dict[str, object], query_id: str, observed_at: str) -> dict[str, object]:
    owner = item.get("owner") if isinstance(item.get("owner"), dict) else {}
    return {
        "repository_id": item.get("id"),
        "repository": item.get("full_name"),
        "repository_url": item.get("html_url"),
        "description": item.get("description"),
        "owner_type": owner.get("type"),
        "fork": bool(item.get("fork")),
        "archived": bool(item.get("archived")),
        "stars": item.get("stargazers_count"),
        "created_at": item.get("created_at"),
        "updated_at": item.get("updated_at"),
        "pushed_at": item.get("pushed_at"),
        "default_branch": item.get("default_branch"),
        "topics": item.get("topics") if isinstance(item.get("topics"), list) else [],
        "discovery_sources": [{"query_id": query_id, "observed_at": observed_at}],
    }


def deduplicate(observations: Iterable[dict[str, object]]) -> list[dict[str, object]]:
    merged: dict[object, dict[str, object]] = {}
    for observation in observations:
        key = observation.get("repository_id") or observation.get("repository")
        if key not in merged:
            merged[key] = observation
            continue
        current_sources = merged[key].setdefault("discovery_sources", [])
        new_sources = observation.get("discovery_sources", [])
        if isinstance(current_sources, list) and isinstance(new_sources, list):
            known = {json.dumps(source, sort_keys=True) for source in current_sources}
            current_sources.extend(
                source for source in new_sources if json.dumps(source, sort_keys=True) not in known
            )
    return sorted(merged.values(), key=lambda entry: str(entry.get("repository", "")).lower())


def fetch_page(query: str, page: int, per_page: int, token: str | None) -> dict[str, object]:
    url = f"{API}?{urlencode({'q': query, 'sort': 'updated', 'order': 'desc', 'per_page': per_page, 'page': page})}"
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": USER_AGENT,
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    request = Request(url, headers=headers)
    try:
        with urlopen(request, timeout=30) as response:
            return json.load(response)
    except HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"GitHub search failed ({exc.code}) for page {page}: {detail}") from exc
    except URLError as exc:
        raise RuntimeError(f"GitHub search network failure for page {page}: {exc}") from exc


def discover(config: dict[str, object], token: str | None) -> dict[str, object]:
    github = config["github"]
    assert isinstance(github, dict)
    queries = github["queries"]
    assert isinstance(queries, list)
    per_page = int(github.get("per_page", 50))
    max_pages = int(github.get("max_pages_per_query", 1))
    observed_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    observations: list[dict[str, object]] = []
    query_results: list[dict[str, object]] = []

    for query_config in queries:
        assert isinstance(query_config, dict)
        query_id = str(query_config["id"])
        query = str(query_config["query"])
        seen_for_query = 0
        total_count = 0
        for page in range(1, max_pages + 1):
            payload = fetch_page(query, page, per_page, token)
            total_count = int(payload.get("total_count", 0))
            items = payload.get("items", [])
            if not isinstance(items, list) or not items:
                break
            observations.extend(
                normalize_item(item, query_id, observed_at)
                for item in items
                if isinstance(item, dict)
            )
            seen_for_query += len(items)
            if len(items) < per_page:
                break
            time.sleep(1)
        query_results.append(
            {"id": query_id, "query": query, "reported_total": total_count, "observed": seen_for_query}
        )

    normalized = deduplicate(observations)
    return {
        "schema_version": 1,
        "observed_at": observed_at,
        "notice": "Unverified discovery leads. Human source verification is required before catalog promotion.",
        "query_results": query_results,
        "observations": normalized,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    config = yaml.safe_load(args.config.read_text(encoding="utf-8"))
    if not isinstance(config, dict) or config.get("schema_version") != 1:
        parser.error("discovery config must be a schema_version 1 mapping")
    payload = discover(config, os.environ.get("GITHUB_TOKEN"))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {len(payload['observations'])} unique repository observations to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

