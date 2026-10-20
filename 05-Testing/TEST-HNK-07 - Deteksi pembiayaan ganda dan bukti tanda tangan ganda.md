---
tags: [test, "HNK-07"]
type: test
id: HNK-07
phase: F3
lead: Hans
owners: [Hans, Dex]
unit: PASS
integrasi: PASS
e2e: TODO
updated: 2026-10-17
---

# TEST-HNK-07 - Deteksi pembiayaan ganda dan bukti tanda tangan ganda

> **Peta link:** [[Testing Hub]] · [[Backlog]] · [[AC-HNK-07 - Deteksi pembiayaan ganda dan bukti tanda tangan ganda|AC]] · **Test** · [[ES-HNK-07 - Deteksi pembiayaan ganda dan bukti tanda tangan ganda|Exec Summary]]

**Lead:** Hans #hans · **Tim:** Hans #hans, Dex #dex 

## 1. Unit
Logika murni, cepat, tanpa DB dan tanpa chain.

| ID | Kasus | Hasil | Tanggal | Bukti |
|---|---|---|---|---|
| U-HNK-07.1 | Verifikasi bundel valid dan invalid | PASS | 2026-10-17 | `valid_proof_roundtrips_and_verifies`, `forged_or_mismatched_proofs_fail` (key lain, invoice lain, invoice tanpa tanda tangan buyer, byte rusak), board `double_sign_proofs_from_a_race_and_from_an_offer` (`8e523f0`) |
| U-HNK-07.2 | Entri ulang dengan commitment yang sama tidak dianggap penipuan | PASS | 2026-10-17 | `same_commitment_is_not_double_financing` (`NotDoubleSigned`), board `repost_with_same_commitment_is_not_a_conflict` |

## 2. Integrasi
Skrip vs DB/chain sungguhan. Semua artefak memakai prefix `TES-` (invoice, akun, label, order).

| ID | Skenario | Hasil | Tanggal | Bukti (txid/log) |
|---|---|---|---|---|
| I-HNK-07.1 | Supplier `TES-` mencoba ke financier `TES-b`; terdeteksi; bundel tersimpan | PASS (testnet, DEV-03) | 2026-10-17 | Scratchpad `proof-it`: B berhenti tanpa transaksi; bukti dari tawaran valid; varian balapan: entri B `05d5aa7a02a33c14d460922468745fb4d6d814daa83989eed22b21c0540c79eb` (fee 10000 zat) → `DoubleFinanced`, bukti dari papan valid. Bundel disimpan sebagai teks base64url (710 karakter) |

**Bukti pembersihan:** sisa artefak off-chain `TES-` = **0** (bundel hanya di memori dan log scratchpad). Artefak on-chain: entri B di atas; `TES-INV-0003` kini berstatus `DoubleFinanced` di papan testnet (disengaja). Artefak on-chain tidak bisa dihapus; catat txid-nya di tabel di atas. Data produksi tidak boleh tersentuh.

## 3. E2E
Panduan langkah demi langkah untuk user (naskah adegan: [[VID-06 - Skenario Demo Pembiayaan Ganda]]).

- [ ] Financier B memeriksa papan untuk invoice yang ditawarkan → berhenti di `AlreadyFinanced` tanpa transaksi.
- [ ] Financier B membentuk bukti dari tawaran supplier (backend `proof_from_offer`).
- [ ] Buka tab **Verify**, tempel bukti, klik *Verify*.
- [ ] Unduh bukti dengan *Download proof*.

| Langkah | Hasil diharapkan | Hasil aktual | Status |
|---|---|---|---|
| 1 | `AlreadyFinanced`, tanpa tx | Testnet `proof-it` (2026-10-17) | PASS |
| 2 | Bukti `JTSP…` valid offline | 710 karakter, valid | PASS |
| 3 | Banner "Caught: the supplier signed this invoice twice" + dua commitment | Halaman Verify dibangun; jalur yang sama teruji di unit `jitsuin-wasm` (`verify_proof`) | PASS |
| 4 | File `double-signature.proof.txt` terunduh | Tombol tersedia | PASS |
