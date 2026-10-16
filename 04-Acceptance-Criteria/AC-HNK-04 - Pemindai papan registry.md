---
tags: [ac, "HNK-04"]
type: ac
id: HNK-04
phase: F2
lead: Hans
owners: [Hans, Dex]
status: TODO
updated: 2026-10-16
---

# AC-HNK-04 - Pemindai papan registry

> **Peta link:** [[AC Hub]] · [[Backlog]] · **AC** · [[TEST-HNK-04 - Pemindai papan registry|Test]] · [[ES-HNK-04 - Pemindai papan registry|Exec Summary]]

**Item:** HNK-04 · **Fase:** F2 · **Dependency:** HNK-02, HNK-03, SPK-05, SPK-08

**Lead:** Hans #hans · **Tim:** Hans #hans, Dex #dex

## Deskripsi
Scanner watch-only yang memakai viewing key papan untuk membaca semua entri, memvalidasi, dan menyusun urutan (tinggi blok, indeks transaksi).

## Acceptance criteria
Status per kriteria: `TODO` / `PASS` / `FAIL` / `BLOCKED`, wajib dengan tanggal dan bukti (commit, txid, log, id tes).

| ID | Kriteria | Status | Tanggal | Bukti |
|---|---|---|---|---|
| AC-HNK-04.1 | Semua entri uji sejak birthday height terbaca. | TODO | — | — |
| AC-HNK-04.2 | Entri invalid (tanda tangan salah, format salah) diabaikan dan dilaporkan. | TODO | — | — |
| AC-HNK-04.3 | Urutan entri deterministik; N ganda terdeteksi; entri sah pertama yang menang. | TODO | — | — |
| AC-HNK-04.4 | Waktu scan tercatat. | TODO | — | — |

## Deviasi
_Kosong._ Kalau implementasi menyimpang dari keputusan, tulis di sini **dan** di [[Backlog]] bagian Log Deviasi. Tidak ada perubahan diam-diam.
