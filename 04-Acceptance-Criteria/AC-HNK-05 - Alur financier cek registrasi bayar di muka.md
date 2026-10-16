---
tags: [ac, "HNK-05"]
type: ac
id: HNK-05
phase: F3
lead: Hans
owners: [Hans, Dex, Dave]
status: TODO
updated: 2026-10-16
---

# AC-HNK-05 - Alur financier cek registrasi bayar di muka

> **Peta link:** [[AC Hub]] · [[Backlog]] · **AC** · [[TEST-HNK-05 - Alur financier cek registrasi bayar di muka|Test]] · [[ES-HNK-05 - Alur financier cek registrasi bayar di muka|Exec Summary]]

**Item:** HNK-05 · **Fase:** F3 · **Dependency:** HNK-04

**Lead:** Hans #hans · **Tim:** Hans #hans, Dex #dex, Dave #dave

## Deskripsi
Financier memeriksa papan, mendaftarkan N, menunggu minimal satu konfirmasi, lalu membayar di muka secara shielded ke supplier dengan memo kuitansi.

## Acceptance criteria
Status per kriteria: `TODO` / `PASS` / `FAIL` / `BLOCKED`, wajib dengan tanggal dan bukti (commit, txid, log, id tes).

| ID | Kriteria | Status | Tanggal | Bukti |
|---|---|---|---|---|
| AC-HNK-05.1 | Kalau N sudah ada di papan, alur berhenti sebelum pembayaran. | TODO | — | — |
| AC-HNK-05.2 | Entri registrasi terkonfirmasi sebelum pembayaran di muka dikirim. | TODO | — | — |
| AC-HNK-05.3 | Pembayaran di muka shielded dengan memo kuitansi bertanda tangan financier; supplier memverifikasinya. | TODO | — | — |
| AC-HNK-05.4 | Satu siklus penuh di mainnet dengan invoice `TES-INV-xxxx`; semua txid tercatat. | TODO | — | — |

## Deviasi
_Kosong._ Kalau implementasi menyimpang dari keputusan, tulis di sini **dan** di [[Backlog]] bagian Log Deviasi. Tidak ada perubahan diam-diam.
