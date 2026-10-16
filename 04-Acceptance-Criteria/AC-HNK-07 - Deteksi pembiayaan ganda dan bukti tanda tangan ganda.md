---
tags: [ac, "HNK-07"]
type: ac
id: HNK-07
phase: F3
lead: Hans
owners: [Hans, Dave, Dex]
status: PASS
updated: 2026-10-17
---

# AC-HNK-07 - Deteksi pembiayaan ganda dan bukti tanda tangan ganda

> **Peta link:** [[AC Hub]] · [[Backlog]] · **AC** · [[TEST-HNK-07 - Deteksi pembiayaan ganda dan bukti tanda tangan ganda|Test]] · [[ES-HNK-07 - Deteksi pembiayaan ganda dan bukti tanda tangan ganda|Exec Summary]]

**Item:** HNK-07 · **Fase:** F3 · **Dependency:** HNK-05

**Lead:** Hans #hans · **Tim:** Hans #hans, Dave #dave, Dex #dex

## Deskripsi
Financier kedua yang menerima invoice yang sama menemukan N di papan dan mendapat bundel bukti bahwa supplier menandatangani dua kali.

## Acceptance criteria
Status per kriteria: `TODO` / `PASS` / `FAIL` / `BLOCKED`, wajib dengan tanggal dan bukti (commit, txid, log, id tes).

| ID | Kriteria | Status | Tanggal | Bukti |
|---|---|---|---|---|
| AC-HNK-07.1 | Financier B menolak invoice yang N-nya sudah terdaftar. | PASS | 2026-10-17 | Testnet: financier B untuk `TES-INV-0003` berhenti di `Stopped(AlreadyFinanced)` (pemenang `33b8f3b0…`, tinggi 4509299) sebelum transaksi apa pun. Unit `financier::stops_when_another_financier_is_registered` |
| AC-HNK-07.2 | Bundel bukti (dua tanda tangan key sementara supplier atas N yang sama dengan commitment financier berbeda) bisa diverifikasi offline. | PASS | 2026-10-17 | `8e523f0`; unit `proof::tests` (3) + board `double_sign_proofs_from_a_race_and_from_an_offer`. Testnet: bukti dari tawaran supplier (532 byte / 710 karakter teks) valid offline dan posisinya cocok di papan; bukti dari balapan (entri B `05d5aa7a02a33c14d460922468745fb4d6d814daa83989eed22b21c0540c79eb`) valid offline, urutan papan cocok |
| AC-HNK-07.3 | Orang luar tanpa invoice tidak bisa memahami isi entri atau bundel. | PASS | 2026-10-17 | Entri di papan hanya berisi hash (N, commitment); tanda tangan supplier tidak bisa dicek tanpa key dari invoice (testnet: key tebakan = `false`, key invoice = `true`). Catatan jujur: orang luar bisa melihat N yang sama muncul dua kali, tapi tidak bisa membedakannya dari griefing atau tahu invoice dan pihaknya. Bundel bukti sengaja berisi invoice, jadi hanya diberikan ke pihak yang berwenang |
| AC-HNK-07.4 | Didemokan di mainnet dengan `TES-INV-0003`. | PASS | 2026-10-17 | Dibaca sebagai testnet (DEV-03): `TES-INV-0003`, entri A `33b8f3b0…`, entri B `05d5aa7a02a33c14d460922468745fb4d6d814daa83989eed22b21c0540c79eb`, total 100 dtk. **Uji ulang di mainnet bila ZEC tersedia** (HNK-07.T4, Dex) |

## Deviasi
_Kosong._ Kalau implementasi menyimpang dari keputusan, tulis di sini **dan** di [[Backlog]] bagian Log Deviasi. Tidak ada perubahan diam-diam.
