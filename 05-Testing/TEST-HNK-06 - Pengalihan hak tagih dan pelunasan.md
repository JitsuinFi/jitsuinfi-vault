---
tags: [test, "HNK-06"]
type: test
id: HNK-06
phase: F3
lead: Hans
owners: [Dex, Hans, Dave]
unit: PASS
integrasi: PASS
e2e: TODO
updated: 2026-10-17
---

# TEST-HNK-06 - Pengalihan hak tagih dan pelunasan

> **Peta link:** [[Testing Hub]] · [[Backlog]] · [[AC-HNK-06 - Pengalihan hak tagih dan pelunasan|AC]] · **Test** · [[ES-HNK-06 - Pengalihan hak tagih dan pelunasan|Exec Summary]]

**Lead:** Hans #hans · **Tim:** Dex #dex, Hans #hans, Dave #dave

## 1. Unit
Logika murni, cepat, tanpa DB dan tanpa chain.

| ID | Kasus | Hasil | Tanggal | Bukti |
|---|---|---|---|---|
| U-HNK-06.1 | Format surat pengalihan | TODO | — | Bagian Dex (HNK-06.T1). Sudah ada untuk T2: `request_carries_a_buyer_signed_receipt`, `qr_decodes_back_to_the_uri` (QR di-decode balik dengan `rqrr`), `builds_zip321_uri` |
| U-HNK-06.2 | Pencocokan pembayaran ke N | PASS | 2026-10-17 | `status_follows_mined_valid_payments` (Unpaid/Pending/Partial/Settled, kuitansi palsu dan nominal beda tidak dihitung, kuitansi advance bukan pelunasan), `settled_entry_is_unlinkable_without_n_and_never_conflicts`, `receipts::verifies_signer_kind_and_amount`, board `settled_entries_do_not_conflict_and_need_the_financier_signature`, core `settled_tag_vector` |

## 2. Integrasi
Skrip vs DB/chain sungguhan. Semua artefak memakai prefix `TES-` (invoice, akun, label, order).

| ID | Skenario | Hasil | Tanggal | Bukti (txid/log) |
|---|---|---|---|---|
| I-HNK-06.1 | Buyer `TES-` membayar `TES-INV-0002` ke financier `TES-`; terdeteksi | PASS (testnet, DEV-03) | 2026-10-17 | Scratchpad `settle-it`: URI 438 karakter (QR SVG 63730 byte), pelunasan `b29fd4e1755159e2088777e6f2a31284908db3997722763206ac2efe489f7118` (fee 15000 zat) terdeteksi `Settled`, entri `settled` `a81cd2045664e83a4141278f4878c401d6181344b90d02526fb2b61205e5e858` (fee 10000 zat), posting ulang tidak membayar lagi. Total 308 dtk |

**Bukti pembersihan:** sisa artefak off-chain `TES-` = **0** (tidak ada DB; QR hanya di memori). Artefak on-chain tidak bisa dihapus; catat txid-nya di tabel di atas. Data produksi tidak boleh tersentuh.

## 3. E2E
Panduan langkah demi langkah untuk user.

- [ ] Buyer membayar dari Zodl via QR ZIP-321 (kalau SPK-04 PASS).
- [ ] Financier melihat status berubah menjadi lunas.

| Langkah | Hasil diharapkan | Hasil aktual | Status |
|---|---|---|---|
| 1 | _TODO_ | — | TODO |
