#!/usr/bin/env python3
"""check-links.py - verify all [[wikilinks]] in the vault resolve to real .md files.

Port of ObsidianGuides/_assets/scripts/check-links.ps1 for macOS/Linux (no PowerShell needed).
Run from anywhere:
    python3 scripts/check-links.py
Ignores links inside code fences (```) and inline code (`...`) - those are examples, not real links.
Exit code 1 when any link is broken.
"""
import os
import re
import sys
from pathlib import Path

VAULT = Path(__file__).resolve().parent.parent

FENCE_RE = re.compile(r"```.*?```", re.DOTALL)
INLINE_RE = re.compile(r"`[^`]*`")
LINK_RE = re.compile(r"\[\[([^\]]+)\]\]")


def collect_md_files():
    files = []
    for root, dirs, names in os.walk(VAULT):
        dirs[:] = [d for d in dirs if d != ".obsidian"]
        for name in names:
            if name.endswith(".md"):
                files.append(Path(root) / name)
    return sorted(files)


def build_maps(files):
    basemap = {}
    pathmap = set()
    for f in files:
        rel = f.relative_to(VAULT).as_posix()
        pathmap.add(rel)
        basemap.setdefault(f.stem, []).append(rel)
    return basemap, pathmap


def resolve(target, basemap, pathmap):
    if target.endswith(".md"):
        target = target[:-3]
    if "/" in target:
        return (target + ".md") in pathmap
    return target in basemap


def check(verbose=True):
    files = collect_md_files()
    basemap, pathmap = build_maps(files)
    checked = 0
    broken = []
    for f in files:
        text = f.read_text(encoding="utf-8-sig")
        text = FENCE_RE.sub("", text)
        text = INLINE_RE.sub("", text)
        for m in LINK_RE.finditer(text):
            raw = m.group(1)
            target = raw.split("|")[0].split("#")[0].strip()
            # inside markdown tables the alias pipe is escaped as "\|"
            target = target.rstrip("\\").strip()
            if not target:
                continue
            checked += 1
            if not resolve(target, basemap, pathmap):
                broken.append((f.relative_to(VAULT).as_posix(), raw))
    if verbose:
        for src, raw in broken:
            print("BROKEN: {} -> [[{}]]".format(src, raw))
        print("")
        print("Links checked: {} | Broken: {}".format(checked, len(broken)))
    return checked, len(broken)


if __name__ == "__main__":
    _, n_broken = check()
    sys.exit(1 if n_broken else 0)
