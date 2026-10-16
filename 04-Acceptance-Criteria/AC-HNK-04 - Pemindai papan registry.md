---
tags: [ac, "HNK-04"]
type: ac
id: HNK-04
phase: F2
lead: Hans
owners: [Hans, Dex]
status: PASS
updated: 2026-10-17
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
| AC-HNK-04.1 | Semua entri uji sejak birthday height terbaca. | PASS | 2026-10-17 | commit `ef55987` (`jitsuinfi-zcash`); testnet: `scan` membaca 4 tx papan sejak birthday (semua entri uji) |
| AC-HNK-04.2 | Entri invalid (tanda tangan salah, format salah) diabaikan dan dilaporkan. | PASS | 2026-10-17 | 4 memo format invalid ditolak dan dilaporkan (`unknown magic bytes`: 3 entri lama `HNK1` + 1 `JTSX` sengaja rusak); entri dengan signature key salah diabaikan oleh `lookup` (`ignored_invalid=1`) |
| AC-HNK-04.3 | Urutan entri deterministik; N ganda terdeteksi; entri sah pertama yang menang. | PASS | 2026-10-17 | Urutan (tinggi, indeks tx dari `GetBlock`, indeks output). Lookup N=`42…`: `DoubleFinanced`, pemenang tx `8d8835f7…` (paling awal), 1 konflik dari tx `b8a272a87ad9023f3a00a6ffb630e8a584ba0a279af624cda939426c75809970` |
| AC-HNK-04.4 | Waktu scan tercatat. | PASS | 2026-10-17 | Waktu scan papan uji 5,9 dtk (target < 2 menit) |

## Deviasi
_Kosong._ Kalau implementasi menyimpang dari keputusan, tulis di sini **dan** di [[Backlog]] bagian Log Deviasi. Tidak ada perubahan diam-diam.
