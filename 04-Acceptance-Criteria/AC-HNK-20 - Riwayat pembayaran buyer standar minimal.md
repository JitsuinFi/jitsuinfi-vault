---
tags: [ac, "HNK-20"]
type: ac
id: HNK-20
phase: F3
lead: Hans
owners: [Hans]
status: TODO
updated: 2026-10-17
---

# AC-HNK-20 - Riwayat pembayaran buyer standar minimal

> **Peta link:** [[AC Hub]] · [[Backlog]] · **AC** · [[TEST-HNK-20 - Riwayat pembayaran buyer standar minimal|Test]] · [[ES-HNK-20 - Riwayat pembayaran buyer standar minimal|Exec Summary]]

**Lead:** Hans #hans · **Tim:** Hans #hans

**Item:** HNK-20 · **Fase:** F3 · **Dependency:** HNK-19

## Deskripsi
Riwayat pembayaran buyer menjadi standar minimal sebelum financier membiayai (D-20). Buyer memakai key per invoice agar papan publik tidak bisa menautkan invoice-invoice satu buyer, lalu membuktikan riwayat pelunasan tepat waktu ke financier baru secara selektif. Desain: [[Desain Jitsuin Seal]] bagian 7.

## Acceptance criteria
Status per kriteria: `TODO` / `PASS` / `FAIL` / `BLOCKED`, wajib dengan tanggal dan bukti (commit, txid, log, id tes).

| ID | Kriteria | Status | Tanggal | Bukti |
|---|---|---|---|---|
| AC-HNK-20.1 | Key buyer per invoice deterministik dari master secret; dua invoice buyer yang sama tidak bisa ditautkan dari papan; sertifikat delegasi terverifikasi. | TODO | — | — |
| AC-HNK-20.2 | Verifier bukti riwayat menerima pelunasan tepat waktu yang valid, dan menolak financier di luar allowlist, entri palsu, serta delegasi palsu. | TODO | — | — |
| AC-HNK-20.3 | Alur financier menolak registrasi kalau buyer tidak memenuhi standar minimal yang dikonfigurasi. | TODO | — | — |

## Deviasi
_Kosong._ Kalau implementasi menyimpang dari keputusan, tulis di sini **dan** di [[Backlog]] bagian Log Deviasi. Tidak ada perubahan diam-diam.
