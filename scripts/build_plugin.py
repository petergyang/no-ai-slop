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
SKILLS_DIR = ROOT / "skills"
STATIC_FILES = ("LICENSE", "PRIVACY.md", "TERMS.md")


def skill_dirs() -> list[Path]:
    """Every skill the manifest's ./skills/ directory advertises."""
    found = sorted(d for d in SKILLS_DIR.iterdir()
                   if d.is_dir() and (d / "SKILL.md").is_file())
    if not found:
        raise SystemExit(f"No skills with a SKILL.md under {SKILLS_DIR.relative_to(ROOT)}")
    return found


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

    sources = [ROOT / "assets" / "no-ai-slop.png"]
    for skill in skill_dirs():
        sources += [skill / "SKILL.md", skill / "eval.md"]
    for source in sources:
        if not source.is_file():
            raise SystemExit(f"Missing package source: {source.relative_to(ROOT)}")


def build_plugin(manifest: dict) -> tuple[Path, Path]:
    plugin_root = DIST / "no-ai-slop"
    if plugin_root.exists():
        shutil.rmtree(plugin_root)

    (plugin_root / ".codex-plugin").mkdir(parents=True)
    (plugin_root / "assets").mkdir(parents=True)

    shutil.copy2(MANIFEST, plugin_root / ".codex-plugin" / "plugin.json")
    for skill in skill_dirs():
        dest = plugin_root / "skills" / skill.name
        dest.mkdir(parents=True)
        shutil.copy2(skill / "SKILL.md", dest / "SKILL.md")
        shutil.copy2(skill / "eval.md", dest / "eval.md")
    shutil.copy2(ROOT / "assets" / "no-ai-slop.png", plugin_root / "assets" / "no-ai-slop.png")
    for name in STATIC_FILES:
        shutil.copy2(ROOT / name, plugin_root / name)

    archive = DIST / f"no-ai-slop-plugin-{manifest['version']}.zip"
    if archive.exists():
        archive.unlink()
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as output:
        for path in sorted(plugin_root.rglob("*")):
            if path.is_file():
                output.write(path, path.relative_to(DIST))
    return plugin_root, archive


def validate_build(plugin_root: Path, archive: Path) -> None:
    expected = {".codex-plugin/plugin.json", "assets/no-ai-slop.png", *STATIC_FILES}
    for skill in skill_dirs():
        expected |= {f"skills/{skill.name}/SKILL.md", f"skills/{skill.name}/eval.md"}
    actual = {
        str(path.relative_to(plugin_root))
        for path in plugin_root.rglob("*")
        if path.is_file()
    }
    if expected != actual:
        raise SystemExit(f"Unexpected package files: expected {sorted(expected)}, found {sorted(actual)}")

    for skill in skill_dirs():
        for name in ("SKILL.md", "eval.md"):
            packaged = plugin_root / "skills" / skill.name / name
            if packaged.read_bytes() != (skill / name).read_bytes():
                raise SystemExit(
                    f"Packaged skills/{skill.name}/{name} does not match the canonical file")
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
        shutil.rmtree(plugin_root)
        archive.unlink()
        try:
            DIST.rmdir()
        except OSError:
            pass


if __name__ == "__main__":
    main()
