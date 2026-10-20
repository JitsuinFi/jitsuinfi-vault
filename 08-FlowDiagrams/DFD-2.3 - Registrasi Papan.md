---
tags: [flow, dfd]
status: DRAF
updated: 2026-10-20
---

# DFD-2.3 - Registrasi Papan

**Bagian dari:** [[08 - FlowDiagrams]] · Legenda: [[FD-00 - Arsitektur Target dan Legenda]] · Induk: [[DFD-1 - Proses Utama]] · Sequence: [[SEQ-03 - Financier]] · [[SEQ-01 - Supplier]]

Proses 3.0 dirinci: dari penawaran sampai entri financier menjadi entri valid pertama untuk N dan terkonfirmasi. Urutan kerja: komitmen dan surat (3.2, 4.1) sebelum `Flow::new` (3.3), cek riwayat (6.x) sebelum posting entri bertag (3.8). Pemindaian papan (3.4) adalah satu fungsi yang dipanggil ulang oleh setiap pengecekan (3.5, 3.9, 4.5, 5.4, 6.5, 7.x); hasilnya digambar sebagai D10. Dasar: `jitsuin-flow::financier` (`Deal`, `Flow`, `check`, `register`, `wait_for_confirmation`), `jitsuin-board` (`scan`, `collect`, `lookup`, `lwd`), wasm `supplierRegisterEntry`, `supplierRegisterHistoryEntry`, `jitsuin-core::index::classes_for`.

Satu jalur = satu proses. Kotak bertanda `*` adalah entitas atau penyimpanan yang sama, digambar ulang supaya garis tidak bersilang. Proses bergaris penuh = ADA atau PARSIAL (rinciannya di kolom Status), kuning putus-putus = USULAN.

![DFD-2.3](assets/dfd-2-3.svg)

```plantuml
@startuml dfd-2-3
!include dfd-style.iuml
left to right direction
skinparam nodesep 12
skinparam ranksep 35
rectangle "Jaringan Zcash\n(lightwalletd) *" <<entity>> as Z_9
rectangle "D4 | Dokumen deal\n(salinan tiap pihak) *" <<store>> as D4_9
rectangle "D10 | Hasil pindai papan\n(node, memori) *" <<store>> as D10_9
rectangle "D11 | Status deal\n(node, memori) *" <<store>> as D11_9
rectangle "D1 | Papan registry *" <<store>> as D1_8
rectangle "D2 | Node financier\n(wallet, key,\nwatch-only papan) *" <<store>> as D2_8
rectangle "D11 | Status deal\n(node, memori) *" <<store>> as D11_8
rectangle "Financier *" <<entity>> as F_7
rectangle "D11 | Status deal\n(node, memori) *" <<store>> as D11_7
rectangle "D4 | Dokumen deal\n(salinan tiap pihak) *" <<store>> as D4_7
rectangle "D7 | Kotak surat\nterenkripsi *" <<storeproposal>> as D7_7
rectangle "D4 | Dokumen deal\n(salinan tiap pihak) *" <<store>> as D4_6
rectangle "D3 | Key sesi\n(memori tab)" <<store>> as D3_6
rectangle "Supplier *" <<entity>> as S_6
rectangle "D7 | Kotak surat\nterenkripsi *" <<storeproposal>> as D7_6
rectangle "Financier *" <<entity>> as F_5
rectangle "Jaringan Zcash\n(lightwalletd) *" <<entity>> as Z_5
rectangle "D11 | Status deal\n(node, memori) *" <<store>> as D11_5
rectangle "D4 | Dokumen deal\n(salinan tiap pihak) *" <<store>> as D4_5
rectangle "D10 | Hasil pindai papan\n(node, memori) *" <<store>> as D10_5
rectangle "D10 | Hasil pindai papan\n(node, memori)" <<store>> as D10_4
rectangle "Jaringan Zcash\n(lightwalletd)" <<entity>> as Z_4
rectangle "D1 | Papan registry" <<store>> as D1_4
rectangle "D2 | Node financier\n(wallet, key,\nwatch-only papan) *" <<store>> as D2_4
rectangle "D11 | Status deal\n(node, memori)" <<store>> as D11_3
rectangle "D4 | Dokumen deal\n(salinan tiap pihak) *" <<store>> as D4_3
rectangle "D7 | Kotak surat\nterenkripsi" <<storeproposal>> as D7_2
rectangle "D19 | Kontak rekan\n(mailbox_pk)" <<storeproposal>> as D19_2
rectangle "D4 | Dokumen deal\n(salinan tiap pihak) *" <<store>> as D4_2
rectangle "D2 | Node financier\n(wallet, key,\nwatch-only papan)" <<store>> as D2_2
rectangle "D4 | Dokumen deal\n(salinan tiap pihak)" <<store>> as D4_1
rectangle "Financier" <<entity>> as F_1
rectangle "Supplier" <<entity>> as S_1
rectangle "**3.9**\nTunggu konfirmasi" <<process>> as P9
rectangle "**3.8**\nPosting entri" <<process>> as P8
rectangle "**3.7**\nPeriksa entri" <<process>> as P7
rectangle "**3.6**\nTanda tangani entri\n(supplier)" <<process>> as P6
rectangle "**3.5**\nLookup N" <<process>> as P5
rectangle "**3.4**\nPindai papan" <<process>> as P4
rectangle "**3.3**\nMulai alur deal\n(Flow::new)" <<process>> as P3
rectangle "**3.2**\nBuat komitmen\ndan kelas" <<process>> as P2
rectangle "**3.1**\nTerima penawaran" <<proposal>> as P1
rectangle "F3.01 penawaran: invoice, sig,\nalamat, advance" <<flow>> as f_F3_01
rectangle "F3.02 syarat: advance,\nkonfirmasi" <<flow>> as f_F3_02
rectangle "F3.03 tanda tangan buyer\ntidak valid (tolak)" <<flow>> as f_F3_03
rectangle "F3.04 deal" <<flow>> as f_F3_04
rectangle "F3.05 financier_pk" <<flow>> as f_F3_05
rectangle "F3.06 nominal, advance,\ntanggal" <<flow>> as f_F3_06
rectangle "F3.07 mailbox_pk supplier" <<flow>> as f_F3_07
rectangle "F3.08 komitmen + salt,\nkelas" <<flow>> as f_F3_08
rectangle "F3.09 pembuka komitmen,\nkelas" <<flow>> as f_F3_09
rectangle "F3.10 invoice, surat, komitmen, alamat,\nadvance, min_confirmations, tag" <<flow>> as f_F3_10
rectangle "F3.11 Check" <<flow>> as f_F3_11
rectangle "F3.12 wallet watch-only\npapan" <<flow>> as f_F3_12
rectangle "F3.13 memo papan\n(lewat UFVK)" <<flow>> as f_F3_13
rectangle "F3.14 blok, tx penuh,\nurutan txid" <<flow>> as f_F3_14
rectangle "F3.15 records, settled,\nrejected" <<flow>> as f_F3_15
rectangle "F3.16 records" <<flow>> as f_F3_16
rectangle "F3.17 N, supplier_pk, komitmen\nsendiri, min_confirmations" <<flow>> as f_F3_17
rectangle "F3.18 state" <<flow>> as f_F3_18
rectangle "F3.19 tinggi tip" <<flow>> as f_F3_19
rectangle "F3.20 AwaitSupplierSignature /\nAwaitConfirmation /\nAwaitAssignment / Stopped" <<flow>> as f_F3_20
rectangle "F3.21 bebas / sudah\ndibiayai" <<flow>> as f_F3_21
rectangle "F3.22 pembuka komitmen, kelas,\nhistory_tag atau sertifikat k" <<flow>> as f_F3_22
rectangle "F3.23 rincian entri: N,\nfinancier, kelas" <<flow>> as f_F3_23
rectangle "F3.24 keputusan setuju" <<flow>> as f_F3_24
rectangle "F3.25 key per invoice" <<flow>> as f_F3_25
rectangle "F3.26 invoice (salinan\nsupplier)" <<flow>> as f_F3_26
rectangle "F3.27 entri bertanda\ntangan" <<flow>> as f_F3_27
rectangle "F3.28 entri" <<flow>> as f_F3_28
rectangle "F3.29 invoice, komitmen,\ntag" <<flow>> as f_F3_29
rectangle "F3.30 Register" <<flow>> as f_F3_30
rectangle "F3.31 EntryMismatch:\nentri ditolak" <<flow>> as f_F3_31
rectangle "F3.32 entri yang ditawarkan\n(USULAN P-14)" <<flow>> as f_F3_32
rectangle "F3.33 entri" <<flow>> as f_F3_33
rectangle "F3.34 wallet\n(spending key)" <<flow>> as f_F3_34
rectangle "F3.35 entri register\n(10 000 zat + fee)" <<flow>> as f_F3_35
rectangle "F3.36 AwaitConfirmation\n+ txid" <<flow>> as f_F3_36
rectangle "F3.37 AwaitConfirmation\n+ txid" <<flow>> as f_F3_37
rectangle "F3.38 records" <<flow>> as f_F3_38
rectangle "F3.39 N, supplier_pk, komitmen,\nmin_confirmations" <<flow>> as f_F3_39
rectangle "F3.40 tinggi tip" <<flow>> as f_F3_40
rectangle "F3.41 AwaitAssignment\n/ Stopped" <<flow>> as f_F3_41
rectangle "F3.42 entri\nterkonfirmasi" <<flow>> as f_F3_42
S_1 -- f_F3_01
f_F3_01 --> P1
F_1 -- f_F3_02
f_F3_02 --> P1
F_1 <-- f_F3_03
f_F3_03 -- P1
P1 -- f_F3_04
f_F3_04 --> D4_1
P2 <-- f_F3_05
f_F3_05 -- D2_2
P2 <-- f_F3_06
f_F3_06 -- D4_2
P2 <-- f_F3_07
f_F3_07 -- D19_2
P2 -- f_F3_08
f_F3_08 --> D4_2
P2 -- f_F3_09
f_F3_09 --> D7_2
P3 <-- f_F3_10
f_F3_10 -- D4_3
P3 -- f_F3_11
f_F3_11 --> D11_3
P4 <-- f_F3_12
f_F3_12 -- D2_4
P4 <-- f_F3_13
f_F3_13 -- D1_4
Z_4 -- f_F3_14
f_F3_14 --> P4
P4 -- f_F3_15
f_F3_15 --> D10_4
P5 <-- f_F3_16
f_F3_16 -- D10_5
P5 <-- f_F3_17
f_F3_17 -- D4_5
P5 <-- f_F3_18
f_F3_18 -- D11_5
Z_5 -- f_F3_19
f_F3_19 --> P5
P5 -- f_F3_20
f_F3_20 --> D11_5
F_5 <-- f_F3_21
f_F3_21 -- P5
P6 <-- f_F3_22
f_F3_22 -- D7_6
S_6 <-- f_F3_23
f_F3_23 -- P6
S_6 -- f_F3_24
f_F3_24 --> P6
P6 <-- f_F3_25
f_F3_25 -- D3_6
P6 <-- f_F3_26
f_F3_26 -- D4_6
P6 -- f_F3_27
f_F3_27 --> D7_6
P7 <-- f_F3_28
f_F3_28 -- D7_7
P7 <-- f_F3_29
f_F3_29 -- D4_7
P7 -- f_F3_30
f_F3_30 --> D11_7
F_7 <-- f_F3_31
f_F3_31 -- P7
P7 -- f_F3_32
f_F3_32 --> D4_7
P8 <-- f_F3_33
f_F3_33 -- D11_8
P8 <-- f_F3_34
f_F3_34 -- D2_8
P8 -- f_F3_35
f_F3_35 --> D1_8
P8 -- f_F3_36
f_F3_36 --> D11_8
P9 <-- f_F3_37
f_F3_37 -- D11_9
P9 <-- f_F3_38
f_F3_38 -- D10_9
P9 <-- f_F3_39
f_F3_39 -- D4_9
Z_9 -- f_F3_40
f_F3_40 --> P9
P9 -- f_F3_41
f_F3_41 --> D11_9
P9 -- f_F3_42
f_F3_42 --> D4_9
rectangle " " <<spacer>> as sp_P2_a
rectangle " " <<spacer>> as sp_P2_b
sp_P2_a -[hidden]- sp_P2_b
sp_P2_b -[hidden]- P2
rectangle " " <<spacer>> as sp_P3_a
rectangle " " <<spacer>> as sp_P3_b
sp_P3_a -[hidden]- sp_P3_b
sp_P3_b -[hidden]- P3
rectangle " " <<spacer>> as sp_P8_a
rectangle " " <<spacer>> as sp_P8_b
sp_P8_a -[hidden]- sp_P8_b
sp_P8_b -[hidden]- P8
@enduml
```

## Proses

| Proses | Isi | Status | Kode / item |
|---|---|---|---|
| 3.1 Terima penawaran | Supplier mengirim invoice + tanda tangan buyer + alamat advance; financier menetapkan advance dan `min_confirmations` ≥ 1; tanda tangan buyer diperiksa (`bundleBuild`) sebelum deal disimpan, karena `Deal` dan `Flow` sendiri tidak memeriksanya | USULAN (alur relay); `Deal` ADA | `financier::Deal`, P-04 |
| 3.2 Buat komitmen dan kelas | `financier_commitment = BLAKE2b(financier_pk ‖ salt)`; salt diturunkan dari key financier dan N (`commitment_opening`, DEV-14), jadi retry memberi komitmen yang sama; kelas dari `deal_classes(invoice, advance, tanggal advance)` (0/0 bila tidak cocok kelas mana pun), `check_entry` menolak kelas yang berbeda | PARSIAL: core, flow, wasm ADA (HNK-27.T1 – T2); API node yang memanggilnya USULAN (HNK-26) | `commitment_opening`, `deal_classes`, wasm `financierCommitment` |
| 3.3 Mulai alur deal | `Flow::new` memeriksa `min_confirmations` ≥ 1, advance > 0, alamat tidak kosong, dan surat milik invoice (`assignment.verify(&invoice, &[])`) | ADA | `Flow::new` |
| 3.4 Pindai papan | `sync`, `enhance`, `list_tx` wallet watch-only di node; `block_txids` per tinggi; `collect`, urut (tinggi, indeks tx, indeks output). Dipanggil ulang setiap pengecekan; tx yang belum tertambang dilewati | ADA | `jitsuin_board::scan` |
| 3.5 Lookup N | Entri valid pertama menang; tanda tangan tidak valid diabaikan; komitmen sendiri: lanjut ke `AwaitConfirmation`/`AwaitAssignment`; komitmen lain: `AlreadyFinanced`; lebih dari satu komitmen: `DoubleFinanced` | ADA | `lookup`, `Flow::on_board` |
| 3.6 Tanda tangani entri | Entri `0x01` atau `0x03` dengan key per invoice supplier dan kelas dari financier; `0x03` dari sertifikat k atau cukup `history_tag` 32 byte (supplier tidak perlu sertifikat k) | PARSIAL (wasm ADA, HNK-27.T2 dan T8; layar belum) | wasm `supplierRegisterEntry`, `supplierRegisterHistoryEntry`, `supplierRegisterTaggedEntry` |
| 3.7 Periksa entri | Jenis register, N, komitmen, tag riwayat (bila deal punya tag; entri bertag tetap diterima bila deal tanpa tag), kelas, tanda tangan supplier. Ditolak: `EntryMismatch`, state tetap. Kode tidak menyimpan entri yang ditawarkan setelah `Register` | ADA (penyimpanan entri untuk bukti USULAN P-14) | `Flow::check_entry` |
| 3.8 Posting entri | 10 000 zat ke alamat papan + fee ZIP-317. Tepat sebelum posting papan dicek sekali lagi (`BoardChecked` diterima di `Register`: konflik = `Stopped`, entri sendiri yang sudah tertambang diikuti), lalu `sent_entry` mencari entri yang sudah terkirim supaya crash tidak membuat posting ganda | ADA (HNK-27.T5) | `Financier::register`, `sent_entry` |
| 3.9 Tunggu konfirmasi | Ulangi 3.4 + lookup sampai konfirmasi ≥ minimum; entri hilang saat scan kembali ke `AwaitConfirmation`; konflik baru `Stopped`; `Error::Timeout` | ADA | `wait_for_confirmation` |

## Aliran data

| Aliran | Dari | Ke | Data |
|---|---|---|---|
| F3.01 | Supplier | 3.1 Terima penawaran | penawaran: invoice, sig, alamat, advance |
| F3.02 | Financier | 3.1 Terima penawaran | syarat: advance, konfirmasi |
| F3.03 | 3.1 Terima penawaran | Financier | tanda tangan buyer tidak valid (tolak) |
| F3.04 | 3.1 Terima penawaran | D4 Dokumen deal (salinan tiap pihak) | deal |
| F3.05 | D2 Node financier (wallet, key, watch-only papan) | 3.2 Buat komitmen dan kelas | financier_pk |
| F3.06 | D4 Dokumen deal (salinan tiap pihak) | 3.2 Buat komitmen dan kelas | nominal, advance, tanggal |
| F3.07 | D19 Kontak rekan (mailbox_pk) | 3.2 Buat komitmen dan kelas | mailbox_pk supplier |
| F3.08 | 3.2 Buat komitmen dan kelas | D4 Dokumen deal (salinan tiap pihak) | komitmen + salt, kelas |
| F3.09 | 3.2 Buat komitmen dan kelas | D7 Kotak surat terenkripsi | pembuka komitmen, kelas |
| F3.10 | D4 Dokumen deal (salinan tiap pihak) | 3.3 Mulai alur deal (Flow::new) | invoice, surat, komitmen, alamat, advance, min_confirmations, tag |
| F3.11 | 3.3 Mulai alur deal (Flow::new) | D11 Status deal (node, memori) | Check |
| F3.12 | D2 Node financier (wallet, key, watch-only papan) | 3.4 Pindai papan | wallet watch-only papan |
| F3.13 | D1 Papan registry | 3.4 Pindai papan | memo papan (lewat UFVK) |
| F3.14 | Jaringan Zcash (lightwalletd) | 3.4 Pindai papan | blok, tx penuh, urutan txid |
| F3.15 | 3.4 Pindai papan | D10 Hasil pindai papan (node, memori) | records, settled, rejected |
| F3.16 | D10 Hasil pindai papan (node, memori) | 3.5 Lookup N | records |
| F3.17 | D4 Dokumen deal (salinan tiap pihak) | 3.5 Lookup N | N, supplier_pk, komitmen sendiri, min_confirmations |
| F3.18 | D11 Status deal (node, memori) | 3.5 Lookup N | state |
| F3.19 | Jaringan Zcash (lightwalletd) | 3.5 Lookup N | tinggi tip |
| F3.20 | 3.5 Lookup N | D11 Status deal (node, memori) | AwaitSupplierSignature / AwaitConfirmation / AwaitAssignment / Stopped |
| F3.21 | 3.5 Lookup N | Financier | bebas / sudah dibiayai |
| F3.22 | D7 Kotak surat terenkripsi | 3.6 Tanda tangani entri (supplier) | pembuka komitmen, kelas, history_tag atau sertifikat k |
| F3.23 | 3.6 Tanda tangani entri (supplier) | Supplier | rincian entri: N, financier, kelas |
| F3.24 | Supplier | 3.6 Tanda tangani entri (supplier) | keputusan setuju |
| F3.25 | D3 Key sesi (memori tab) | 3.6 Tanda tangani entri (supplier) | key per invoice |
| F3.26 | D4 Dokumen deal (salinan tiap pihak) | 3.6 Tanda tangani entri (supplier) | invoice (salinan supplier) |
| F3.27 | 3.6 Tanda tangani entri (supplier) | D7 Kotak surat terenkripsi | entri bertanda tangan |
| F3.28 | D7 Kotak surat terenkripsi | 3.7 Periksa entri | entri |
| F3.29 | D4 Dokumen deal (salinan tiap pihak) | 3.7 Periksa entri | invoice, komitmen, tag |
| F3.30 | 3.7 Periksa entri | D11 Status deal (node, memori) | Register |
| F3.31 | 3.7 Periksa entri | Financier | EntryMismatch: entri ditolak |
| F3.32 | 3.7 Periksa entri | D4 Dokumen deal (salinan tiap pihak) | entri yang ditawarkan (USULAN P-14) |
| F3.33 | D11 Status deal (node, memori) | 3.8 Posting entri | entri |
| F3.34 | D2 Node financier (wallet, key, watch-only papan) | 3.8 Posting entri | wallet (spending key) |
| F3.35 | 3.8 Posting entri | D1 Papan registry | entri register (10 000 zat + fee) |
| F3.36 | 3.8 Posting entri | D11 Status deal (node, memori) | AwaitConfirmation + txid |
| F3.37 | D11 Status deal (node, memori) | 3.9 Tunggu konfirmasi | AwaitConfirmation + txid |
| F3.38 | D10 Hasil pindai papan (node, memori) | 3.9 Tunggu konfirmasi | records |
| F3.39 | D4 Dokumen deal (salinan tiap pihak) | 3.9 Tunggu konfirmasi | N, supplier_pk, komitmen, min_confirmations |
| F3.40 | Jaringan Zcash (lightwalletd) | 3.9 Tunggu konfirmasi | tinggi tip |
| F3.41 | 3.9 Tunggu konfirmasi | D11 Status deal (node, memori) | AwaitAssignment / Stopped |
| F3.42 | 3.9 Tunggu konfirmasi | D4 Dokumen deal (salinan tiap pihak) | entri terkonfirmasi |
