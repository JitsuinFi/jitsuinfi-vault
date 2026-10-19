---
tags: [flow, dfd]
status: DRAF
updated: 2026-10-19
---

# DFD-2.3 - Registrasi Papan

**Bagian dari:** [[08 - FlowDiagrams]] · Legenda: [[FD-00 - Arsitektur Target dan Legenda]] · Induk: [[DFD-1 - Proses Utama]] · Sequence: [[SEQ-03 - Financier]] · [[SEQ-01 - Supplier]]

Proses 3.0 dirinci: dari penawaran sampai entri financier terkonfirmasi sebagai entri valid pertama untuk N. Dasar: `jitsuin-flow::financier` (`Flow`, `check`, `register`, `wait_for_confirmation`), `jitsuin-board` (`scan`, `collect`, `lookup`, `lwd`), wasm `supplierRegisterEntry`, `supplierRegisterHistoryEntry`.

Kotak bertanda `*` adalah entitas atau penyimpanan yang sama yang digambar ulang di jalur proses lain, supaya garis tidak bersilang. Kotak bergaris putus-putus kuning = usulan.

![DFD-2.3](assets/dfd-2-3.svg)

```plantuml
@startuml dfd-2-3
!include dfd-style.iuml
left to right direction
skinparam nodesep 12
skinparam ranksep 35
rectangle "D4 | Dokumen deal *" <<store>> as D4_8
rectangle "D11 | Status deal\n(state machine) *" <<store>> as D11_8
rectangle "Jaringan Zcash\n(lightwalletd) *" <<entity>> as Z_8
rectangle "D10 | Hasil pindai\npapan *" <<store>> as D10_8
rectangle "Jaringan Zcash\n(lightwalletd) *" <<entity>> as Z_7
rectangle "D2 | Wallet dan\nkey financier *" <<store>> as D2_7
rectangle "D11 | Status deal\n(state machine) *" <<store>> as D11_7
rectangle "D11 | Status deal\n(state machine) *" <<store>> as D11_6
rectangle "D4 | Dokumen deal *" <<store>> as D4_6
rectangle "D7 | Kotak surat\nterenkripsi *" <<storeproposal>> as D7_6
rectangle "D4 | Dokumen deal *" <<store>> as D4_5
rectangle "D3 | Key sesi\n(memori tab)" <<store>> as D3_5
rectangle "Supplier *" <<entity>> as S_5
rectangle "D7 | Kotak surat\nterenkripsi *" <<storeproposal>> as D7_5
rectangle "D7 | Kotak surat\nterenkripsi" <<storeproposal>> as D7_4
rectangle "D4 | Dokumen deal *" <<store>> as D4_4
rectangle "D2 | Wallet dan\nkey financier" <<store>> as D2_4
rectangle "Financier *" <<entity>> as F_3
rectangle "D11 | Status deal\n(state machine)" <<store>> as D11_3
rectangle "Jaringan Zcash\n(lightwalletd) *" <<entity>> as Z_3
rectangle "D4 | Dokumen deal *" <<store>> as D4_3
rectangle "D10 | Hasil pindai\npapan *" <<store>> as D10_3
rectangle "D10 | Hasil pindai\npapan" <<store>> as D10_2
rectangle "Jaringan Zcash\n(lightwalletd)" <<entity>> as Z_2
rectangle "D1 | Papan registry" <<store>> as D1_2
rectangle "D14 | Wallet watch-only\npapan" <<store>> as D14_2
rectangle "D4 | Dokumen deal" <<store>> as D4_1
rectangle "Financier" <<entity>> as F_1
rectangle "Supplier" <<entity>> as S_1
rectangle "**3.8**\nTunggu konfirmasi" <<process>> as P8
rectangle "**3.7**\nPosting entri" <<process>> as P7
rectangle "**3.6**\nPeriksa entri" <<process>> as P6
rectangle "**3.5**\nTandatangani entri\n(supplier)" <<process>> as P5
rectangle "**3.4**\nBuat pembuka\nkomitmen" <<process>> as P4
rectangle "**3.3**\nLookup N" <<process>> as P3
rectangle "**3.2**\nPindai papan" <<process>> as P2
rectangle "**3.1**\nTerima penawaran" <<proposal>> as P1
rectangle "F3.01 penawaran: invoice, sig,\nalamat, advance" <<flow>> as f_F3_01
rectangle "F3.02 syarat: advance,\nkonfirmasi, bucket" <<flow>> as f_F3_02
rectangle "F3.03 deal" <<flow>> as f_F3_03
rectangle "F3.04 wallet watch-only" <<flow>> as f_F3_04
rectangle "F3.05 memo papan\n(lewat UFVK)" <<flow>> as f_F3_05
rectangle "F3.06 blok, tx penuh,\nurutan txid" <<flow>> as f_F3_06
rectangle "F3.07 records, settled,\nrejected (terurut)" <<flow>> as f_F3_07
rectangle "F3.08 records" <<flow>> as f_F3_08
rectangle "F3.09 N, supplier_pk" <<flow>> as f_F3_09
rectangle "F3.10 tinggi tip" <<flow>> as f_F3_10
rectangle "F3.11 Check ->\nAwaitSupplierSignature\natau Stopped" <<flow>> as f_F3_11
rectangle "F3.12 sudah dibiayai\n(berhenti)" <<flow>> as f_F3_12
rectangle "F3.13 financier_pk" <<flow>> as f_F3_13
rectangle "F3.14 tag riwayat" <<flow>> as f_F3_14
rectangle "F3.15 pembuka komitmen\n(pk, salt), bucket" <<flow>> as f_F3_15
rectangle "F3.16 pembuka komitmen" <<flow>> as f_F3_16
rectangle "F3.17 persetujuan" <<flow>> as f_F3_17
rectangle "F3.18 key per invoice" <<flow>> as f_F3_18
rectangle "F3.19 invoice,\nsertifikat k" <<flow>> as f_F3_19
rectangle "F3.20 entri bertanda\ntangan" <<flow>> as f_F3_20
rectangle "F3.21 entri" <<flow>> as f_F3_21
rectangle "F3.22 invoice, komitmen,\ntag" <<flow>> as f_F3_22
rectangle "F3.23 Register" <<flow>> as f_F3_23
rectangle "F3.24 entri" <<flow>> as f_F3_24
rectangle "F3.25 wallet (spending key)" <<flow>> as f_F3_25
rectangle "F3.26 tx 10 000 zat\n+ memo entri" <<flow>> as f_F3_26
rectangle "F3.27 AwaitConfirmation\n+ txid" <<flow>> as f_F3_27
rectangle "F3.28 records" <<flow>> as f_F3_28
rectangle "F3.29 tinggi tip" <<flow>> as f_F3_29
rectangle "F3.30 AwaitAssignment\natau Stopped" <<flow>> as f_F3_30
rectangle "F3.31 entri terkonfirmasi /\nentri ditolak" <<flow>> as f_F3_31
S_1 -- f_F3_01
f_F3_01 --> P1
F_1 -- f_F3_02
f_F3_02 --> P1
P1 -- f_F3_03
f_F3_03 --> D4_1
P2 <-- f_F3_04
f_F3_04 -- D14_2
P2 <-- f_F3_05
f_F3_05 -- D1_2
Z_2 -- f_F3_06
f_F3_06 --> P2
P2 -- f_F3_07
f_F3_07 --> D10_2
P3 <-- f_F3_08
f_F3_08 -- D10_3
P3 <-- f_F3_09
f_F3_09 -- D4_3
Z_3 -- f_F3_10
f_F3_10 --> P3
P3 -- f_F3_11
f_F3_11 --> D11_3
F_3 <-- f_F3_12
f_F3_12 -- P3
P4 <-- f_F3_13
f_F3_13 -- D2_4
P4 <-- f_F3_14
f_F3_14 -- D4_4
P4 -- f_F3_15
f_F3_15 --> D7_4
P5 <-- f_F3_16
f_F3_16 -- D7_5
S_5 -- f_F3_17
f_F3_17 --> P5
P5 <-- f_F3_18
f_F3_18 -- D3_5
P5 <-- f_F3_19
f_F3_19 -- D4_5
P5 -- f_F3_20
f_F3_20 --> D7_5
P6 <-- f_F3_21
f_F3_21 -- D7_6
P6 <-- f_F3_22
f_F3_22 -- D4_6
P6 -- f_F3_23
f_F3_23 --> D11_6
P7 <-- f_F3_24
f_F3_24 -- D11_7
P7 <-- f_F3_25
f_F3_25 -- D2_7
Z_7 <-- f_F3_26
f_F3_26 -- P7
P7 -- f_F3_27
f_F3_27 --> D11_7
P8 <-- f_F3_28
f_F3_28 -- D10_8
Z_8 -- f_F3_29
f_F3_29 --> P8
P8 -- f_F3_30
f_F3_30 --> D11_8
P8 -- f_F3_31
f_F3_31 --> D4_8
rectangle " " <<spacer>> as sp_P4_a
rectangle " " <<spacer>> as sp_P4_b
sp_P4_a -[hidden]- sp_P4_b
sp_P4_b -[hidden]- P4
rectangle " " <<spacer>> as sp_P6_a
rectangle " " <<spacer>> as sp_P6_b
sp_P6_a -[hidden]- sp_P6_b
sp_P6_b -[hidden]- P6
@enduml
```

## Proses

| Proses | Isi | Status | Kode / item |
|---|---|---|---|
| 3.1 Terima penawaran | Supplier mengirim invoice + tanda tangan buyer + alamat advance; financier menetapkan advance, `min_confirmations` ≥ 1, bucket | USULAN (alur relay); `Deal` ADA | `financier::Deal`, P-04 |
| 3.2 Pindai papan | `sync`, `enhance`, `list_tx` wallet watch-only; `block_txids` per tinggi; `collect` dan urut (tinggi, indeks tx, indeks output) | ADA | `jitsuin_board::scan` |
| 3.3 Lookup N | Entri valid pertama menang; tanda tangan tidak valid diabaikan; komitmen lain = sudah dibiayai; lebih dari satu komitmen = pembiayaan ganda | ADA | `jitsuin_board::lookup`, `Flow::on_board` |
| 3.4 Buat pembuka komitmen | `financier_commitment = BLAKE2b(financier_pk ‖ salt)`; salt CSPRNG 32 byte | ADA (fungsi); salt dari library USULAN P-08 | `jitsuin_core::financier_commitment` |
| 3.5 Tandatangani entri | Entri `0x01` atau `0x03` (bertag riwayat), tanda tangan key per invoice supplier | PARSIAL (wasm ADA, layar belum) | wasm `supplierRegisterEntry`, `supplierRegisterHistoryEntry` |
| 3.6 Periksa entri | Jenis register, N, komitmen, tag riwayat, tanda tangan supplier | ADA | `Flow::check_entry` |
| 3.7 Posting entri | Bayar 10 000 zat ke alamat papan dengan memo entri | ADA | `Financier::register`, `ENTRY_POST_ZAT` |
| 3.8 Tunggu konfirmasi | Poll sampai konfirmasi ≥ minimum; reorg kembali ke `AwaitConfirmation`; konflik baru `Stopped` | ADA | `wait_for_confirmation`, `confirmations` |

## Aliran data

| Aliran | Dari | Ke | Data |
|---|---|---|---|
| F3.01 | Supplier | 3.1 Terima penawaran | penawaran: invoice, sig, alamat, advance |
| F3.02 | Financier | 3.1 Terima penawaran | syarat: advance, konfirmasi, bucket |
| F3.03 | 3.1 Terima penawaran | D4 | Dokumen deal | deal |
| F3.04 | D14 | Wallet watch-only papan | 3.2 Pindai papan | wallet watch-only |
| F3.05 | D1 | Papan registry | 3.2 Pindai papan | memo papan (lewat UFVK) |
| F3.06 | Jaringan Zcash (lightwalletd) | 3.2 Pindai papan | blok, tx penuh, urutan txid |
| F3.07 | 3.2 Pindai papan | D10 | Hasil pindai papan | records, settled, rejected (terurut) |
| F3.08 | D10 | Hasil pindai papan | 3.3 Lookup N | records |
| F3.09 | D4 | Dokumen deal | 3.3 Lookup N | N, supplier_pk |
| F3.10 | Jaringan Zcash (lightwalletd) | 3.3 Lookup N | tinggi tip |
| F3.11 | 3.3 Lookup N | D11 | Status deal (state machine) | Check -> AwaitSupplierSignature atau Stopped |
| F3.12 | 3.3 Lookup N | Financier | sudah dibiayai (berhenti) |
| F3.13 | D2 | Wallet dan key financier | 3.4 Buat pembuka komitmen | financier_pk |
| F3.14 | D4 | Dokumen deal | 3.4 Buat pembuka komitmen | tag riwayat |
| F3.15 | 3.4 Buat pembuka komitmen | D7 | Kotak surat terenkripsi | pembuka komitmen (pk, salt), bucket |
| F3.16 | D7 | Kotak surat terenkripsi | 3.5 Tandatangani entri (supplier) | pembuka komitmen |
| F3.17 | Supplier | 3.5 Tandatangani entri (supplier) | persetujuan |
| F3.18 | D3 | Key sesi (memori tab) | 3.5 Tandatangani entri (supplier) | key per invoice |
| F3.19 | D4 | Dokumen deal | 3.5 Tandatangani entri (supplier) | invoice, sertifikat k |
| F3.20 | 3.5 Tandatangani entri (supplier) | D7 | Kotak surat terenkripsi | entri bertanda tangan |
| F3.21 | D7 | Kotak surat terenkripsi | 3.6 Periksa entri | entri |
| F3.22 | D4 | Dokumen deal | 3.6 Periksa entri | invoice, komitmen, tag |
| F3.23 | 3.6 Periksa entri | D11 | Status deal (state machine) | Register |
| F3.24 | D11 | Status deal (state machine) | 3.7 Posting entri | entri |
| F3.25 | D2 | Wallet dan key financier | 3.7 Posting entri | wallet (spending key) |
| F3.26 | 3.7 Posting entri | Jaringan Zcash (lightwalletd) | tx 10 000 zat + memo entri |
| F3.27 | 3.7 Posting entri | D11 | Status deal (state machine) | AwaitConfirmation + txid |
| F3.28 | D10 | Hasil pindai papan | 3.8 Tunggu konfirmasi | records |
| F3.29 | Jaringan Zcash (lightwalletd) | 3.8 Tunggu konfirmasi | tinggi tip |
| F3.30 | 3.8 Tunggu konfirmasi | D11 | Status deal (state machine) | AwaitAssignment atau Stopped |
| F3.31 | 3.8 Tunggu konfirmasi | D4 | Dokumen deal | entri terkonfirmasi / entri ditolak |
