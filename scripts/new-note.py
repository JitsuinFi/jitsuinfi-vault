#!/usr/bin/env python3
"""new-note.py - generate a concept note into Concepts/ (or another folder).

Port of ObsidianGuides/_assets/scripts/new-note.ps1.
Usage:
    python3 scripts/new-note.py --title "Nullifier" --source "Arsitektur JitsuinFi" --module 07
    python3 scripts/new-note.py --title "MEV" --related "Viewing Key" "Attestor"
"""
import argparse
import importlib.util
import re
import sys
from pathlib import Path

VAULT = Path(__file__).resolve().parent.parent


def load_check_links():
    spec = importlib.util.spec_from_file_location(
        "check_links", str(Path(__file__).resolve().parent / "check-links.py")
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--title", required=True)
    ap.add_argument("--source")
    ap.add_argument("--module", help='module number, e.g. "07"')
    ap.add_argument("--related", nargs="*", default=[])
    ap.add_argument("--folder", default="Concepts")
    a = ap.parse_args()

    safe = re.sub(r'[<>:"/\\|?*]', "", a.title).strip()
    if not safe:
        print("ERROR: Title kosong setelah sanitasi.")
        return 1

    folder = VAULT / a.folder
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / (safe + ".md")
    if path.exists():
        print("SKIP: sudah ada -> {}/{}.md".format(a.folder, safe))
        return 0

    module_link = None
    if a.module:
        guides = sorted((VAULT / "Module-Guides").glob(a.module + " *.md"))
        if guides:
            module_link = guides[0].stem

    refs = []
    if a.source:
        refs.append("[[{}]]".format(a.source))
    if module_link:
        refs.append("[[{}]]".format(module_link))
    related = [r.strip() for item in a.related for r in item.split(",") if r.strip()]

    lines = [
        "---",
        "tags: [concept]",
        "---",
        "",
        "# {}".format(a.title),
        "",
        "**Definisi:** _TODO 1-2 kalimat._",
        "",
        "**Detail:** _TODO penjelasan._",
        "",
        "**Referensi:** " + (", ".join(refs) if refs else "_TODO_"),
        "",
        "**Related:** " + (", ".join("[[{}]]".format(r) for r in related) if related else "_TODO_"),
        "",
    ]
    path.write_text("\n".join(lines), encoding="utf-8")
    print("OK  dibuat: {}/{}.md".format(a.folder, safe))

    _, n_broken = load_check_links().check(verbose=False)
    if n_broken == 0:
        print("OK  semua link valid.")
    else:
        print("WARN cek link: ada link belum resolve (jalankan check-links.py).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
