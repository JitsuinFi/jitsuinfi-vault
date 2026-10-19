#!/usr/bin/env python3
"""Generate DFD-1 and DFD-2.x in 08-FlowDiagrams from scripts/dfd_model.py, and check balancing.

Level 2 is the source. Level 1 is rolled up from it: every level-1 flow is the union of the
level-2 flows of one process with the same entity or shared store in the same direction.
The "Di level 1" column of DFD-0 is rewritten from the roll-up, and the script fails when an
entity flow has no level-0 row or a level-0 row has no flow.

Usage: python3 scripts/build-dfd.py && python3 scripts/render-diagrams.py
"""
import os
import re
import sys
import textwrap

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dfd_model import E, D, L1NAME, L1STATUS, L2  # noqa: E402

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "08-FlowDiagrams")
UPDATED = "2026-10-20"
FRONT = "---\ntags: [flow, dfd]\nstatus: DRAF\nupdated: %s\n---\n\n" % UPDATED
COL = {"entity": 0, "process": 1, "store": 2}
# Level-0 rows: (entity, direction) -> K id. "in" = entity to system.
K0 = {("A", "in"): "K1", ("A", "out"): "K2", ("S", "in"): "K3", ("S", "out"): "K4",
      ("B", "in"): "K5", ("B", "out"): "K6", ("F", "in"): "K7", ("F", "out"): "K8",
      ("V", "out"): "K9", ("V", "in"): "K10", ("M", "out"): "K11", ("M", "in"): "K12",
      ("Z", "out"): "K13", ("Z", "in"): "K14"}
NOTE_LANES = ("Satu jalur = satu proses. Kotak bertanda `*` adalah entitas atau penyimpanan yang sama, "
              "digambar ulang supaya garis tidak bersilang. Proses bergaris penuh = ADA atau PARSIAL "
              "(rinciannya di kolom Status), kuning putus-putus = USULAN.")


def build(name, nodes, flows, nodesep=12, ranksep=35):
    """PlantUML with fixed columns: entities | processes | stores. Each flow is drawn as
    left node -- label node --> right node; flows inside one column use norank edges."""
    kind = {n[0]: n[1] for n in nodes}
    out = ["@startuml " + name, "!include dfd-style.iuml", "left to right direction",
           "skinparam nodesep %d" % nodesep, "skinparam ranksep %d" % ranksep]
    # Graphviz stacks left-to-right lanes bottom-up; declare in reverse so the first lane is on top.
    for nid, k, label, prop in reversed(nodes):
        st = k
        if prop and k == "process":
            st = "proposal"
        elif prop and k == "store":
            st = "storeproposal"
        out.append('rectangle "%s" <<%s>> as %s' % (label, st, nid))
    for fid, src, dst, text in flows:
        if COL[kind[src]] != COL[kind[dst]]:
            out.append('rectangle "%s %s" <<flow>> as f_%s' % (fid, text, fid.replace(".", "_")))
    for fid, src, dst, text in flows:
        lid = "f_" + fid.replace(".", "_")
        cs, cd = COL[kind[src]], COL[kind[dst]]
        if cs == cd:
            out.append("%s -[norank]-> %s : %s %s" % (src, dst, fid, text))
        elif cs < cd:
            out += ["%s -- %s" % (src, lid), "%s --> %s" % (lid, dst)]
        else:
            out += ["%s <-- %s" % (dst, lid), "%s -- %s" % (lid, src)]
    # keep every process in the middle column: a lane without entities gets an invisible spacer
    with_entity = set()
    for _, src, dst, _ in flows:
        if kind[src] == "entity":
            with_entity.add(dst)
        if kind[dst] == "entity":
            with_entity.add(src)
    for nid, k, _, _ in nodes:
        if k == "process" and nid not in with_entity:
            sp = "sp_" + nid
            out += ['rectangle " " <<spacer>> as %s_a' % sp, 'rectangle " " <<spacer>> as %s_b' % sp,
                    "%s_a -[hidden]- %s_b" % (sp, sp), "%s_b -[hidden]- %s" % (sp, nid)]
    out.append("@enduml")
    return "\n".join(out)


def flat(s):
    return s.replace("\\n", " ").replace("**", "").replace(" *", "").replace(" | ", " ").strip()


def base(r):
    return r.split("@")[0]


use = {}
for k, v in L2.items():
    for f in v["flows"]:
        for end in f[:2]:
            if base(end) in D:
                use.setdefault(base(end), set()).add(k)
SHARED = sorted([s for s, ks in use.items() if len(ks) > 1], key=lambda s: int(s[1:]))
LOCAL = {s: sorted(ks)[0] for s, ks in use.items() if len(ks) == 1}
unused = sorted(set(D) - set(use))
if unused:
    sys.exit("store tanpa aliran: %s" % unused)


def node_label(b, star):
    if b in E:
        return E[b] + star
    return "%s | %s%s" % (b, D[b][0], star)


def lanes(procs, flows, idfmt):
    nodes, seen, drawn = [], set(), set()

    def ref(r):
        if "@" not in r:
            return r
        b, k = r.split("@")
        nid = b + "_" + k
        if b not in E and b not in D:
            sys.exit("referensi tidak dikenal: %s" % r)
        if nid not in seen:
            seen.add(nid)
            star = " *" if b in drawn else ""
            drawn.add(b)
            nodes.append((nid, "entity" if b in E else "store", node_label(b, star), 0 if b in E else D[b][1]))
        return nid

    fl = [(idfmt(i + 1), ref(f[0]), ref(f[1]), f[2]) for i, f in enumerate(flows)]
    return [(p, "process", label, prop) for p, label, prop in procs] + nodes, fl


def ftable(allnodes, fl, extra=None):
    names = {n[0]: flat(n[2]) for n in allnodes}
    rows = ["| Aliran | Dari | Ke | Data |" + (" %s |" % extra[0] if extra else ""),
            "|---|---|---|---|" + ("---|" if extra else "")]
    for i, (fid, s, d, t) in enumerate(fl):
        rows.append("| %s | %s | %s | %s |" % (fid, names[s], names[d], flat(t)) + (" %s |" % extra[1][i] if extra else ""))
    return "\n".join(rows)


def ptable(rows):
    return "\n".join(["| Proses | Isi | Status | Kode / item |", "|---|---|---|---|"] + ["| %s | %s | %s | %s |" % r for r in rows])


HUB = "**Bagian dari:** [[08 - FlowDiagrams]] · Legenda: [[FD-00 - Arsitektur Target dan Legenda]] · Induk: [[DFD-1 - Proses Utama]]"
l1flows = {}
l2count = 0
localcount = 0
for k in range(1, 10):
    v = L2[k]
    if len(v["ptable"]) != len(v["procs"]):
        sys.exit("DFD-2.%d: tabel proses tidak sama dengan jumlah proses" % k)
    procs = [("P%d" % (i + 1), "**%s**\\n%s" % (pid, name), kind == "usulan") for i, (pid, name, kind) in enumerate(v["procs"])]
    allnodes, fl = lanes(procs, v["flows"], lambda i, k=k: "F%d.%02d" % (k, i))
    touched = {n for _, s, d, _ in fl for n in (s, d)}
    for p, _, _ in procs:
        if p not in touched:
            sys.exit("DFD-2.%d: proses %s tanpa aliran" % (k, p))
    for (fid, _, _, _), f in zip(fl, v["flows"]):
        l2count += 1
        tag = f[3] if len(f) > 3 else f[2]
        if any(base(e) in LOCAL for e in f[:2]):
            localcount += 1
        for end, direction in ((f[0], "in"), (f[1], "out")):
            b = base(end)
            if b in E or b in SHARED:
                l1flows.setdefault((k, b, direction), []).append((tag, fid))
            elif b in D and b not in LOCAL:
                sys.exit("store %s tidak terklasifikasi" % b)
    src = build("dfd-2-%d" % k, allnodes, fl)
    title = v["file"][:-3]
    local = sorted([s for s, kk in LOCAL.items() if kk == k], key=lambda s: int(s[1:]))
    loc = (" Penyimpanan lokal proses ini (tidak muncul di level 1): %s." % ", ".join("%s %s" % (s, flat(D[s][0])) for s in local)) if local else ""
    body = "# %s\n\n%s · Sequence: %s\n\n%s\n\n%s%s\n\n![%s](assets/dfd-2-%d.svg)\n\n```plantuml\n%s\n```\n\n## Proses\n\n%s\n\n## Aliran data\n\n%s\n%s" % (
        title, HUB, v["seqs"], v["intro"], NOTE_LANES, loc, title.split(" - ")[0], k, src,
        ptable(v["ptable"]), ftable(allnodes, fl), ("\n" + v["notes"]) if v.get("notes") else "")
    with open(os.path.join(ROOT, v["file"]), "w") as fh:
        fh.write(FRONT + body)

# ---------- level 1 (rolled up) ----------
procs = [("P%d" % k, "**%d.0**\\n%s" % (k, L1NAME[k]), False) for k in range(1, 10)]
l1 = []
for (k, b, direction), items in l1flows.items():
    tags = []
    for t, _ in items:
        if t not in tags:
            tags.append(t)
    label = "\\n".join(textwrap.wrap(", ".join(tags), 26))
    src, dst = ("%s@%d" % (b, k), "P%d" % k) if direction == "in" else ("P%d" % k, "%s@%d" % (b, k))
    l1.append((k, direction, b, src, dst, label, [i for _, i in items]))
l1.sort(key=lambda x: (x[0], 0 if x[2] in E else 1, x[2] if x[2] in E else int(x[2][1:]), {"in": 0, "out": 1}[x[1]]))
allnodes, fl = lanes(procs, [(x[3], x[4], x[5]) for x in l1], lambda i: "F%d" % i)
covered = sum(len(x[6]) for x in l1)
src = build("dfd-1", allnodes, fl)
storerows = ["| Penyimpanan | Isi | Level | Status |", "|---|---|---|---|"]
for s in sorted(D, key=lambda s: int(s[1:])):
    lvl = "1 dan 2" if s in SHARED else "2 (lokal %d.0)" % LOCAL[s]
    storerows.append("| %s | %s | %s | %s |" % (s, flat(D[s][0]), lvl, D[s][2]))
l1rows = [("%d.0 %s" % (k, flat(L1NAME[k])), "[[%s]]" % L2[k]["file"][:-3], L1STATUS[k],
           ", ".join(p[0] for p in L2[k]["procs"])) for k in range(1, 10)]
body = """# DFD-1 - Proses Utama

**Bagian dari:** [[08 - FlowDiagrams]] · Legenda: [[FD-00 - Arsitektur Target dan Legenda]] · Induk: [[DFD-0 - Diagram Konteks]]

Sembilan proses utama. Level 1 ini **dibuat oleh `scripts/build-dfd.py` dari level 2** (`scripts/dfd_model.py`): setiap aliran level 1 adalah gabungan aliran level 2 satu proses dengan entitas atau penyimpanan yang sama dan arah yang sama, dan kolom terakhir tabel aliran menyebut aliran level 2-nya. Skrip yang sama menulis ulang kolom "Di level 1" di [[DFD-0 - Diagram Konteks]] dan gagal bila ada aliran entitas tanpa baris level 0. Jangan edit file DFD-1 dan DFD-2.x langsung. Penyimpanan yang dipakai lebih dari satu proses digambar di sini; penyimpanan lokal hanya muncul di level 2.

Posting ke papan digambar sebagai tulisan ke D1 (secara fisik transaksi 10 000 zat + fee ZIP-317 ke alamat papan). Pembayaran uang (advance, pelunasan, setoran) dan data chain (tinggi tip, waktu blok, urutan tx) melewati entitas Jaringan Zcash. Satu transaksi advance muncul dua kali: sebagai tx ke Jaringan Zcash (uang ke supplier) dan sebagai tulisan ke D6 (memo JTN1 yang dibaca anggota dana dari akun operasional).

%s

![DFD-1](assets/dfd-1.svg)

```plantuml
%s
```

## Proses

| Proses | Rincian | Status | Subproses |
|---|---|---|---|
%s

## Penyimpanan data (semua level)

%s

## Aliran data

%s
""" % (NOTE_LANES, src, "\n".join("| %s | %s | %s | %s |" % r for r in l1rows), "\n".join(storerows),
       ftable(allnodes, fl, ("Level 2", [", ".join(x[6]) for x in l1])))
with open(os.path.join(ROOT, "DFD-1 - Proses Utama.md"), "w") as fh:
    fh.write(FRONT + body)

# ---------- level 0 mapping and balance ----------
k0 = {}
for i, x in enumerate(l1):
    if x[2] in E:
        if (x[2], x[1]) not in K0:
            sys.exit("aliran level 1 F%d (%s, %s) tanpa baris level 0" % (i + 1, x[2], x[1]))
        k0.setdefault(K0[(x[2], x[1])], []).append("F%d" % (i + 1))
missing = sorted(set(K0.values()) - set(k0), key=lambda s: int(s[1:]))
if missing:
    sys.exit("baris level 0 tanpa aliran level 1: %s" % missing)
p0 = os.path.join(ROOT, "DFD-0 - Diagram Konteks.md")
text = open(p0).read()
for kid, fs in k0.items():
    pat = re.compile(r"^(\| %s \|(?:[^|\n]*\|){3}) [^|\n]* \|$" % kid, re.M)
    if not pat.search(text):
        sys.exit("DFD-0: baris %s tidak ditemukan" % kid)
    text = pat.sub(lambda m: "%s %s |" % (m.group(1), ", ".join(fs)), text)
with open(p0, "w") as fh:
    fh.write(text)
if covered + localcount != l2count:
    sys.exit("roll-up tidak lengkap: %d + %d lokal dari %d aliran level 2" % (covered, localcount, l2count))
print("OK: %d aliran level 2 (%d lewat penyimpanan lokal), %d aliran level 1, %d baris level 0; shared %s"
      % (l2count, localcount, len(fl), len(k0), ", ".join(SHARED)))
