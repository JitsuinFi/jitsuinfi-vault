#!/usr/bin/env python3
"""render-diagrams.py - render every PlantUML block in 08-FlowDiagrams/*.md to SVG.

Each block is a fenced ```plantuml block that starts with `@startuml <name>`; it is rendered to
08-FlowDiagrams/assets/<name>.svg, which the note embeds as ![...](assets/<name>.svg).
`!include dfd-style.iuml` / `!include seq-style.iuml` resolve to 08-FlowDiagrams/assets/.

Usage (from the vault folder): python3 scripts/render-diagrams.py [--png]
Needs `plantuml` on PATH (macOS: brew install plantuml).
"""
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

VAULT = Path(__file__).resolve().parent.parent
DIR = VAULT / "08-FlowDiagrams"
ASSETS = DIR / "assets"
BLOCK_RE = re.compile(r"```plantuml\n(.*?)```", re.DOTALL)
NAME_RE = re.compile(r"^@startuml\s+(\S+)", re.MULTILINE)


def main():
    fmt = "png" if "--png" in sys.argv else "svg"
    if not shutil.which("plantuml"):
        sys.exit("plantuml not found (macOS: brew install plantuml)")
    blocks = []
    for md in sorted(DIR.glob("*.md")):
        for src in BLOCK_RE.findall(md.read_text(encoding="utf-8")):
            m = NAME_RE.search(src)
            if not m:
                sys.exit("{}: plantuml block without '@startuml <name>'".format(md.name))
            blocks.append((md.name, m.group(1), src))
    names = [n for _, n, _ in blocks]
    dupes = {n for n in names if names.count(n) > 1}
    if dupes:
        sys.exit("duplicate diagram names: {}".format(", ".join(sorted(dupes))))
    with tempfile.TemporaryDirectory() as tmp:
        for _, name, src in blocks:
            for style in ASSETS.glob("*.iuml"):
                shutil.copy(style, tmp)
            (Path(tmp) / (name + ".puml")).write_text(src, encoding="utf-8")
        files = [str(Path(tmp) / (n + ".puml")) for n in names]
        r = subprocess.run(["plantuml", "-t" + fmt, "-failfast2", "-o", str(ASSETS)] + files,
                           capture_output=True, text=True)
        if r.returncode != 0:
            sys.exit(r.stdout + r.stderr)
    for md, name, _ in blocks:
        print("OK  {} -> assets/{}.{}".format(md, name, fmt))
    print("Rendered: {}".format(len(blocks)))


if __name__ == "__main__":
    main()
