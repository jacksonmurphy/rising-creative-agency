#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
INDEX_PATH = ROOT / "index.html"
DATA_PATH = ROOT / "content" / "music-releases.json"
START_MARKER = "    <!-- MUSIC SECTION:START -->"
END_MARKER = "    <!-- MUSIC SECTION:END -->"


def indent(text: str, spaces: int) -> str:
    prefix = " " * spaces
    return "\n".join(prefix + line if line else line for line in text.splitlines())


def render_card(item: dict[str, Any]) -> str:
    classes = "media-card featured-release" if item.get("featured") else "media-card"
    badge = f'\n      <span class="series-badge">{item["badge"]}</span>' if item.get("badge") else ""
    return (
        f'<article class="{classes}">{badge}\n'
        f'      <img src="{item["image"]}" alt="{item["alt"]}" class="cover" />\n'
        f'      <h3>{item["title"]}</h3>\n'
        f'      <p>{item["description"]}</p>\n'
        '      <div class="button-row">\n'
        f'        <a class="btn btn-block" target="_blank" rel="noopener noreferrer" href="{item["apple_url"]}">Apple Music</a>\n'
        f'        <a class="btn btn-ghost btn-block" target="_blank" rel="noopener noreferrer" href="{item["spotify_url"]}">Spotify</a>\n'
        '      </div>\n'
        '    </article>'
    )


def build_music_section(data: dict[str, Any]) -> str:
    new_cards = "\n        ".join(render_card(item) for item in data["new_releases"])
    catalog_cards = "\n          ".join(render_card(item) for item in data["catalog"])
    return (
        '<section id="music" class="section container">\n'
        '      <p class="eyebrow">Music</p>\n'
        '      <h2>New Releases</h2>\n'
        '      <p class="lead section-lead">\n'
        f'        {data["new_releases_intro"]}\n'
        '      </p>\n'
        '      <div class="catalog-grid new-release-grid">\n'
        f'        {new_cards}\n'
        '      </div>\n\n'
        '      <div class="series-group">\n'
        f'        <h3 class="series-heading">{data["catalog_heading"]}</h3>\n'
        '        <div class="catalog-grid">\n'
        f'          {catalog_cards}\n'
        '        </div>\n'
        '      </div>\n'
        '    </section>'
    )


def main() -> None:
    data = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    html = INDEX_PATH.read_text(encoding="utf-8")
    start = html.index(START_MARKER) + len(START_MARKER)
    end = html.index(END_MARKER)
    section = "\n" + indent(build_music_section(data), 4) + "\n"
    updated = html[:start] + section + html[end:]
    INDEX_PATH.write_text(updated, encoding="utf-8")


if __name__ == "__main__":
    main()
