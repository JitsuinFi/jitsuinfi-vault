---
tags: [architecture, security]
---

# Threat Model

**Bagian dari:** [[07 - Architecture]] · Kembali: [[START-HERE]] · Terkait: [[Arsitektur JitsuinFi]] · [[Format Data]]

> **Draf awal.** Difinalkan di HNK-11 setelah HNK-05 – HNK-07 selesai. Aturan juri: "Leaks are disqualifying." Setiap kebocoran harus punya mitigasi atau dinyatakan terang-terangan.

## Siapa melihat apa
| Pihak | Melihat | Tidak melihat |
|---|---|---|
| Publik / pengamat chain | Ada transaksi shielded; waktu dan jumlah transaksi | Isi memo, nominal, pihak |
| Pemegang viewing key papan (siapa pun) | Entri: N, commitment financier, bucket diskon/tenor, waktu | Isi invoice, identitas supplier/buyer/financier, nominal |
| Financier A | Invoice yang dibiayainya, nominal, pembayaran dari buyer | Invoice dan financier lain |
| Financier B (ditawari invoice yang sama) | Invoice itu + bukti bahwa sudah dibiayai | Siapa financier A (hanya commitment) |
| Supplier | Invoice-nya, pembayaran di muka | Financier lain |
| Buyer | Invoice yang ditandatanganinya, alamat bayar financier | Nominal pembayaran di muka |
| Operator web (Railway) | Request yang lewat backend; bisa membaca memori server | Spending key user (tidak pernah dikirim ke server) |
| Server lightwalletd | IP dan pola sync klien | Isi transaksi shielded |

## Kebocoran yang diketahui dan mitigasinya
| Kebocoran | Mitigasi | Sisa risiko |
|---|---|---|
| Metadata waktu dan jumlah entri di papan | Akui di deskripsi; entri hanya berisi data tanpa identitas | Pola aktivitas terlihat |
| Bucket indeks bisa mempersempit identitas | Tampilkan hanya bila minimal k entri per kelas | Pasar kecil = anonymity set kecil |
| QR ZIP-321 di tempat umum membuka alamat dan nominal | QR hanya dibagikan langsung ke pihak terkait | Kalau bocor, alamat dan nominal terlihat |
| IP terlihat oleh lightwalletd | Opsi Tor; dinyatakan di threat model | Default tanpa Tor |
| Input transparan membocorkan pengirim | Tolak atau tandai input transparan | Pengguna yang memaksa tetap bocor |
| Invoice fiktif (supplier dan buyer bersekongkol) | Due diligence financier; audit sampel (JitsuinFi Vault) | Tidak bisa dideteksi registry |
| Tidak ada smart contract: pelunasan bergantung pada buyer membayar ke alamat yang benar | Surat pengalihan bertanda tangan buyer | Penegakan lebih lemah dari smart contract (contoh: AVAL di Casper) |
| Mode confidential (buyer tidak diberi tahu) | Opsi terpisah dengan peringatan risiko | Financier harus percaya supplier meneruskan pembayaran |
| Viewing key yang dibagikan tidak bisa dicabut | Akun ZIP-32 terpisah per peran/periode | Pemegang lama tetap bisa melihat data lama |
| Operator web bisa membaca memori server | Spending key tetap di sisi user/CLI; server hanya relay | Kalau key ditaruh di server, operator bisa melihatnya |
