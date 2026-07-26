from __future__ import annotations

import copy
import importlib.util
import sys
import unittest
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


validate_data = load_module("validate_data", ROOT / "scripts" / "validate_data.py")
render_readmes = load_module("render_readmes", ROOT / "scripts" / "render_readmes.py")
discover_github = load_module("discover_github", ROOT / "scripts" / "discover_github.py")
update_stars = load_module("update_stars", ROOT / "scripts" / "update_stars.py")


class CatalogTests(unittest.TestCase):
    def test_repository_catalog_is_valid(self):
        self.assertEqual(validate_data.validate_all(), [])

    def test_all_three_categories_render_in_both_languages(self):
        data = yaml.safe_load((ROOT / "data" / "skills.yaml").read_text(encoding="utf-8"))
        stars = {item["repository"]: 1234 for item in data["skills"]}
        zh = render_readmes.render_catalog(data, "zh", stars)
        en = render_readmes.render_catalog(data, "en", stars)
        for category in data["categories"]:
            self.assertIn(category["name_zh"], zh)
            self.assertIn(category["name_en"], en)
        self.assertIn("仓库 Stars", zh)
        self.assertIn("Repo Stars", en)
        self.assertIn("1,234", zh)

    def test_catalog_entries_are_sorted_by_repository(self):
        data = yaml.safe_load((ROOT / "data" / "skills.yaml").read_text(encoding="utf-8"))
        rendered = render_readmes.render_catalog(data, "en", {})
        for category in data["categories"]:
            repositories = sorted(
                (
                    item["repository"]
                    for item in data["skills"]
                    if item["category"] == category["id"]
                ),
                key=str.casefold,
            )
            positions = [rendered.index(f"[{repository}]") for repository in repositories]
            self.assertEqual(positions, sorted(positions))

    def test_stars_refresh_is_stable_when_counts_do_not_change(self):
        previous = {
            "schema_version": 1,
            "updated_at": "2026-01-01T00:00:00Z",
            "source": "github-rest-api",
            "stars": {"owner/repo": 7},
        }
        payload, changed, failures = update_stars.refresh(
            ["owner/repo"], previous, lambda _: 7, "2026-07-26T00:00:00Z"
        )
        self.assertFalse(changed)
        self.assertEqual(payload, previous)
        self.assertEqual(failures, {})

    def test_stars_refresh_keeps_cached_value_on_network_failure(self):
        previous = {
            "schema_version": 1,
            "updated_at": "2026-01-01T00:00:00Z",
            "source": "github-rest-api",
            "stars": {"owner/repo": 7},
        }

        def fail(_: str) -> int:
            raise RuntimeError("network unavailable")

        payload, changed, failures = update_stars.refresh(
            ["owner/repo"], previous, fail, "2026-07-26T00:00:00Z"
        )
        self.assertFalse(changed)
        self.assertEqual(payload["stars"]["owner/repo"], 7)
        self.assertIn("owner/repo", failures)

    def test_discovery_deduplicates_and_preserves_sources(self):
        first = {
            "repository_id": 1,
            "repository": "owner/repo",
            "discovery_sources": [{"query_id": "a", "observed_at": "now"}],
        }
        second = copy.deepcopy(first)
        second["discovery_sources"] = [{"query_id": "b", "observed_at": "now"}]
        result = discover_github.deduplicate([first, second])
        self.assertEqual(len(result), 1)
        self.assertEqual(len(result[0]["discovery_sources"]), 2)

    def test_normalized_observation_is_marked_as_a_lead_not_a_skill(self):
        item = {
            "id": 7,
            "full_name": "owner/repo",
            "html_url": "https://github.com/owner/repo",
            "owner": {"type": "User"},
            "stargazers_count": 3,
            "topics": ["pptx"],
        }
        result = discover_github.normalize_item(item, "query", "now")
        self.assertEqual(result["repository_id"], 7)
        self.assertNotIn("verification_status", result)
        self.assertNotIn("skill_path", result)


if __name__ == "__main__":
    unittest.main()
