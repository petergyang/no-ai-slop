#!/usr/bin/env python3
"""Build and validate the distributable No AI Slop plugin archive."""

from __future__ import annotations

import argparse
import json
import shutil
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / ".codex-plugin" / "plugin.json"
DIST = ROOT / "dist"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Validate without keeping build output")
    return parser.parse_args()


def validate_source(manifest: dict) -> None:
    required = ("name", "version", "description", "author", "skills", "interface")
    missing = [key for key in required if not manifest.get(key)]
    if missing:
        raise SystemExit(f"Missing manifest fields: {', '.join(missing)}")

    interface = manifest["interface"]
    interface_required = (
        "displayName",
        "shortDescription",
        "longDescription",
        "developerName",
        "category",
        "capabilities",
        "defaultPrompt",
    )
    missing_interface = [key for key in interface_required if not interface.get(key)]
    if missing_interface:
        raise SystemExit(f"Missing interface fields: {', '.join(missing_interface)}")

    prompts = interface["defaultPrompt"]
    if len(prompts) > 3 or any(len(prompt) > 128 for prompt in prompts):
        raise SystemExit("Starter prompts must contain at most three entries of 128 characters or fewer")

    for source in (ROOT / "SKILL.md", ROOT / "eval.md", ROOT / "assets" / "no-ai-slop.svg"):
        if not source.is_file():
            raise SystemExit(f"Missing package source: {source.relative_to(ROOT)}")


def build_plugin(manifest: dict) -> tuple[Path, Path]:
    plugin_root = DIST / "no-ai-slop"
    if plugin_root.exists():
        shutil.rmtree(plugin_root)

    skill_root = plugin_root / "skills" / "no-ai-slop"
    (plugin_root / ".codex-plugin").mkdir(parents=True)
    (plugin_root / "assets").mkdir(parents=True)
    skill_root.mkdir(parents=True)

    shutil.copy2(MANIFEST, plugin_root / ".codex-plugin" / "plugin.json")
    shutil.copy2(ROOT / "SKILL.md", skill_root / "SKILL.md")
    shutil.copy2(ROOT / "eval.md", skill_root / "eval.md")
    shutil.copy2(ROOT / "assets" / "no-ai-slop.svg", plugin_root / "assets" / "no-ai-slop.svg")
    shutil.copy2(ROOT / "LICENSE", plugin_root / "LICENSE")
    shutil.copy2(ROOT / "PRIVACY.md", plugin_root / "PRIVACY.md")
    shutil.copy2(ROOT / "TERMS.md", plugin_root / "TERMS.md")

    archive = DIST / f"no-ai-slop-plugin-{manifest['version']}.zip"
    if archive.exists():
        archive.unlink()
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as output:
        for path in sorted(plugin_root.rglob("*")):
            if path.is_file():
                output.write(path, path.relative_to(DIST))
    return plugin_root, archive


def validate_build(plugin_root: Path, archive: Path) -> None:
    expected = {
        ".codex-plugin/plugin.json",
        "assets/no-ai-slop.svg",
        "skills/no-ai-slop/SKILL.md",
        "skills/no-ai-slop/eval.md",
        "LICENSE",
        "PRIVACY.md",
        "TERMS.md",
    }
    actual = {
        str(path.relative_to(plugin_root))
        for path in plugin_root.rglob("*")
        if path.is_file()
    }
    if expected != actual:
        raise SystemExit(f"Unexpected package files: expected {sorted(expected)}, found {sorted(actual)}")

    packaged_skill = plugin_root / "skills" / "no-ai-slop" / "SKILL.md"
    packaged_eval = plugin_root / "skills" / "no-ai-slop" / "eval.md"
    if packaged_skill.read_bytes() != (ROOT / "SKILL.md").read_bytes():
        raise SystemExit("Packaged SKILL.md does not match the canonical file")
    if packaged_eval.read_bytes() != (ROOT / "eval.md").read_bytes():
        raise SystemExit("Packaged eval.md does not match the canonical file")
    if not zipfile.is_zipfile(archive):
        raise SystemExit("Plugin archive is not a valid ZIP file")


def main() -> None:
    args = parse_args()
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    validate_source(manifest)
    plugin_root, archive = build_plugin(manifest)
    validate_build(plugin_root, archive)
    print(f"Built {archive.relative_to(ROOT)}")
    if args.check:
        shutil.rmtree(DIST)


if __name__ == "__main__":
    main()
