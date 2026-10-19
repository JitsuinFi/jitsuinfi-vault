---
tags: [flow, dfd]
status: DRAF
updated: 2026-10-20
---

# DFD-2.2 - Penerbitan dan Tanda Tangan Invoice

**Bagian dari:** [[08 - FlowDiagrams]] · Legenda: [[FD-00 - Arsitektur Target dan Legenda]] · Induk: [[DFD-1 - Proses Utama]] · Sequence: [[SEQ-01 - Supplier]] · [[SEQ-02 - Buyer]]

Proses 2.0 dirinci: buyer membagikan key invoice, supplier menyiapkan key per invoice dan invoice kanonik, buyer memeriksa dan menandatanganinya. Dasar: `src/pages/supplier.ts`, `src/pages/buyer.ts`, `src/lib/core.ts`, wasm `buyerKeys`, `publicKey`, `documentHash`, `invoiceEncode`, `invoiceDecode`, `buyerSignInvoice`, `bundleBuild`; format di [[Format Data]].

Satu jalur = satu proses. Kotak bertanda `*` adalah entitas atau penyimpanan yang sama, digambar ulang supaya garis tidak bersilang. Proses bergaris penuh = ADA atau PARSIAL (rinciannya di kolom Status), kuning putus-putus = USULAN.

![DFD-2.2](assets/dfd-2-2.svg)

```plantuml
@startuml dfd-2-2
!include dfd-style.iuml
left to right direction
skinparam nodesep 12
skinparam ranksep 35
rectangle "Supplier *" <<entity>> as S_8
rectangle "D4 | Dokumen deal\n(salinan tiap pihak) *" <<store>> as D4_8
rectangle "D7 | Kotak surat\nterenkripsi *" <<storeproposal>> as D7_8
rectangle "D7 | Kotak surat\nterenkripsi *" <<storeproposal>> as D7_7
rectangle "D19 | Kontak rekan\n(mailbox_pk) *" <<storeproposal>> as D19_7
rectangle "D3 | Key sesi\n(memori tab) *" <<store>> as D3_7
rectangle "D4 | Dokumen deal\n(salinan tiap pihak) *" <<store>> as D4_7
rectangle "Buyer *" <<entity>> as B_7
rectangle "Buyer *" <<entity>> as B_6
rectangle "D4 | Dokumen deal\n(salinan tiap pihak) *" <<store>> as D4_6
rectangle "D3 | Key sesi\n(memori tab) *" <<store>> as D3_6
rectangle "D7 | Kotak surat\nterenkripsi *" <<storeproposal>> as D7_6
rectangle "D7 | Kotak surat\nterenkripsi *" <<storeproposal>> as D7_5
rectangle "D19 | Kontak rekan\n(mailbox_pk) *" <<storeproposal>> as D19_5
rectangle "D4 | Dokumen deal\n(salinan tiap pihak) *" <<store>> as D4_5
rectangle "D4 | Dokumen deal\n(salinan tiap pihak) *" <<store>> as D4_4
rectangle "D3 | Key sesi\n(memori tab) *" <<store>> as D3_4
rectangle "D7 | Kotak surat\nterenkripsi *" <<storeproposal>> as D7_4
rectangle "Supplier *" <<entity>> as S_4
rectangle "D4 | Dokumen deal\n(salinan tiap pihak)" <<store>> as D4_3
rectangle "Supplier *" <<entity>> as S_3
rectangle "D3 | Key sesi\n(memori tab) *" <<store>> as D3_2
rectangle "Supplier" <<entity>> as S_2
rectangle "D7 | Kotak surat\nterenkripsi" <<storeproposal>> as D7_1
rectangle "D19 | Kontak rekan\n(mailbox_pk)" <<storeproposal>> as D19_1
rectangle "D3 | Key sesi\n(memori tab)" <<store>> as D3_1
rectangle "Buyer" <<entity>> as B_1
rectangle "**2.8**\nCek tanda tangan\nbuyer" <<process>> as P8
rectangle "**2.7**\nTanda tangani\ninvoice" <<process>> as P7
rectangle "**2.6**\nPeriksa invoice" <<process>> as P6
rectangle "**2.5**\nKirim invoice\nke buyer" <<proposal>> as P5
rectangle "**2.4**\nSusun invoice\nkanonik dan N" <<process>> as P4
rectangle "**2.3**\nHash file syarat" <<process>> as P3
rectangle "**2.2**\nSiapkan key\nper invoice" <<process>> as P2
rectangle "**2.1**\nBagikan key\ninvoice (buyer)" <<process>> as P1
rectangle "F2.01 bagikan key\ninvoice k" <<flow>> as f_F2_01
rectangle "F2.02 invoice_pk(k)" <<flow>> as f_F2_02
rectangle "F2.03 mailbox_pk supplier" <<flow>> as f_F2_03
rectangle "F2.04 invoice_pk(k)" <<flow>> as f_F2_04
rectangle "F2.05 invoice_id\n(unik per supplier)" <<flow>> as f_F2_05
rectangle "F2.06 master supplier\n(P-03)" <<flow>> as f_F2_06
rectangle "F2.07 key per invoice" <<flow>> as f_F2_07
rectangle "F2.08 backup JSON\n(saat ini)" <<flow>> as f_F2_08
rectangle "F2.09 file syarat (PDF)" <<flow>> as f_F2_09
rectangle "F2.10 terms_hash" <<flow>> as f_F2_10
rectangle "F2.11 nominal (ZEC),\ntanggal" <<flow>> as f_F2_11
rectangle "F2.12 invoice_pk(k)\ndari buyer" <<flow>> as f_F2_12
rectangle "F2.13 supplier_pk" <<flow>> as f_F2_13
rectangle "F2.14 terms_hash" <<flow>> as f_F2_14
rectangle "F2.15 invoice JTSI + N" <<flow>> as f_F2_15
rectangle "F2.16 invoice + PDF syarat" <<flow>> as f_F2_16
rectangle "F2.17 mailbox_pk buyer" <<flow>> as f_F2_17
rectangle "F2.18 ciphertext\ninvoice + PDF" <<flow>> as f_F2_18
rectangle "F2.19 invoice + PDF" <<flow>> as f_F2_19
rectangle "F2.20 invoice_pk(k)" <<flow>> as f_F2_20
rectangle "F2.21 invoice (salinan buyer)" <<flow>> as f_F2_21
rectangle "F2.22 isi invoice,\nhasil cek hash" <<flow>> as f_F2_22
rectangle "F2.23 keputusan setuju" <<flow>> as f_F2_23
rectangle "F2.24 invoice" <<flow>> as f_F2_24
rectangle "F2.25 key invoice buyer" <<flow>> as f_F2_25
rectangle "F2.26 mailbox_pk supplier" <<flow>> as f_F2_26
rectangle "F2.27 sig_buyer" <<flow>> as f_F2_27
rectangle "F2.28 sig_buyer" <<flow>> as f_F2_28
rectangle "F2.29 invoice" <<flow>> as f_F2_29
rectangle "F2.30 invoice + sig valid" <<flow>> as f_F2_30
rectangle "F2.31 status tanda tangan" <<flow>> as f_F2_31
B_1 -- f_F2_01
f_F2_01 --> P1
P1 <-- f_F2_02
f_F2_02 -- D3_1
P1 <-- f_F2_03
f_F2_03 -- D19_1
P1 -- f_F2_04
f_F2_04 --> D7_1
S_2 -- f_F2_05
f_F2_05 --> P2
P2 <-- f_F2_06
f_F2_06 -- D3_2
P2 -- f_F2_07
f_F2_07 --> D3_2
S_2 <-- f_F2_08
f_F2_08 -- P2
S_3 -- f_F2_09
f_F2_09 --> P3
P3 -- f_F2_10
f_F2_10 --> D4_3
S_4 -- f_F2_11
f_F2_11 --> P4
P4 <-- f_F2_12
f_F2_12 -- D7_4
P4 <-- f_F2_13
f_F2_13 -- D3_4
P4 <-- f_F2_14
f_F2_14 -- D4_4
P4 -- f_F2_15
f_F2_15 --> D4_4
P5 <-- f_F2_16
f_F2_16 -- D4_5
P5 <-- f_F2_17
f_F2_17 -- D19_5
P5 -- f_F2_18
f_F2_18 --> D7_5
P6 <-- f_F2_19
f_F2_19 -- D7_6
P6 <-- f_F2_20
f_F2_20 -- D3_6
P6 -- f_F2_21
f_F2_21 --> D4_6
B_6 <-- f_F2_22
f_F2_22 -- P6
B_7 -- f_F2_23
f_F2_23 --> P7
P7 <-- f_F2_24
f_F2_24 -- D4_7
P7 <-- f_F2_25
f_F2_25 -- D3_7
P7 <-- f_F2_26
f_F2_26 -- D19_7
P7 -- f_F2_27
f_F2_27 --> D7_7
P8 <-- f_F2_28
f_F2_28 -- D7_8
P8 <-- f_F2_29
f_F2_29 -- D4_8
P8 -- f_F2_30
f_F2_30 --> D4_8
S_8 <-- f_F2_31
f_F2_31 -- P8
rectangle " " <<spacer>> as sp_P5_a
rectangle " " <<spacer>> as sp_P5_b
sp_P5_a -[hidden]- sp_P5_b
sp_P5_b -[hidden]- P5
@enduml
```

## Proses

| Proses | Isi | Status | Kode / item |
|---|---|---|---|
| 2.1 Bagikan key invoice | Buyer memberi `invoice_pk(k)` untuk invoice berikutnya ke supplier | ADA (salin) / USULAN (relay) | wasm `buyerKeys` |
| 2.2 Siapkan key per invoice | Sekarang: 32 byte dari `crypto.getRandomValues` di JS + unduh backup JSON plaintext (TM #10). Target: keyed BLAKE2b dengan personalisasi sendiri dan input unik per invoice (bukan `invoice_id` polos); `invoice_id` dipakai ulang ditolak | ADA (akan diganti) / USULAN P-03 | `src/lib/core.ts`, `supplier.ts` |
| 2.3 Hash file syarat | SHA-256 file di browser; file tidak diunggah ke server | ADA | wasm `documentHash` |
| 2.4 Susun invoice kanonik dan N | Nominal diisi dalam ZEC lalu dikonversi ke zat; JTSI dengan dekoder ketat; N = BLAKE2b-256("JitsuinNullifier", byte kanonik) | ADA | wasm `invoiceEncode`, `invoiceDecode` |
| 2.5 Kirim invoice ke buyer | Invoice + PDF syarat lewat kotak surat buyer; sekarang salin-tempel dan PDF dikirim di luar sistem | USULAN | P-04 |
| 2.6 Periksa invoice | Decode dan tampilkan; hash PDF syarat dibandingkan dengan `terms_hash` | PARSIAL: decode ADA; input file dan cek hash belum ada di layar Buyer | wasm `invoiceDecode`, `documentHash` |
| 2.7 Tanda tangani invoice | Ed25519 atas byte kanonik dengan key invoice buyer; wasm menolak invoice yang `buyer_pk`-nya bukan `invoice_pk(k)` | ADA | wasm `buyerSignInvoice` |
| 2.8 Cek tanda tangan buyer | `bundleBuild` memeriksa tanda tangan (`verify_strict`) dan gagal bila tidak valid | PARSIAL: fungsi ADA; kartu cek di layar Supplier belum ada | wasm `bundleBuild` |

## Aliran data

| Aliran | Dari | Ke | Data |
|---|---|---|---|
| F2.01 | Buyer | 2.1 Bagikan key invoice (buyer) | bagikan key invoice k |
| F2.02 | D3 Key sesi (memori tab) | 2.1 Bagikan key invoice (buyer) | invoice_pk(k) |
| F2.03 | D19 Kontak rekan (mailbox_pk) | 2.1 Bagikan key invoice (buyer) | mailbox_pk supplier |
| F2.04 | 2.1 Bagikan key invoice (buyer) | D7 Kotak surat terenkripsi | invoice_pk(k) |
| F2.05 | Supplier | 2.2 Siapkan key per invoice | invoice_id (unik per supplier) |
| F2.06 | D3 Key sesi (memori tab) | 2.2 Siapkan key per invoice | master supplier (P-03) |
| F2.07 | 2.2 Siapkan key per invoice | D3 Key sesi (memori tab) | key per invoice |
| F2.08 | 2.2 Siapkan key per invoice | Supplier | backup JSON (saat ini) |
| F2.09 | Supplier | 2.3 Hash file syarat | file syarat (PDF) |
| F2.10 | 2.3 Hash file syarat | D4 Dokumen deal (salinan tiap pihak) | terms_hash |
| F2.11 | Supplier | 2.4 Susun invoice kanonik dan N | nominal (ZEC), tanggal |
| F2.12 | D7 Kotak surat terenkripsi | 2.4 Susun invoice kanonik dan N | invoice_pk(k) dari buyer |
| F2.13 | D3 Key sesi (memori tab) | 2.4 Susun invoice kanonik dan N | supplier_pk |
| F2.14 | D4 Dokumen deal (salinan tiap pihak) | 2.4 Susun invoice kanonik dan N | terms_hash |
| F2.15 | 2.4 Susun invoice kanonik dan N | D4 Dokumen deal (salinan tiap pihak) | invoice JTSI + N |
| F2.16 | D4 Dokumen deal (salinan tiap pihak) | 2.5 Kirim invoice ke buyer | invoice + PDF syarat |
| F2.17 | D19 Kontak rekan (mailbox_pk) | 2.5 Kirim invoice ke buyer | mailbox_pk buyer |
| F2.18 | 2.5 Kirim invoice ke buyer | D7 Kotak surat terenkripsi | ciphertext invoice + PDF |
| F2.19 | D7 Kotak surat terenkripsi | 2.6 Periksa invoice | invoice + PDF |
| F2.20 | D3 Key sesi (memori tab) | 2.6 Periksa invoice | invoice_pk(k) |
| F2.21 | 2.6 Periksa invoice | D4 Dokumen deal (salinan tiap pihak) | invoice (salinan buyer) |
| F2.22 | 2.6 Periksa invoice | Buyer | isi invoice, hasil cek hash |
| F2.23 | Buyer | 2.7 Tanda tangani invoice | keputusan setuju |
| F2.24 | D4 Dokumen deal (salinan tiap pihak) | 2.7 Tanda tangani invoice | invoice |
| F2.25 | D3 Key sesi (memori tab) | 2.7 Tanda tangani invoice | key invoice buyer |
| F2.26 | D19 Kontak rekan (mailbox_pk) | 2.7 Tanda tangani invoice | mailbox_pk supplier |
| F2.27 | 2.7 Tanda tangani invoice | D7 Kotak surat terenkripsi | sig_buyer |
| F2.28 | D7 Kotak surat terenkripsi | 2.8 Cek tanda tangan buyer | sig_buyer |
| F2.29 | D4 Dokumen deal (salinan tiap pihak) | 2.8 Cek tanda tangan buyer | invoice |
| F2.30 | 2.8 Cek tanda tangan buyer | D4 Dokumen deal (salinan tiap pihak) | invoice + sig valid |
| F2.31 | 2.8 Cek tanda tangan buyer | Supplier | status tanda tangan |
