---
tags: [conventions]
---

# Conventions

Aturan vault ini. Diadaptasi dari panduan `ObsidianGuides/Conventions.md`, ditambah aturan proyek dari [[Workflow Development]].

## Struktur
- Modul = folder `NN-nama/` (prefix 2 digit), mudah di-sort dan cocok dengan regex `^\d{2}-`.
- Dokumen yang tumbuh per item (AC, testing, exec summary, spike) memakai pola **Hub + satu file per item**.
- Sumber eksternal (folder `Brainstorm/`, `reports/`, `research_notes/`, `Info/` di luar vault) **tidak diubah** dan dirujuk sebagai inline code path, bukan wikilink. Lihat [[Sumber Eksternal]].

## ID stabil (konsisten lintas dokumen)
| Prefix | Arti | Contoh nama file |
|---|---|---|
| `HNK-xx` | Item backlog | `AC-HNK-01 - <Judul>.md`, `TEST-HNK-01 - <Judul>.md`, `ES-HNK-01 - <Judul>.md` |
| `SPK-xx` | Spike | `SPK-01 - <Judul>.md` |
| `VID-xx` | Dokumen video | `VID-01 - <Judul>.md` |
| `DEV-xx` | Deviasi dari rencana | ditulis di [[Backlog]] bagian Log Deviasi |
| `D-xx` | Keputusan | ditulis di [[Decision Log]] |
| `AC-HNK-xx.k` | Kriteria ke-k dari item | baris tabel di file AC |
| `U-`, `I-` | Kasus unit dan integrasi | baris tabel di file TEST |
| `TES-` | Prefix artefak uji integrasi | `TES-INV-0001`, label akun `TES-financier-a` |
| `FD-xx`, `PG-xx` | Dokumen alur: arsitektur target, peta halaman | `FD-00 - <Judul>.md`, `PG-01 - <Judul>.md` |
| `SEQ-xx` | Sequence diagram per peran | `SEQ-01 - Supplier.md` |
| `DFD-n` / `DFD-2.k` | DFD level 0, 1, dan level 2 per proses k | `DFD-2.3 - Registrasi Papan.md` |
| `P-xx` | Usulan desain di [[FD-00 - Arsitektur Target dan Legenda]] (belum keputusan) | `P-04` |

ID tidak pernah dipakai ulang. Item yang dibatalkan tetap ada dengan status `BLOCKED` dan alasan.

## Status
| Artefak | Nilai status |
|---|---|
| Spike | `TODO` / `PASS` / `FAIL` / `BLOCKED` |
| Kriteria AC | `TODO` / `PASS` / `FAIL` / `BLOCKED` + tanggal + bukti |
| Test (unit/integrasi/e2e) | `TODO` / `PASS` / `FAIL` / `BLOCKED` |
| Exec summary | `BELUM` / `SELESAI` / `PARSIAL` / `BLOCKED` |

Status ditulis di frontmatter (dibaca [[Dashboard]]) **dan** di isi note.

## Header peta link
Setiap file AC, TEST, dan ES dibuka dengan baris "Peta link" yang menautkan hub, backlog, dan dua artefak saudaranya. Dibuat otomatis oleh `scripts/new-item.py`.

## Nama file
- Hindari `: \ / | ? * " < >` di nama file (`:` → ` - `, `/` → `-`).
- Jangan pakai emoji di nama file.
- Hub/MOC modul: `NN - Title.md` di `Module-Guides/`.

## Link
- Wikilink hanya ke `.md`. File lain (gambar, video, `.rs`, `.json`) → inline code path.
- Basename harus unik di seluruh vault, karena link pakai format terpendek.
- Display link: `[[Target|tampilan]]`. Di dalam tabel, tulis pipe sebagai `\|`.

## Tag dan frontmatter
- Tag tanpa spasi. Tag identitas diberi quote: `"HNK-01"`.
- `tags: [concept]` untuk catatan konsep atomik.
- Field Dataview: `type`, `id`, `phase`, `status`, `updated` (format `YYYY-MM-DD`).

## Otomasi
- Script versi Python (`scripts/*.py`) adalah yang utama, karena PowerShell tidak terpasang di Mac. Versi asli `.ps1` untuk Windows ada di `scripts/windows/`.
- Setelah edit vault: `python3 scripts/sync-vault.py` → target `Broken: 0`.
- Daftar panjang memakai Dataview atau `_Auto-Index`, bukan daftar manual.

Lanjut: [[Quick-Reference]] · [[Glossary]] · [[Workflow Development]]
