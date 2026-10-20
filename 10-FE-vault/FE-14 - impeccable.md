---
tags: [fe-tool, "FE-14"]
type: fe-tool
id: FE-14
layer: skill
status: TERPASANG-BELUM-INIT
updated: 2026-10-20
---

# FE-14 - impeccable

> **Peta link:** [[FE-00 - Peta Tools FE|Peta tools]] · [[10 - FE Vault|Hub modul]] · [[FE-01 - Batasan Platform FE|Batasan platform]]

Skill desain, command, dan detektor anti-pattern untuk agent coding. Dipasang 2026-10-20, belum dipakai.

## Akar
| | |
|---|---|
| Paket npm | `impeccable` 4.7.0, maintainer Paul Bakaus, repo https://github.com/pbakaus/impeccable, lisensi Apache 2.0 |
| Perintah pasang | `npx -y impeccable@4.7.0 install --project --providers=claude --no-hooks -y` (dijalankan dari `zkSNARK/`) |
| Lingkup | Proyek `zkSNARK` saja (bukan global), **tanpa hook** (pilihan user) |
| Lokasi | `zkSNARK/.claude/skills/impeccable/` dan `zkSNARK/.claude/agents/impeccable-*.md`; di luar repo `jitsuinfi-*`, jadi tidak ikut ter-commit |
| Engine | Biner `impeccable` v0.1.16 darwin-arm64 (±16 MB) di `.claude/skills/impeccable/scripts/bin/darwin-arm64/`; launcher `scripts/impeccable` |
| Settings | `settings.json` tidak diubah |

## Cara kerja
1. Setup per sesi: `.claude/skills/impeccable/scripts/impeccable context` memuat `PRODUCT.md`, `DESIGN.md`, dan brief permukaan (belum ada di proyek ini).
2. Muat playbook command dari `reference/<command>.md`, atau `reference/new-work.md` untuk permukaan baru.
3. Sebelum edit UI apa pun: `reference/craft-floor.md` (batas kualitas dan larangan).

Mode permukaan: **Persuade** (landing), **Operate** (app, dashboard, settings), **Read** (dokumen), **Experience** (galeri).

## Command (`/impeccable <command>`)
| Kelompok | Command |
|---|---|
| Build | `shape`, `init` (alias `teach`, tulis PRODUCT.md), `document` (tulis DESIGN.md dari kode), `extract`, `craft` (alias usang) |
| Evaluate | `critique` (skor heuristik), `audit` (a11y, performa, responsif; varian native) |
| Refine | `polish`, `bolder`, `quieter`, `distill`, `harden`, `onboard` |
| Enhance | `animate`, `colorize`, `typeset`, `layout`, `delight`, `overdrive` |
| Fix | `clarify`, `adapt`, `optimize` |
| Iterate | `live` (pilih elemen di browser), `generate [n]` (varian) |
| Lain | `pin`/`unpin`, `hooks <on\|off\|status…>`, `doctor` |

## Agent bawaan (`.claude/agents/`)
| Agent | Tugas | Tools |
|---|---|---|
| `impeccable-asset-producer` | Aset raster dari mock yang disetujui | Read, Write, Edit, Bash, Glob, Grep |
| `impeccable-documenter` | Menulis DESIGN.md dari hasil build | Read, Write, Bash, Glob, Grep |
| `impeccable-finish-reviewer` | Review hasil akhir terhadap arah desain | Read, Bash, Glob, Grep |
| `impeccable-manual-edit-applier` | Menerapkan edit copy dari mode live | Read, Write, Edit, Bash, Glob, Grep |

## Hubungan dengan JitsuinFi
- Desain landing sudah tercatat di `jitsuinfi-frontend/MASTER.md` (bukan DESIGN.md). `/impeccable document` atau `init` akan membuat file baru; putuskan dulu apakah MASTER.md tetap sumber tunggal.
- Calon pemakaian: `critique`/`audit` untuk layar app (HNK-21, HNK-22) dan `harden`/`clarify` untuk pesan error.

## Batasan dan risiko
- Mode `live` menyuntikkan `live-browser.js` (±537 KB) ke halaman; CSP `script-src 'self'` bisa memblokirnya di build produksi.
- Engine adalah biner tertutup yang belum diaudit; jalankan hanya di proyek ini.
- Hook detektor sengaja tidak dipasang; aktifkan hanya dengan izin (`/impeccable hooks on`).

## Status
TERPASANG, BELUM `init`.
