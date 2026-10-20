#!/usr/bin/env python3
"""check-backlogs.py - audit queue for the per-diagram backlogs (08-FlowDiagrams/*-backlogs.md).

Workflow step 6 (Workflow Development): when every backlog task a BL row points to is DONE,
the BL row must be audited against its diagram and labelled SELESAI or GAGAL AUDIT.

This script reads the task statuses in 03-Backlog/Backlog.md and the Status column of every
BL row, then reports:
  - AUDIT QUEUE  : all tasks DONE, BL row not yet SELESAI / GAGAL AUDIT / DITUNDA
  - MISMATCH     : BL row SELESAI while one of its tasks is not DONE
  - UNKNOWN TASK : BL row points to a task ID that is not in the Backlog
  - BAD STATUS   : Status value outside the allowed labels
It also rewrites the `progress:` line in each file's frontmatter (SELESAI / total).

Usage (from the vault folder): python3 scripts/check-backlogs.py [--strict]
--strict exits 1 when anything is reported (for a pre-push check). sync-vault.py runs it
without --strict, so the queue is shown on every sync.
"""
import re
import sys
from pathlib import Path

VAULT = Path(__file__).resolve().parent.parent
BACKLOG = VAULT / "03-Backlog" / "Backlog.md"
DIAGRAMS = VAULT / "08-FlowDiagrams"
LABELS = ("TODO", "DIKERJAKAN", "AUDIT", "SELESAI", "GAGAL AUDIT", "DITUNDA", "ATURAN")
TASK_RE = re.compile(r"^\| (HNK-\d+\.T\d+) \|.*\| ([^|]*) \|$", re.M)
ROW_RE = re.compile(r"^\| (BL-[A-Z0-9]+-\d+) \|(.*)\|$", re.M)


def task_status():
    out = {}
    for tid, status in TASK_RE.findall(BACKLOG.read_text(encoding="utf-8")):
        out[tid] = status.strip()
    return out


def is_done(status):
    return status.startswith("DONE")


def label_of(status):
    for lab in sorted(LABELS, key=len, reverse=True):
        if status.startswith(lab):
            return lab
    return None


def check(strict=False):
    tasks = task_status()
    queue, mismatch, unknown, bad = [], [], [], []
    for path in sorted(DIAGRAMS.glob("*-backlogs.md")):
        text = path.read_text(encoding="utf-8")
        total = done = 0
        for bl, rest in ROW_RE.findall(text):
            cells = [c.strip() for c in rest.split("|")]
            status, refs = cells[-1], cells[-3]
            total += 1
            lab = label_of(status)
            if lab is None:
                bad.append("{}: {} status '{}'".format(path.stem, bl, status))
                continue
            if lab == "SELESAI":
                done += 1
            ids = re.findall(r"HNK-\d+\.T\d+", refs)
            missing = [t for t in ids if t not in tasks]
            if missing:
                unknown.append("{}: {} -> {}".format(path.stem, bl, ", ".join(missing)))
                continue
            if not ids or lab in ("ATURAN", "DITUNDA"):
                continue
            all_done = all(is_done(tasks[t]) for t in ids)
            if all_done and lab not in ("SELESAI", "GAGAL AUDIT"):
                queue.append("{}: {} ({})".format(path.stem, bl, ", ".join(ids)))
            if lab == "SELESAI" and not all_done:
                mismatch.append("{}: {} SELESAI but {} not DONE".format(
                    path.stem, bl, ", ".join(t for t in ids if not is_done(tasks[t]))))
        progress = "progress: {}/{} SELESAI".format(done, total)
        if re.search(r"^progress: .*$", text, re.M):
            new = re.sub(r"^progress: .*$", progress, text, count=1, flags=re.M)
        else:
            new = text.replace("\nupdated:", "\n" + progress + "\nupdated:", 1)
        if new != text:
            path.write_text(new, encoding="utf-8")
    for title, items in (("AUDIT QUEUE", queue), ("MISMATCH", mismatch),
                         ("UNKNOWN TASK", unknown), ("BAD STATUS", bad)):
        print("{}: {}".format(title, len(items)))
        for i in items:
            print("  - " + i)
    n = len(queue) + len(mismatch) + len(unknown) + len(bad)
    return 1 if (strict and n) else 0


if __name__ == "__main__":
    sys.exit(check("--strict" in sys.argv))
