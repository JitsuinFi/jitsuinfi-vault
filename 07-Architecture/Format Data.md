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

## Nullifier (HNK-02) — **diimplementasikan** (`40d7656`, DEV-04)
```
N = BLAKE2b-256(personalization = "JitsuinNullifier", input = bytes_kanonik_invoice)
```
N unik per invoice walaupun signer buyer tidak deterministik, dan tidak bisa ditebak tanpa invoice karena byte kanonik memuat `supplier_ephemeral_pk` acak 256 bit. N adalah id dokumen invoice: semua entri, kuitansi, dan seal merujuk N ([[Desain Jitsuin Seal]]). Tanda tangan buyer tetap wajib sebagai bukti persetujuan, tapi bukan input N.

**Test vector:** invoice HNK-01 di atas → N = `3513c284b075c8efbd27da2de1ad9eb673bcbb8c45ae087a9a594c35c8064a6e` (dicek silang Python `hashlib.blake2b(digest_size=32, person=b"JitsuinNullifier")`).

**Hash dokumen off-chain:** `terms_hash = SHA-256(file)` dihitung di klien (`document_hash`), jadi file tidak pernah dikirim dan bisa dicek dengan `shasum -a 256`. Vector: `SHA-256("TES-terms")` = `00082d1119307d17036738bf382daab1bfe963280b44b7dc050f5ad30542b229`.

## Entri papan registry (HNK-02) — **diimplementasikan** (`c0d6981`, rename `f4913a4`)
Isi memo (biner). Byte pertama memo `0xFF` menandai data arbitrer (ZIP-302, dikonfirmasi di SPK-06).

| Offset | Field | Ukuran |
|---|---|---|
| 0 | prefix memo `0xFF` | 1 |
| 1 | magic `JTS1` | 4 |
| 5 | tipe (`0x01` register, `0x02` settled — lihat bagian Entri `settled`) | 1 |
| 6 | `N` | 32 |
| 38 | `financier_commitment = BLAKE2b-256(financier_pk ‖ salt)` | 32 |
| 70 | `discount_bucket` | 1 |
| 71 | `tenor_bucket` | 1 |
| 72 | `sig_supplier` atas byte 1–71 (key sementara supplier) | 64 |
| **Total** | | **136 byte** (batas memo 512) |

Entri tanpa `sig_supplier` yang valid diabaikan (anti-griefing). Yang bisa memverifikasi `sig_supplier` hanya pemegang invoice, karena `supplier_ephemeral_pk` ada di invoice.

## Bundel bukti tanda tangan ganda (HNK-07) — **diimplementasikan** (`8e523f0`)
Dua entri register dengan `N` sama dan `financier_commitment` berbeda, keduanya bertanda tangan valid oleh `supplier_ephemeral_pk` dari invoice, plus invoice kanonik bertanda tangan buyer. Bisa diverifikasi offline.

Layout: magic `JTSP` (4), versi `0x01` (1), panjang invoice (2, LE), invoice kanonik, tanda tangan buyer (64), lalu dua entri masing-masing `panjang (1) ‖ byte entri dengan marker (136/168) ‖ flag (1)`. Flag `1` diikuti posisi papan `txid (32, urutan tampilan) ‖ tinggi (4) ‖ indeks tx (4) ‖ indeks output (4)`; flag `0` untuk entri yang hanya ditawarkan (tidak di papan). Commitment yang sama ditolak (`NotDoubleSigned`): itu re-post, bukan penipuan.

## Commitment financier (HNK-05) — **diimplementasikan** (`6b5c343`)
`financier_commitment = BLAKE2b-256(financier_pk ‖ salt)` (output 32 byte, tanpa personalisasi, sesuai spesifikasi entri). `salt` 32 byte dipegang financier dan supplier (dibagikan off-chain bersama `financier_pk`), jadi papan tidak membuka siapa financier-nya.

**Test vector:** `financier_pk` 32×`0x03`, `salt` 32×`0x04` → `c72255e7b3f5bd4f2e652cf71eceb37d0b35074f2bb11c4a788ce2282d982b3a` (dicek silang dengan Python `hashlib.blake2b(digest_size=32)`).

## Memo kuitansi (HNK-05, HNK-06) — **diimplementasikan** (`6b5c343`)
Kuitansi ada di memo output shielded yang membawa uangnya, jadi hanya penerima yang bisa membacanya. Byte pertama memo `0xFF` (ZIP-302).

| Offset | Field | Ukuran |
|---|---|---|
| 0 | prefix memo `0xFF` | 1 |
| 1 | magic `JTR1` | 4 |
| 5 | tipe (`0x01` advance: financier → supplier; `0x02` pelunasan: buyer → financier) | 1 |
| 6 | `N` | 32 |
| 38 | `amount_zat` (u64 LE, > 0) | 8 |
| 46 | tanggal (hari sejak epoch, u32 LE) | 4 |
| 50 | `signer_pk` (Ed25519) | 32 |
| 82 | tanda tangan signer atas byte 1–81 | 64 |
| **Total** | | **146 byte** (batas memo 512) |

Decoder ketat (marker, magic, tipe, nominal 0, input terpotong, dan padding bukan nol ditolak). Verifikasi supplier:
1. `signer_pk` sama dengan `financier_pk` yang disepakati (pembukaan commitment). Kalau beda: `UnexpectedSigner`.
2. Tanda tangan valid (`verify_strict`).
3. `amount_zat` sama dengan nilai output yang membawa memo.

Tipe `0x02` (pelunasan) dibuat oleh buyer di web app dan dimasukkan ke URI ZIP-321 (HNK-06, `aff284d`; sejak HNK-19 memo-nya dua item, lihat bagian Memo dua item): `zcash:<alamat financier>?amount=<nominal>&memo=<base64url>`. Nominal, N, dan alamat diambil dari surat pengalihan. Financier mencocokkan pembayaran ke N: kuitansi tipe `0x02`, N sama, ditandatangani `buyer_pk` dari invoice, nominal = nilai output. Status watchdog: `Unpaid` / `Pending` / `Partial` / `Claimed` / `Settled` / `Disputed` / `Overdue`; `Settled` hanya dari pembayaran valid yang sudah ditambang.

## Entri `settled` dua tanda tangan (HNK-19.T4, D-19, DEV-08) — **diimplementasikan** (`f07787b`)
Menggantikan layout satu tanda tangan dari `aff284d`; layout lama tidak lagi di-decode.

**Dokumen pelunasan (privat):** magic `JTSS` (4), versi `0x01` (1), N (32), `amount_zat` (8, LE), `due_date` (4, LE). Disegel dengan policy Buyer lalu Financier. Seal buyer = klaim "sudah bayar" (flag 0). Seal financier = "sudah terima", flag `0x01` tepat waktu atau `0x02` terlambat (tanggal blok pembayaran yang menutup jumlah ≤ `due_date`).

**Entri publik di papan (167 byte):**

| Offset | Field | Ukuran |
|---|---|---|
| 0 | prefix memo `0xFF` | 1 |
| 1 | magic `JTS1` | 4 |
| 5 | tipe `0x02` | 1 |
| 6 | `settled_tag = BLAKE2b-256(N ‖ "settled")` | 32 |
| 38 | flag financier (`0x01` / `0x02`) | 1 |
| 39 | tanda tangan seal buyer | 64 |
| 103 | tanda tangan seal financier | 64 |

Tidak ada N, commitment, atau bucket, jadi orang luar tidak bisa menautkannya ke entri register. Pemegang N membangun ulang kedua seal dari dokumen pelunasan dan memverifikasinya dengan `buyer_pk` (invoice) dan `financier_pk` (surat pengalihan). `lookup` hanya memakai entri register, jadi entri `settled` tidak pernah dihitung sebagai registrasi atau konflik.

**Test vector `settled_tag`:** N 32×`0x07` → `745dd5c7a8c41316f9c712e9aef7e458ece60e0a3ef1914ad47bee144c13a494`.

## Seal (Jitsuin Seal, HNK-19.T1, D-21) — **diimplementasikan** (`b007a26`)
Desain: [[Desain Jitsuin Seal]]. 200 byte, tanpa marker memo:

| Offset | Field | Ukuran |
|---|---|---|
| 0 | magic `JTL1` | 4 |
| 4 | jenis dokumen (`0x01` invoice, `0x02` surat pengalihan, `0x03` pelunasan) | 1 |
| 5 | id dokumen = N | 32 |
| 37 | hash dokumen = `BLAKE2b-256("JitsuinDocument_", byte kanonik)` | 32 |
| 69 | langkah (indeks di policy) | 1 |
| 70 | role (`0x01` supplier, `0x02` buyer, `0x03` financier) | 1 |
| 71 | flag (atestasi khusus role, selain itu 0) | 1 |
| 72 | hash seal sebelumnya (nol di langkah 0) | 32 |
| 104 | `signer_pk` | 32 |
| 136 | tanda tangan atas byte 0–135 | 64 |

Hash seal = `BLAKE2b-256("JitsuinSealHash_", 200 byte)`. Policy: invoice = Buyer; surat pengalihan = Supplier, Buyer, Financier; pelunasan = Buyer, Financier. Ditolak: langkah dilewati atau ditukar, rantai putus, seal untuk dokumen lain, signer yang bukan key role-nya, satu key untuk dua role (`SelfApproval`), seal melebihi policy.

## Surat pengalihan (HNK-19.T2, DEV-06) — **diimplementasikan** (`fdc399e`)
Magic `JTSA` (4), versi `0x01` (1), N (32), `amount_zat` (8, LE), `due_date` (4, LE), `financier_pk` (32), `terms_hash` (32, SHA-256 PDF surat), panjang alamat (2, LE), alamat financier (1–512 byte ASCII alfanumerik). N, nominal, dan jatuh tempo harus sama dengan invoice. Key supplier dan buyer diambil dari invoice, key financier dari surat ini.

## Memo dua item, Sign-to-Pay (HNK-19.T3, DEV-07) — **diimplementasikan** (`f9fee3e`)
Marker `0xFF`, lalu item berurutan, lalu padding nol: kuitansi `JTR1` (145 byte tanpa marker) dan/atau seal `JTL1` (200 byte). Memo berisi satu kuitansi identik byte-per-byte dengan memo kuitansi lama.
- **Advance:** kuitansi advance + seal Financier atas surat pengalihan (346 byte). Financier baru bisa membayar setelah seal Supplier dan Buyer valid (`AwaitAssignment`) dan setelah cek papan terakhir.
- **Pelunasan:** kuitansi pelunasan + seal klaim buyer atas dokumen pelunasan (346 byte; di URI ZIP-321 menjadi 462 karakter base64url).

## Bundel verifikasi (HNK-19.T6) — **diimplementasikan** (`dd23864`)
Magic `JTSB` (4), versi `0x01` (1), lalu item `tipe (1) ‖ panjang (2, LE) ‖ isi`: `1` invoice kanonik, `2` tanda tangan buyer (64), `3` surat pengalihan kanonik, `4` seal surat pengalihan (berurutan), `5` dokumen pelunasan. Bentuk teks: base64url tanpa padding. `Bundle::verify` memeriksa tanda tangan buyer, N, surat pengalihan dan rantai seal-nya, serta dokumen pelunasan. `bundle_on_board` menambahkan lookup register dan entri `settled` dua tanda tangan.

## Entri register bertag riwayat (HNK-20, DEV-10) — **diimplementasikan** (`f03cfb1`)
Tipe `0x03` = entri register dengan tag riwayat buyer. Layout sama dengan tipe `0x01` sampai `tenor_bucket` (offset 71), lalu `history_tag` (32 byte, offset 72), lalu tanda tangan supplier atas byte 1–103 (64 byte). Total **168 byte**. Tipe `0x01` tetap valid; keduanya dihitung sebagai registrasi untuk `lookup` dan deteksi pembiayaan ganda.

## Sertifikat riwayat buyer (HNK-20) — **diimplementasikan** (`f03cfb1`, `687f2b4`)
Magic `JTSH` (4), versi `0x01` (1), nomor urut (4, LE), key invoice (32), key supplier (32), N (32), `amount_zat` (8, LE), `due_date` (4, LE), key financier (32), hash sertifikat sebelumnya (32, nol untuk nomor 0), key identitas (32), tanda tangan key identitas atas byte sebelumnya (64). Total **277 byte**.
- Hash sertifikat: `BLAKE2b-256("JitsuinHistory__", 277 byte)`.
- Tag penerus: `BLAKE2b-256("JitsuinHistTag__", identity_pk ‖ hash sebelumnya)`.
- Derivasi key: `seed = BLAKE2b-256(key = master, personal = "JitsuinBuyerKey_", input)`, dengan `input` = `"identity"` atau `"invoice" ‖ nomor (u32 LE)`. Vector: master 32×`0x42`, invoice 0 → seed `b467d39acc924edc21c631f77e1f1a6781dbd254efa0cc344ab1c7beaf34ac98` (dicek silang Python).

## Item memo dana: catatan piutang dan root kewajiban (HNK-15.T2) — **diimplementasikan** (`e54ea36`)
Untuk anggota dana yang memegang viewing key akun operasional:
- **Catatan piutang `JTN1`** (48 byte tanpa marker): magic (4), N (32), nilai nominal (8, LE), jatuh tempo (4, LE). Ikut di setiap memo advance setelah kuitansi dan seal (total 394 byte).
- **Root kewajiban `JTLR`** (144 byte): magic (4), periode (4, LE), root Merkle sum tree (32), total kewajiban (8, LE), key manajer (32), tanda tangan manajer atas byte sebelumnya (64). Dikirim ke akun sendiri per periode. Root dari pihak lain diabaikan.
- **Solvabilitas:** kas (saldo watch-only) + piutang berjalan (nominal − pelunasan yang masuk untuk N itu) + piutang lewat jatuh tempo setelah potongan ≥ total di root terbaru.

## Bucket indeks (HNK-08) — **diimplementasikan** (`90a64c7`, PR #5, usulan D-27)
`discount_bucket` dan `tenor_bucket` = kelas diskon dan tenor (tanpa nominal). Diskon = (nominal − advance) / nominal dalam basis poin; tenor = hari dari advance sampai jatuh tempo.

| Kode | Diskon | Tenor |
|---|---|---|
| 0 | tidak diungkap | tidak diungkap |
| 1 | < 1% (0–99 bp) | ≤ 30 hari |
| 2 | 1–2% | 31–60 hari |
| 3 | 2–3% | 61–90 hari |
| 4 | 3–5% | 91–180 hari |
| 5 | 5–8% | 181–365 hari |
| 6 | 8–12% | — |
| 7 | ≥ 12% | — |

- Dua-duanya diisi atau `0/0` (nilai entri sebelum HNK-08). Kombinasi lain = kelas salah: entri tetap registrasi yang sah untuk `lookup`, tetapi tidak masuk indeks.
- Indeks: tiap N dihitung sekali dengan entri register pertamanya di urutan papan; entri `settled` tidak membawa kelas. Per kelas tenor: jumlah invoice, median bawah kelas diskon, kelas diskon yang punya ≥ k invoice, sisanya satu total "other".
- **k = 5** (`jitsuin_core::index::K`): kelas di bawah k tidak diberi angka. k boleh dinaikkan, tidak boleh diturunkan.

## Urutan entri (HNK-04) — **diimplementasikan** (`ef55987`)
Urutan total: (tinggi blok, indeks transaksi, indeks output). Indeks transaksi diambil dari `GetBlock` lightwalletd (SPK-08); tidak perlu tie-break tambahan. Memo hanya terbaca setelah transaksi penuh diambil (`enhance`, SPK-05). Entri ulang dengan commitment financier yang sama bukan konflik.
