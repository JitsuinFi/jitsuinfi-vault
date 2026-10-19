---
tags: [flow, dfd]
status: DRAF
updated: 2026-10-19
---

# DFD-2.4 - Pengalihan dan Advance

**Bagian dari:** [[08 - FlowDiagrams]] · Legenda: [[FD-00 - Arsitektur Target dan Legenda]] · Induk: [[DFD-1 - Proses Utama]] · Sequence: [[SEQ-03 - Financier]] · [[SEQ-01 - Supplier]] · [[SEQ-02 - Buyer]]

Proses 4.0 dirinci: surat pengalihan disegel supplier lalu buyer, lalu advance dikirim bersama seal financier dalam satu transaksi shielded (Sign-to-Pay). Seal boleh dikumpulkan lebih awal, tetapi baru diterapkan di state `AwaitAssignment`. Dasar: wasm `assignmentEncode`, `supplierSealAssignment`, `buyerSealAssignment`, `assignmentStatus`; `jitsuin-flow::financier::pay_advance`, `sent_advance`; `jitsuin-flow::supplier::verify_sign_to_pay`; [[Desain Jitsuin Seal]].

Satu jalur = satu proses. Kotak bertanda `*` adalah entitas atau penyimpanan yang sama, digambar ulang supaya garis tidak bersilang. Kotak bergaris putus-putus kuning = usulan.

![DFD-2.4](assets/dfd-2-4.svg)

```plantuml
@startuml dfd-2-4
!include dfd-style.iuml
left to right direction
skinparam nodesep 12
skinparam ranksep 35
rectangle "Supplier *" <<entity>> as S_8
rectangle "D4 | Dokumen deal\n(lokal) *" <<store>> as D4_8
rectangle "D7 | Kotak surat\nterenkripsi *" <<storeproposal>> as D7_8
rectangle "D7 | Kotak surat\nterenkripsi *" <<storeproposal>> as D7_7
rectangle "D6 | Akun dana\n(operasional)" <<store>> as D6_7
rectangle "Jaringan Zcash\n(lightwalletd)" <<entity>> as Z_7
rectangle "D2 | Node financier\n(wallet, key,\nwatch-only papan) *" <<store>> as D2_7
rectangle "D11 | Status deal\n(node, memori) *" <<store>> as D11_7
rectangle "D11 | Status deal\n(node, memori) *" <<store>> as D11_6
rectangle "D4 | Dokumen deal\n(lokal) *" <<store>> as D4_6
rectangle "D2 | Node financier\n(wallet, key,\nwatch-only papan) *" <<store>> as D2_6
rectangle "D2 | Node financier\n(wallet, key,\nwatch-only papan) *" <<store>> as D2_5
rectangle "D1 | Papan registry" <<store>> as D1_5
rectangle "D11 | Status deal\n(node, memori) *" <<store>> as D11_5
rectangle "D11 | Status deal\n(node, memori)" <<store>> as D11_4
rectangle "D4 | Dokumen deal\n(lokal) *" <<store>> as D4_4
rectangle "D7 | Kotak surat\nterenkripsi *" <<storeproposal>> as D7_4
rectangle "D3 | Key sesi\n(memori tab) *" <<store>> as D3_3
rectangle "Buyer" <<entity>> as B_3
rectangle "D7 | Kotak surat\nterenkripsi *" <<storeproposal>> as D7_3
rectangle "D3 | Key sesi\n(memori tab)" <<store>> as D3_2
rectangle "Supplier" <<entity>> as S_2
rectangle "D4 | Dokumen deal\n(lokal) *" <<store>> as D4_2
rectangle "D7 | Kotak surat\nterenkripsi *" <<storeproposal>> as D7_2
rectangle "D7 | Kotak surat\nterenkripsi" <<storeproposal>> as D7_1
rectangle "D2 | Node financier\n(wallet, key,\nwatch-only papan)" <<store>> as D2_1
rectangle "D4 | Dokumen deal\n(lokal)" <<store>> as D4_1
rectangle "Financier" <<entity>> as F_1
rectangle "**4.8**\nVerifikasi advance\n(supplier)" <<process>> as P8
rectangle "**4.7**\nKirim advance" <<process>> as P7
rectangle "**4.6**\nSusun memo\nSign-to-Pay" <<process>> as P6
rectangle "**4.5**\nCek terakhir dan\nidempotensi" <<process>> as P5
rectangle "**4.4**\nVerifikasi rantai\nseal" <<process>> as P4
rectangle "**4.3**\nSegel buyer" <<process>> as P3
rectangle "**4.2**\nSegel supplier" <<process>> as P2
rectangle "**4.1**\nBuat surat\npengalihan" <<process>> as P1
rectangle "F4.01 PDF surat,\nalamat bayar" <<flow>> as f_F4_01
rectangle "F4.02 invoice" <<flow>> as f_F4_02
rectangle "F4.03 financier_pk" <<flow>> as f_F4_03
rectangle "F4.04 surat JTSA" <<flow>> as f_F4_04
rectangle "F4.05 surat ke supplier\ndan buyer" <<flow>> as f_F4_05
rectangle "F4.06 surat" <<flow>> as f_F4_06
rectangle "F4.07 invoice" <<flow>> as f_F4_07
rectangle "F4.08 isi surat\n(assignmentDecode, USULAN)" <<flow>> as f_F4_08
rectangle "F4.09 keputusan setuju" <<flow>> as f_F4_09
rectangle "F4.10 key per invoice" <<flow>> as f_F4_10
rectangle "F4.11 seal s0" <<flow>> as f_F4_11
rectangle "F4.12 s0 ke buyer\ndan financier" <<flow>> as f_F4_12
rectangle "F4.13 surat + s0" <<flow>> as f_F4_13
rectangle "F4.14 isi surat: alamat\nbayar, nominal" <<flow>> as f_F4_14
rectangle "F4.15 keputusan setuju" <<flow>> as f_F4_15
rectangle "F4.16 key invoice buyer" <<flow>> as f_F4_16
rectangle "F4.17 s1 ke financier\ndan supplier" <<flow>> as f_F4_17
rectangle "F4.18 s0, s1" <<flow>> as f_F4_18
rectangle "F4.19 invoice, surat" <<flow>> as f_F4_19
rectangle "F4.20 AwaitAssignment" <<flow>> as f_F4_20
rectangle "F4.21 Pay + seal" <<flow>> as f_F4_21
rectangle "F4.22 state Pay" <<flow>> as f_F4_22
rectangle "F4.23 cek papan\nterakhir" <<flow>> as f_F4_23
rectangle "F4.24 tx terkirim\n(sent_advance)" <<flow>> as f_F4_24
rectangle "F4.25 tetap Pay / mundur\n/ txid lama" <<flow>> as f_F4_25
rectangle "F4.26 key financier" <<flow>> as f_F4_26
rectangle "F4.27 surat, invoice,\nnominal advance" <<flow>> as f_F4_27
rectangle "F4.28 seal s0, s1" <<flow>> as f_F4_28
rectangle "F4.29 memo: kuitansi +\nseal s2 + JTN1" <<flow>> as f_F4_29
rectangle "F4.30 memo, alamat\nsupplier" <<flow>> as f_F4_30
rectangle "F4.31 wallet" <<flow>> as f_F4_31
rectangle "F4.32 tx advance\nshielded" <<flow>> as f_F4_32
rectangle "F4.33 Done + txid" <<flow>> as f_F4_33
rectangle "F4.34 advance + catatan\npiutang (dana)" <<flow>> as f_F4_34
rectangle "F4.35 txid + memo\nke supplier" <<flow>> as f_F4_35
rectangle "F4.36 txid + memo, s1" <<flow>> as f_F4_36
rectangle "F4.37 invoice, surat, s0" <<flow>> as f_F4_37
rectangle "F4.38 nominal yang\nterlihat di Zodl" <<flow>> as f_F4_38
rectangle "F4.39 Sealed / gagal" <<flow>> as f_F4_39
F_1 -- f_F4_01
f_F4_01 --> P1
P1 <-- f_F4_02
f_F4_02 -- D4_1
P1 <-- f_F4_03
f_F4_03 -- D2_1
P1 -- f_F4_04
f_F4_04 --> D4_1
P1 -- f_F4_05
f_F4_05 --> D7_1
P2 <-- f_F4_06
f_F4_06 -- D7_2
P2 <-- f_F4_07
f_F4_07 -- D4_2
S_2 <-- f_F4_08
f_F4_08 -- P2
S_2 -- f_F4_09
f_F4_09 --> P2
P2 <-- f_F4_10
f_F4_10 -- D3_2
P2 -- f_F4_11
f_F4_11 --> D4_2
P2 -- f_F4_12
f_F4_12 --> D7_2
P3 <-- f_F4_13
f_F4_13 -- D7_3
B_3 <-- f_F4_14
f_F4_14 -- P3
B_3 -- f_F4_15
f_F4_15 --> P3
P3 <-- f_F4_16
f_F4_16 -- D3_3
P3 -- f_F4_17
f_F4_17 --> D7_3
P4 <-- f_F4_18
f_F4_18 -- D7_4
P4 <-- f_F4_19
f_F4_19 -- D4_4
P4 <-- f_F4_20
f_F4_20 -- D11_4
P4 -- f_F4_21
f_F4_21 --> D11_4
P5 <-- f_F4_22
f_F4_22 -- D11_5
P5 <-- f_F4_23
f_F4_23 -- D1_5
P5 <-- f_F4_24
f_F4_24 -- D2_5
P5 -- f_F4_25
f_F4_25 --> D11_5
P6 <-- f_F4_26
f_F4_26 -- D2_6
P6 <-- f_F4_27
f_F4_27 -- D4_6
P6 <-- f_F4_28
f_F4_28 -- D11_6
P6 -- f_F4_29
f_F4_29 --> D11_6
P7 <-- f_F4_30
f_F4_30 -- D11_7
P7 <-- f_F4_31
f_F4_31 -- D2_7
Z_7 <-- f_F4_32
f_F4_32 -- P7
P7 -- f_F4_33
f_F4_33 --> D11_7
P7 -- f_F4_34
f_F4_34 --> D6_7
P7 -- f_F4_35
f_F4_35 --> D7_7
P8 <-- f_F4_36
f_F4_36 -- D7_8
P8 <-- f_F4_37
f_F4_37 -- D4_8
S_8 -- f_F4_38
f_F4_38 --> P8
S_8 <-- f_F4_39
f_F4_39 -- P8
rectangle " " <<spacer>> as sp_P4_a
rectangle " " <<spacer>> as sp_P4_b
sp_P4_a -[hidden]- sp_P4_b
sp_P4_b -[hidden]- P4
rectangle " " <<spacer>> as sp_P5_a
rectangle " " <<spacer>> as sp_P5_b
sp_P5_a -[hidden]- sp_P5_b
sp_P5_b -[hidden]- P5
rectangle " " <<spacer>> as sp_P6_a
rectangle " " <<spacer>> as sp_P6_b
sp_P6_a -[hidden]- sp_P6_b
sp_P6_b -[hidden]- P6
@enduml
```

## Proses

| Proses | Isi | Status | Kode / item |
|---|---|---|---|
| 4.1 Buat surat pengalihan | JTSA: N, nominal, jatuh tempo, `financier_pk`, alamat bayar, `terms_hash`; dibuat sebelum 3.3 | ADA | wasm `assignmentEncode` |
| 4.2 Segel supplier | Seal langkah 0; isi surat belum bisa ditampilkan (tidak ada `assignmentDecode` di wasm) | PARSIAL | wasm `supplierSealAssignment` |
| 4.3 Segel buyer | Seal langkah 1, pengakuan tertulis (Pasal 613 KUHPerdata); buyer harus bisa membaca alamat dan nominal sebelum menyegel | PARSIAL (decode surat belum ada) | wasm `buyerSealAssignment` |
| 4.4 Verifikasi rantai seal | Urutan, rantai hash, signer = key role, tanpa `SelfApproval`; event diterima hanya di `AwaitAssignment` | ADA | `Assignment::verify`, `AssignmentSealed` |
| 4.5 Cek terakhir dan idempotensi | Scan sekali lagi; konflik atau reorg keluar dari `Pay`; advance yang sudah terkirim dicatat, tidak dibayar dua kali | ADA | `pay_advance`, `sent_advance` |
| 4.6 Susun memo Sign-to-Pay | Kuitansi JTR1 + seal financier JTL1 + catatan piutang JTN1 (394 byte) | ADA | `Receipt::sign`, `seal_next`, `ReceivableNote` |
| 4.7 Kirim advance | Satu transaksi shielded ke alamat supplier | ADA (diuji testnet) | `Devtool::pay` |
| 4.8 Verifikasi advance | Kuitansi ditandatangani `financier_pk`, nominal = nilai output, rantai `Sealed`. Hanya kuat bila dibaca dari wallet supplier sendiri; memo lewat relay tidak membuktikan uang dan seal satu transaksi | ADA di flow (butuh tx wallet supplier); USULAN di web | `supplier::received_advances`, `verify_sign_to_pay` |

## Aliran data

| Aliran | Dari | Ke | Data |
|---|---|---|---|
| F4.01 | Financier | 4.1 Buat surat pengalihan | PDF surat, alamat bayar |
| F4.02 | D4 Dokumen deal (lokal) | 4.1 Buat surat pengalihan | invoice |
| F4.03 | D2 Node financier (wallet, key, watch-only papan) | 4.1 Buat surat pengalihan | financier_pk |
| F4.04 | 4.1 Buat surat pengalihan | D4 Dokumen deal (lokal) | surat JTSA |
| F4.05 | 4.1 Buat surat pengalihan | D7 Kotak surat terenkripsi | surat ke supplier dan buyer |
| F4.06 | D7 Kotak surat terenkripsi | 4.2 Segel supplier | surat |
| F4.07 | D4 Dokumen deal (lokal) | 4.2 Segel supplier | invoice |
| F4.08 | 4.2 Segel supplier | Supplier | isi surat (assignmentDecode, USULAN) |
| F4.09 | Supplier | 4.2 Segel supplier | keputusan setuju |
| F4.10 | D3 Key sesi (memori tab) | 4.2 Segel supplier | key per invoice |
| F4.11 | 4.2 Segel supplier | D4 Dokumen deal (lokal) | seal s0 |
| F4.12 | 4.2 Segel supplier | D7 Kotak surat terenkripsi | s0 ke buyer dan financier |
| F4.13 | D7 Kotak surat terenkripsi | 4.3 Segel buyer | surat + s0 |
| F4.14 | 4.3 Segel buyer | Buyer | isi surat: alamat bayar, nominal |
| F4.15 | Buyer | 4.3 Segel buyer | keputusan setuju |
| F4.16 | D3 Key sesi (memori tab) | 4.3 Segel buyer | key invoice buyer |
| F4.17 | 4.3 Segel buyer | D7 Kotak surat terenkripsi | s1 ke financier dan supplier |
| F4.18 | D7 Kotak surat terenkripsi | 4.4 Verifikasi rantai seal | s0, s1 |
| F4.19 | D4 Dokumen deal (lokal) | 4.4 Verifikasi rantai seal | invoice, surat |
| F4.20 | D11 Status deal (node, memori) | 4.4 Verifikasi rantai seal | AwaitAssignment |
| F4.21 | 4.4 Verifikasi rantai seal | D11 Status deal (node, memori) | Pay + seal |
| F4.22 | D11 Status deal (node, memori) | 4.5 Cek terakhir dan idempotensi | state Pay |
| F4.23 | D1 Papan registry | 4.5 Cek terakhir dan idempotensi | cek papan terakhir |
| F4.24 | D2 Node financier (wallet, key, watch-only papan) | 4.5 Cek terakhir dan idempotensi | tx terkirim (sent_advance) |
| F4.25 | 4.5 Cek terakhir dan idempotensi | D11 Status deal (node, memori) | tetap Pay / mundur / txid lama |
| F4.26 | D2 Node financier (wallet, key, watch-only papan) | 4.6 Susun memo Sign-to-Pay | key financier |
| F4.27 | D4 Dokumen deal (lokal) | 4.6 Susun memo Sign-to-Pay | surat, invoice, nominal advance |
| F4.28 | D11 Status deal (node, memori) | 4.6 Susun memo Sign-to-Pay | seal s0, s1 |
| F4.29 | 4.6 Susun memo Sign-to-Pay | D11 Status deal (node, memori) | memo: kuitansi + seal s2 + JTN1 |
| F4.30 | D11 Status deal (node, memori) | 4.7 Kirim advance | memo, alamat supplier |
| F4.31 | D2 Node financier (wallet, key, watch-only papan) | 4.7 Kirim advance | wallet |
| F4.32 | 4.7 Kirim advance | Jaringan Zcash (lightwalletd) | tx advance shielded |
| F4.33 | 4.7 Kirim advance | D11 Status deal (node, memori) | Done + txid |
| F4.34 | 4.7 Kirim advance | D6 Akun dana (operasional) | advance + catatan piutang (dana) |
| F4.35 | 4.7 Kirim advance | D7 Kotak surat terenkripsi | txid + memo ke supplier |
| F4.36 | D7 Kotak surat terenkripsi | 4.8 Verifikasi advance (supplier) | txid + memo, s1 |
| F4.37 | D4 Dokumen deal (lokal) | 4.8 Verifikasi advance (supplier) | invoice, surat, s0 |
| F4.38 | Supplier | 4.8 Verifikasi advance (supplier) | nominal yang terlihat di Zodl |
| F4.39 | 4.8 Verifikasi advance (supplier) | Supplier | Sealed / gagal |
