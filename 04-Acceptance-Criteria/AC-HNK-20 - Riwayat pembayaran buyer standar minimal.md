---
tags: [ac, "HNK-20"]
type: ac
id: HNK-20
phase: F3
lead: Hans
owners: [Hans]
status: PASS
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
| AC-HNK-20.1 | Key buyer per invoice deterministik dari master secret; dua invoice buyer yang sama tidak bisa ditautkan dari papan; sertifikat delegasi terverifikasi. | PASS | 2026-10-17 | `f03cfb1`; unit `key_derivation_vector_and_unlinkable_invoice_keys` (vector dicek silang Python), `chain_links_and_tags`, `rejects_gaps_forks_and_wrong_keys`. Testnet: dua invoice satu buyer memakai key dan tag berbeda (entri `89af294e…`, `fe713687…`). Sertifikat = sertifikat riwayat berantai (DEV-10) |
| AC-HNK-20.2 | Verifier bukti riwayat menerima pelunasan tepat waktu yang valid, dan menolak financier di luar allowlist, entri palsu, serta delegasi palsu. | PASS | 2026-10-17 | `687f2b4`; unit `complete_history_with_every_outcome`, `hiding_a_bad_invoice_is_caught`, `forged_tags_are_ignored_but_two_real_anchors_are_equivocation`, `allowlist_and_minimum_standard`. Testnet: laporan riwayat [PaidOnTime, Default] |
| AC-HNK-20.3 | Alur financier menolak registrasi kalau buyer tidak memenuhi standar minimal yang dikonfigurasi. | PASS | 2026-10-17 | `e53ce12`. Testnet: deal 2 ditolak (`buyer has defaults above the standard`); menyembunyikan deal 1 terdeteksi (`the board has a later invoice the buyer did not disclose`); mengaku buyer baru terdeteksi (`the board has a later invoice the buyer did not disclose`); entri tanpa tag ditolak alur |

## Deviasi
- **DEV-10**: rantai dijangkarkan ke papan (entri register `0x03` bertag), sertifikat memuat key supplier; "sertifikat delegasi" di kriteria 1 = sertifikat riwayat berantai.

_Catatan:_ Kalau implementasi menyimpang dari keputusan, tulis di sini **dan** di [[Backlog]] bagian Log Deviasi. Tidak ada perubahan diam-diam.
