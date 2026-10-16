#!/usr/bin/env python3
"""new-item.py - scaffold workflow documents with stable IDs and two-way link headers.

Workflow rule (see 01-Workflow/Workflow Development): documents that grow per item use the
pattern Hub + one file per item, with a link-map header between artifacts.

Usage:
    # backlog item -> creates AC, TEST and ES files
    python3 scripts/new-item.py --kind item --id HNK-16 --title "Fitur baru" --phase F3
    # spike -> creates one SPK file
    python3 scripts/new-item.py --kind spike --id SPK-16 --title "Cek tool X" --area "Tooling"

Existing files are never overwritten. Runs the link check afterwards.
Can also be imported (functions write_item / write_spike) to create files with real content.
"""
import argparse
import datetime
import importlib.util
import re
import sys
from pathlib import Path

VAULT = Path(__file__).resolve().parent.parent
AC_DIR = VAULT / "04-Acceptance-Criteria"
TEST_DIR = VAULT / "05-Testing"
ES_DIR = VAULT / "06-Executive-Summary"
SPK_DIR = VAULT / "02-Spikes"
TODAY = datetime.date.today().isoformat()


def safe_title(title):
    return re.sub(r'[<>:"/\\|?*]', "", title).strip()


def names(item_id, title):
    t = safe_title(title)
    return (
        "AC-{} - {}".format(item_id, t),
        "TEST-{} - {}".format(item_id, t),
        "ES-{} - {}".format(item_id, t),
    )


def header(item_id, title, current):
    ac, test, es = names(item_id, title)
    parts = ["[[Backlog]]"]
    parts.append("**AC**" if current == "ac" else "[[{}|AC]]".format(ac))
    parts.append("**Test**" if current == "test" else "[[{}|Test]]".format(test))
    parts.append("**Exec Summary**" if current == "es" else "[[{}|Exec Summary]]".format(es))
    hub = {"ac": "AC Hub", "test": "Testing Hub", "es": "Exec Summary Hub"}[current]
    return "> **Peta link:** [[{}]] · ".format(hub) + " · ".join(parts)


def write_item(item_id, title, phase, depends="—", description="_TODO deskripsi item._",
               criteria=None, unit=None, integration=None, e2e=None, kpis=None, overwrite=False):
    ac_name, test_name, es_name = names(item_id, title)
    criteria = criteria or ["_TODO kriteria terukur_"]
    unit = unit or ["_TODO kasus unit_"]
    integration = integration or ["_TODO skenario integrasi_"]
    e2e = e2e or ["_TODO langkah E2E_"]
    kpis = kpis or [("_TODO KPI_", "_target_")]

    ac = [
        "---",
        'tags: [ac, "{}"]'.format(item_id),
        "type: ac",
        "id: {}".format(item_id),
        "phase: {}".format(phase),
        "status: TODO",
        "updated: {}".format(TODAY),
        "---",
        "",
        "# {}".format(ac_name),
        "",
        header(item_id, title, "ac"),
        "",
        "**Item:** {} · **Fase:** {} · **Dependency:** {}".format(item_id, phase, depends),
        "",
        "## Deskripsi",
        description,
        "",
        "## Acceptance criteria",
        "Status per kriteria: `TODO` / `PASS` / `FAIL` / `BLOCKED`, wajib dengan tanggal dan bukti (commit, txid, log, id tes).",
        "",
        "| ID | Kriteria | Status | Tanggal | Bukti |",
        "|---|---|---|---|---|",
    ]
    for i, c in enumerate(criteria, 1):
        ac.append("| AC-{}.{} | {} | TODO | — | — |".format(item_id, i, c))
    ac += [
        "",
        "## Deviasi",
        "_Kosong._ Kalau implementasi menyimpang dari keputusan, tulis di sini **dan** di [[Backlog]] bagian Log Deviasi. Tidak ada perubahan diam-diam.",
        "",
    ]

    test = [
        "---",
        'tags: [test, "{}"]'.format(item_id),
        "type: test",
        "id: {}".format(item_id),
        "phase: {}".format(phase),
        "unit: TODO",
        "integrasi: TODO",
        "e2e: TODO",
        "updated: {}".format(TODAY),
        "---",
        "",
        "# {}".format(test_name),
        "",
        header(item_id, title, "test"),
        "",
        "## 1. Unit",
        "Logika murni, cepat, tanpa DB dan tanpa chain.",
        "",
        "| ID | Kasus | Hasil | Tanggal | Bukti |",
        "|---|---|---|---|---|",
    ]
    for i, c in enumerate(unit, 1):
        test.append("| U-{}.{} | {} | TODO | — | — |".format(item_id, i, c))
    test += [
        "",
        "## 2. Integrasi",
        "Skrip vs DB/chain sungguhan. Semua artefak memakai prefix `TES-` (invoice, akun, label, order).",
        "",
        "| ID | Skenario | Hasil | Tanggal | Bukti (txid/log) |",
        "|---|---|---|---|---|",
    ]
    for i, c in enumerate(integration, 1):
        test.append("| I-{}.{} | {} | TODO | — | — |".format(item_id, i, c))
    test += [
        "",
        "**Bukti pembersihan:** sisa artefak off-chain `TES-` = _TODO_ (target **0**). Artefak on-chain tidak bisa dihapus; catat txid-nya di tabel di atas. Data produksi tidak boleh tersentuh.",
        "",
        "## 3. E2E",
        "Panduan langkah demi langkah untuk user.",
        "",
    ]
    for c in e2e:
        test.append("- [ ] {}".format(c))
    test += [
        "",
        "| Langkah | Hasil diharapkan | Hasil aktual | Status |",
        "|---|---|---|---|",
        "| 1 | _TODO_ | — | TODO |",
        "",
    ]

    es = [
        "---",
        'tags: [es, "{}"]'.format(item_id),
        "type: es",
        "id: {}".format(item_id),
        "phase: {}".format(phase),
        "status: BELUM",
        "updated: {}".format(TODAY),
        "---",
        "",
        "# {}".format(es_name),
        "",
        header(item_id, title, "es"),
        "",
        "## Apa diubah",
        "_TODO setelah langkah 1 selesai._",
        "",
        "## Hasil vs KPI (angka riil)",
        "| KPI | Target | Aktual |",
        "|---|---|---|",
    ]
    for k, target in kpis:
        es.append("| {} | {} | — |".format(k, target))
    es += [
        "",
        "## Status",
        "`BELUM` → isi `SELESAI` / `PARSIAL` / `BLOCKED` (juga di frontmatter).",
        "",
        "## Risiko tersisa",
        "_TODO_",
        "",
        "## Bukti",
        "- Commit: _TODO_",
        "- ID tes: _TODO_",
        "- Persetujuan user untuk push/deploy: _belum_",
        "",
    ]

    written = []
    for folder, name, body in ((AC_DIR, ac_name, ac), (TEST_DIR, test_name, test), (ES_DIR, es_name, es)):
        folder.mkdir(parents=True, exist_ok=True)
        path = folder / (name + ".md")
        if path.exists() and not overwrite:
            print("SKIP: sudah ada -> {}".format(path.relative_to(VAULT)))
            continue
        path.write_text("\n".join(body), encoding="utf-8")
        written.append(path)
        print("OK  dibuat: {}".format(path.relative_to(VAULT)))
    return written


def write_spike(spike_id, title, area="—", used_by="—", goal="_TODO_", hypothesis="_TODO_",
                steps=None, pass_criteria=None, fallback=None, notes="_TODO_", overwrite=False):
    name = "{} - {}".format(spike_id, safe_title(title))
    steps = steps or ["_TODO_"]
    pass_criteria = pass_criteria or ["_TODO_"]
    fallback = fallback or ["_TODO_"]
    body = [
        "---",
        'tags: [spike, "{}"]'.format(spike_id),
        "type: spike",
        "id: {}".format(spike_id),
        "area: {}".format(area),
        "status: TODO",
        "updated: {}".format(TODAY),
        "---",
        "",
        "# {}".format(name),
        "",
        "> **Peta link:** [[Spikes Hub]] · [[Backlog]] · [[Rencana Fase]]",
        "",
        "**Area:** {} · **Dipakai oleh:** {}".format(area, used_by),
        "",
        "## Tujuan",
        goal,
        "",
        "## Hipotesis",
        hypothesis,
        "",
        "## Langkah",
    ]
    body += ["{}. {}".format(i, s) for i, s in enumerate(steps, 1)]
    body += ["", "## Kriteria lulus"]
    body += ["- [ ] {}".format(c) for c in pass_criteria]
    body += ["", "## Fallback kalau gagal"]
    body += ["- {}".format(f) for f in fallback]
    body += [
        "",
        "## Hasil",
        "| Status | Tanggal | Bukti | Catatan |",
        "|---|---|---|---|",
        "| TODO | — | — | — |",
        "",
        "## Catatan",
        notes,
        "",
    ]
    SPK_DIR.mkdir(parents=True, exist_ok=True)
    path = SPK_DIR / (name + ".md")
    if path.exists() and not overwrite:
        print("SKIP: sudah ada -> {}".format(path.relative_to(VAULT)))
        return None
    path.write_text("\n".join(body), encoding="utf-8")
    print("OK  dibuat: {}".format(path.relative_to(VAULT)))
    return path


def load_check_links():
    spec = importlib.util.spec_from_file_location(
        "check_links", str(Path(__file__).resolve().parent / "check-links.py")
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--kind", choices=["item", "spike"], required=True)
    ap.add_argument("--id", required=True, help="stable ID, e.g. HNK-16 or SPK-16")
    ap.add_argument("--title", required=True)
    ap.add_argument("--phase", default="—")
    ap.add_argument("--area", default="—")
    a = ap.parse_args()
    if a.kind == "item":
        write_item(a.id, a.title, a.phase)
        print("Ingat: tambahkan baris {} ke tabel di 03-Backlog/Backlog.md".format(a.id))
    else:
        write_spike(a.id, a.title, area=a.area)
        print("Ingat: tambahkan baris {} ke tabel di 02-Spikes/Spikes Hub.md".format(a.id))
    _, n_broken = load_check_links().check(verbose=False)
    print("Link check: {}".format("Broken: 0" if n_broken == 0 else "ada link broken, jalankan check-links.py"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
