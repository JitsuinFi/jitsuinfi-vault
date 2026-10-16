---
tags: [test, "HNK-19"]
type: test
id: HNK-19
phase: F3
lead: Hans
owners: [Hans]
unit: PASS
integrasi: PASS
e2e: TODO
updated: 2026-10-17
---

# TEST-HNK-19 - Jitsuin Seal tanda tangan berantai dan Sign-to-Pay

> **Peta link:** [[Testing Hub]] · [[Backlog]] · [[AC-HNK-19 - Jitsuin Seal tanda tangan berantai dan Sign-to-Pay|AC]] · **Test** · [[ES-HNK-19 - Jitsuin Seal tanda tangan berantai dan Sign-to-Pay|Exec Summary]]

**Lead:** Hans #hans · **Tim:** Hans #hans

## 1. Unit
Logika murni, cepat, tanpa DB dan tanpa chain.

| ID | Kasus | Hasil | Tanggal | Bukti |
|---|---|---|---|---|
| U-HNK-19.1 | Rantai seal: urutan, role, key ganda, tamper | PASS | 2026-10-17 | `seal::tests` (6) di `b007a26` |
| U-HNK-19.2 | Surat pengalihan kanonik roundtrip dan decoder ketat | PASS | 2026-10-17 | `assignment::tests` (3) di `fdc399e` |
| U-HNK-19.3 | Gerbang `AwaitAssignment` di state machine | PASS | 2026-10-17 | `financier::tests` (10): `happy_path_waits_for_confirmations_and_the_sealed_letter`, `incomplete_or_forged_letters_keep_the_money`, `late_double_financing_or_reorg_before_paying`, dll. (`f9fee3e`) |
| U-HNK-19.4 | Memo dua item (kuitansi + seal) encode/decode | PASS | 2026-10-17 | `memo::tests` (2), `supplier::advance_and_last_seal_arrive_together`, `finds_an_advance_already_sent` (memo dua item dan memo lama) |
| U-HNK-19.5 | Status pelunasan: Unpaid, Claimed, Settled, Disputed, Overdue | PASS | 2026-10-17 | `settlement::tests` (3), `settled::tests` (3), board `settled_entries_are_separate_and_need_both_signatures` (`f07787b`); bundel `bundle::tests` (2, `dd23864`) |

## 2. Integrasi
Skrip vs DB/chain sungguhan. Semua artefak memakai prefix `TES-` (invoice, akun, label, order).

| ID | Skenario | Hasil | Tanggal | Bukti (txid/log) |
|---|---|---|---|---|
| I-HNK-19.1 | Siklus penuh `TES-INV-0003` di testnet: registrasi, surat pengalihan, advance Sign-to-Pay, pelunasan dua tanda tangan | PASS (testnet, DEV-03) | 2026-10-17 | Scratchpad `cycle-it` (302 dtk): entri `33b8f3b0aa754e790e9c7fac0ae7dc08ce8612a8c26620d551d790e1ea390a56` (fee 10000), konfirmasi tinggi 4509299, advance `501e40dafff4d2b7bcedf1adb9535522dc8977b6c6c8f8d3da55e00574335ccb` (fee 10000), pelunasan `d59014b726554404fc5729c8699d0d029fab7a3900485241d632c50bf4aadaf0` (fee 10000, URI 705 karakter, QR SVG 96846 byte), `settled` `dcba74c63a701057d0e6e5f2cee4391b509d393c792801449c772c9552b7cad3` (fee 10000). Scratchpad `bundle-it`: bundel 1212 byte / 1616 karakter teks, offline `Sealed`, papan: register `33b8f3b0…` + `settled` `dcba74c6…` (on_time true); bundel dengan nominal diubah ditolak (`BadSignature`) |

**Bukti pembersihan:** sisa artefak off-chain `TES-` = **0** (tidak ada DB; bundel dan QR hanya di memori). Artefak on-chain tidak bisa dihapus; catat txid-nya di tabel di atas. Data produksi tidak boleh tersentuh.

## 3. E2E
Panduan langkah demi langkah untuk user.

- [ ] _TODO langkah E2E_

| Langkah | Hasil diharapkan | Hasil aktual | Status |
|---|---|---|---|
| 1 | _TODO_ | — | TODO |
