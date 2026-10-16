---
tags: [architecture, spec]
---

# Format Data

**Bagian dari:** [[07 - Architecture]] · Kembali: [[START-HERE]] · Terkait: [[Arsitektur JitsuinFi]] · [[Nullifier]] · [[Memo Zcash]]

> **Draf.** Difinalkan di HNK-01 dan HNK-02 (lihat [[Backlog]]); diverifikasi di SPK-06. Perubahan setelah final wajib dicatat sebagai `DEV-xx`.

## Invoice kanonik (HNK-01) — **diimplementasikan** (`c0d6981`, rename `f4913a4`)
Field berurutan tetap, integer little-endian, decoder ketat (magic/version tidak dikenal, input terpotong, dan byte sisa ditolak):

| Field | Ukuran | Catatan |
|---|---|---|
| magic `JTSI` | 4 byte | |
| `version` | 1 byte | `0x01` |
| panjang `invoice_id` | 1 byte | 1–32 |
| `invoice_id` | 1–32 byte | ASCII cetak (`0x21`–`0x7E`); data uji berprefix `TES-` |
| `supplier_ephemeral_pk` | 32 byte | Key Ed25519 sementara khusus invoice ini (divalidasi sebagai titik) |
| `buyer_pk` | 32 byte | Key Ed25519 buyer (divalidasi sebagai titik) |
| `amount_zat` | 8 byte | > 0 |
| `issue_date` | 4 byte | Hari sejak epoch |
| `due_date` | 4 byte | Hari sejak epoch, ≥ `issue_date` |
| `terms_hash` | 32 byte | Hash dokumen syarat off-chain |

Tanda tangan buyer: `sig_buyer = Ed25519.sign(buyer_sk, bytes_kanonik)`; verifikasi memakai `verify_strict` (menolak signature non-kanonik dan key lemah).

**Test vector HNK-01:** supplier sk 32×`0x01`, buyer sk 32×`0x02`, `invoice_id` `TES-INV-0001`, `amount_zat` 1.000.000.000, `issue_date` 20.377, `due_date` 20.437, `terms_hash` 32×`0x09`:
- bytes kanonik (130 byte): `4a545349010c5445532d494e562d303030318a88e3dd7409f195fd52db2d3cba5d72ca6709bf1d94121bf3748801b40f6f5c8139770ea87d175f56a35466c34c7ecccb8d8a91b4ee37a25df60f5b8fc9b39400ca9a3b00000000994f0000d54f00000909090909090909090909090909090909090909090909090909090909090909`
- `sig_buyer`: `11b59c4dbce361601b4ba66f246b4ca17469722f506e23fa8d63de28b6acc142b091392510709c67fedd800bc93b8e7a7321c362363c8d04ca164d2a1e76cb0b`

## Nullifier (HNK-02)
> **Belum diimplementasikan — menunggu DEV-04.** Usulan: `N = BLAKE2b-256(personalization = "JitsuinNullifier", input = bytes_kanonik_invoice)` supaya N unik per invoice walaupun signer buyer tidak deterministik.

```
N = BLAKE2b-256(personalization = "JitsuinNullifier", input = sig_buyer)
```
N tidak bisa ditebak tanpa memegang invoice bertanda tangan.

## Entri papan registry (HNK-02) — **diimplementasikan** (`c0d6981`, rename `f4913a4`)
Isi memo (biner). Byte pertama memo `0xFF` menandai data arbitrer (ZIP-302, dikonfirmasi di SPK-06).

| Offset | Field | Ukuran |
|---|---|---|
| 0 | prefix memo `0xFF` | 1 |
| 1 | magic `JTS1` | 4 |
| 5 | tipe (`0x01` register, `0x02` settled) | 1 |
| 6 | `N` | 32 |
| 38 | `financier_commitment = BLAKE2b-256(financier_pk ‖ salt)` | 32 |
| 70 | `discount_bucket` | 1 |
| 71 | `tenor_bucket` | 1 |
| 72 | `sig_supplier` atas byte 1–71 (key sementara supplier) | 64 |
| **Total** | | **136 byte** (batas memo 512) |

Entri tanpa `sig_supplier` yang valid diabaikan (anti-griefing). Yang bisa memverifikasi `sig_supplier` hanya pemegang invoice, karena `supplier_ephemeral_pk` ada di invoice.

## Bundel bukti tanda tangan ganda (HNK-07)
Dua entri dengan `N` sama dan `financier_commitment` berbeda, keduanya bertanda tangan valid oleh `supplier_ephemeral_pk` yang sama, plus invoice kanonik. Bisa diverifikasi offline.

## Memo kuitansi (HNK-05, HNK-06)
Kuitansi pembayaran di muka dan pelunasan: magic, tipe, `N`, nominal, tanggal, tanda tangan pengirim. Layout difinalkan di HNK-05.

## Bucket indeks (HNK-08)
`discount_bucket` dan `tenor_bucket` = kelas diskon dan tenor (tanpa nominal). Tabel kelas difinalkan di HNK-08; indeks hanya ditampilkan bila ada minimal k entri per kelas.

## Urutan entri (HNK-04)
Urutan total: (tinggi blok, indeks transaksi, indeks output). Tie-break tambahan ditentukan di SPK-08.
