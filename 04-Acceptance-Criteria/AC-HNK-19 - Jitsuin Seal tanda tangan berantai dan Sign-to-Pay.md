---
tags: [ac, "HNK-19"]
type: ac
id: HNK-19
phase: F3
lead: Hans
owners: [Hans]
status: TODO
updated: 2026-10-17
---

# AC-HNK-19 - Jitsuin Seal tanda tangan berantai dan Sign-to-Pay

> **Peta link:** [[AC Hub]] · [[Backlog]] · **AC** · [[TEST-HNK-19 - Jitsuin Seal tanda tangan berantai dan Sign-to-Pay|Test]] · [[ES-HNK-19 - Jitsuin Seal tanda tangan berantai dan Sign-to-Pay|Exec Summary]]

**Lead:** Hans #hans · **Tim:** Hans #hans

**Item:** HNK-19 · **Fase:** F3 · **Dependency:** HNK-05, HNK-06

## Deskripsi
Adopsi konsep SignBaliola (D-21): dokumen invoice, surat pengalihan, dan pelunasan ditandatangani beberapa pihak secara berurutan dengan seal berantai. Advance hanya cair setelah surat pengalihan tersegel Supplier dan Buyer, dan tanda tangan Financier ikut dalam transaksi advance (Sign-to-Pay). Pelunasan sah hanya dengan tanda tangan buyer dan financier. Desain: [[Desain Jitsuin Seal]].

## Acceptance criteria
Status per kriteria: `TODO` / `PASS` / `FAIL` / `BLOCKED`, wajib dengan tanggal dan bukti (commit, txid, log, id tes).

| ID | Kriteria | Status | Tanggal | Bukti |
|---|---|---|---|---|
| AC-HNK-19.1 | Seal berantai: urutan salah, role ganda, satu key untuk dua role, dan isi seal yang diubah ditolak; policy lengkap menghasilkan `Sealed`. | TODO | — | — |
| AC-HNK-19.2 | Surat pengalihan kanonik memuat N, nominal, jatuh tempo, `financier_pk`, alamat bayar, dan `terms_hash`; tersegel Supplier lalu Buyer dan terverifikasi. | TODO | — | — |
| AC-HNK-19.3 | Advance tidak bisa dikirim sebelum seal Supplier dan Buyer valid; memo advance memuat kuitansi dan seal Financier dalam satu transaksi shielded. | TODO | — | — |
| AC-HNK-19.4 | Entri `settled` memuat tanda tangan buyer dan financier; klaim buyer tanpa pembayaran berakhir `Disputed`, bukan `Settled`. | TODO | — | — |
| AC-HNK-19.5 | Satu siklus penuh `TES-INV-0003` di testnet (DEV-03), semua txid tercatat. | TODO | — | — |

## Deviasi
_Kosong._ Kalau implementasi menyimpang dari keputusan, tulis di sini **dan** di [[Backlog]] bagian Log Deviasi. Tidak ada perubahan diam-diam.
