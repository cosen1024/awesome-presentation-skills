#!/usr/bin/env python3
"""Render catalog sections in README.md and README_EN.md from YAML."""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "skills.yaml"
STARS_PATH = ROOT / "data" / "stars.json"
START = "<!-- CATALOG:START -->"
END = "<!-- CATALOG:END -->"
BLOCK_RE = re.compile(rf"{re.escape(START)}.*?{re.escape(END)}", re.DOTALL)

EDITABILITY_ZH = {
    "native-editable": "原生可编辑",
    "source-editable": "源文件可编辑",
    "partially-editable": "部分可编辑",
    "image-based": "图片式",
}
EDITABILITY_EN = {
    "native-editable": "Native editable",
    "source-editable": "Source editable",
    "partially-editable": "Partially editable",
    "image-based": "Image-based",
}


def cell(value: object) -> str:
    return html.escape(str(value), quote=False).replace("|", "&#124;").replace("\n", " ")


def load_stars() -> dict[str, int]:
    if not STARS_PATH.exists():
        return {}
    payload = json.loads(STARS_PATH.read_text(encoding="utf-8"))
    stars = payload.get("stars", {}) if isinstance(payload, dict) else {}
    return stars if isinstance(stars, dict) else {}


def render_catalog(
    data: dict[str, object], language: str, stars: dict[str, int] | None = None
) -> str:
    skills = data["skills"]
    assert isinstance(skills, list)
    stars = stars if stars is not None else load_stars()
    lines = [START]
    editability_labels = EDITABILITY_ZH if language == "zh" else EDITABILITY_EN
    for category in data["categories"]:
        assert isinstance(category, dict)
        category_id = category["id"]
        title = category["name_zh" if language == "zh" else "name_en"]
        description = category["description_zh" if language == "zh" else "description_en"]
        header = (
            "| 仓库 / Skill | 仓库 Stars | 适合做什么 | 输出与编辑性 |"
            if language == "zh"
            else "| Repository / Skill | Repo Stars | Best suited for | Output and editability |"
        )
        lines.extend(["", f"## {title}", "", str(description), "", header, "|---|---:|---|---|"])
        category_skills = sorted(
            (
                item
                for item in skills
                if isinstance(item, dict) and item["category"] == category_id
            ),
            key=lambda item: str(item["repository"]).casefold(),
        )
        for item in category_skills:
            assert isinstance(item, dict)
            purpose = item["purpose_zh" if language == "zh" else "purpose_en"]
            outputs = ", ".join(str(value).upper() for value in item["outputs"])
            editability = editability_labels[str(item["editability"])]
            repository = str(item["repository"])
            star_value = stars.get(repository)
            star_text = f"[{star_value:,}]({item['repository_url']}/stargazers)" if isinstance(star_value, int) else "—"
            row = (
                f"| [{cell(item['repository'])}]({item['repository_url']})"
                f"<br>[{cell(item['skill'])}]({item['source_url']}) "
                f"| {star_text} | {cell(purpose)} | {cell(outputs)}<br>{cell(editability)} |"
            )
            lines.append(row)
    lines.extend(["", END])
    return "\n".join(lines)


def update_readme(path: Path, catalog: str, write: bool) -> bool:
    content = path.read_text(encoding="utf-8")
    if len(BLOCK_RE.findall(content)) != 1:
        raise ValueError(f"exactly one catalog marker block required in {path}")
    rendered = BLOCK_RE.sub(catalog, content)
    if rendered == content:
        print(f"OK: {path.name} is up to date")
        return True
    if write:
        path.write_text(rendered, encoding="utf-8")
        print(f"UPDATED: {path.name}")
        return True
    print(f"STALE: {path.name}; run scripts/render_readmes.py --write", file=sys.stderr)
    return False


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--write", action="store_true")
    args = parser.parse_args()
    data = yaml.safe_load(DATA_PATH.read_text(encoding="utf-8"))
    targets = ((ROOT / "README.md", "zh"), (ROOT / "README_EN.md", "en"))
    results = [
        update_readme(path, render_catalog(data, language), args.write)
        for path, language in targets
    ]
    return 0 if all(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
