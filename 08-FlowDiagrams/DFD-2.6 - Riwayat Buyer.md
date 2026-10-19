---
tags: [flow, dfd]
status: DRAF
updated: 2026-10-19
---

# DFD-2.6 - Riwayat Buyer

**Bagian dari:** [[08 - FlowDiagrams]] · Legenda: [[FD-00 - Arsitektur Target dan Legenda]] · Induk: [[DFD-1 - Proses Utama]] · Sequence: [[SEQ-02 - Buyer]] · [[SEQ-03 - Financier]]

Proses 6.0 dirinci: financier meminta riwayat, buyer menerbitkan sertifikat dengan persetujuan, financier memeriksa rantai terhadap papan dan standar minimalnya; buyer juga bisa memeriksa riwayatnya sendiri. Dasar: wasm `buyerHistoryCert`, `verifyHistory`; `jitsuin-core::history` (`HistoryCert::issue`, `verify_certs`); `jitsuin-board::history` (`verify_history`, `MinimumStandard`); `jitsuin-flow::history` (`HistoryPolicy`, `check_buyer`); [[Desain Jitsuin Seal]] §7.

Satu jalur = satu proses. Kotak bertanda `*` adalah entitas atau penyimpanan yang sama, digambar ulang supaya garis tidak bersilang. Kotak bergaris putus-putus kuning = usulan. Penyimpanan lokal proses ini (tidak muncul di level 1): D5 Allowlist dan policy, D13 Rantai sertifikat buyer.

![DFD-2.6](assets/dfd-2-6.svg)

```plantuml
@startuml dfd-2-6
!include dfd-style.iuml
left to right direction
skinparam nodesep 12
skinparam ranksep 35
rectangle "D12 | Snapshot papan\n(relay)" <<storeproposal>> as D12_8
rectangle "D13 | Rantai sertifikat\nbuyer *" <<storeproposal>> as D13_8
rectangle "Buyer *" <<entity>> as B_8
rectangle "D5 | Allowlist\ndan policy *" <<store>> as D5_7
rectangle "Financier *" <<entity>> as F_7
rectangle "Financier *" <<entity>> as F_6
rectangle "D5 | Allowlist\ndan policy *" <<store>> as D5_6
rectangle "D4 | Dokumen deal\n(lokal) *" <<store>> as D4_6
rectangle "Financier *" <<entity>> as F_5
rectangle "D5 | Allowlist\ndan policy" <<store>> as D5_5
rectangle "D10 | Hasil pindai papan\n(node, memori)" <<store>> as D10_5
rectangle "D4 | Dokumen deal\n(lokal) *" <<store>> as D4_5
rectangle "D4 | Dokumen deal\n(lokal)" <<store>> as D4_4
rectangle "D7 | Kotak surat\nterenkripsi *" <<storeproposal>> as D7_4
rectangle "D7 | Kotak surat\nterenkripsi *" <<storeproposal>> as D7_3
rectangle "D3 | Key sesi\n(memori tab) *" <<store>> as D3_3
rectangle "D13 | Rantai sertifikat\nbuyer *" <<storeproposal>> as D13_3
rectangle "D13 | Rantai sertifikat\nbuyer" <<storeproposal>> as D13_2
rectangle "D3 | Key sesi\n(memori tab)" <<store>> as D3_2
rectangle "Buyer" <<entity>> as B_2
rectangle "D7 | Kotak surat\nterenkripsi *" <<storeproposal>> as D7_2
rectangle "D7 | Kotak surat\nterenkripsi" <<storeproposal>> as D7_1
rectangle "Financier" <<entity>> as F_1
rectangle "**6.8**\nCek riwayat sendiri\n(buyer)" <<process>> as P8
rectangle "**6.7**\nKelola allowlist\ndan standar" <<proposal>> as P7
rectangle "**6.6**\nTerapkan standar\nminimal" <<process>> as P6
rectangle "**6.5**\nCocokkan dengan\npapan" <<process>> as P5
rectangle "**6.4**\nVerifikasi rantai" <<process>> as P4
rectangle "**6.3**\nKirim rantai" <<proposal>> as P3
rectangle "**6.2**\nTerbitkan\nsertifikat" <<process>> as P2
rectangle "**6.1**\nMinta riwayat" <<proposal>> as P1
rectangle "F6.01 N, financier_pk" <<flow>> as f_F6_01
rectangle "F6.02 permintaan riwayat" <<flow>> as f_F6_02
rectangle "F6.03 permintaan" <<flow>> as f_F6_03
rectangle "F6.04 permintaan dari\nfinancier X" <<flow>> as f_F6_04
rectangle "F6.05 persetujuan" <<flow>> as f_F6_05
rectangle "F6.06 key identitas,\nkey invoice" <<flow>> as f_F6_06
rectangle "F6.07 sertifikat k-1" <<flow>> as f_F6_07
rectangle "F6.08 sertifikat k" <<flow>> as f_F6_08
rectangle "F6.09 sertifikat 0..k" <<flow>> as f_F6_09
rectangle "F6.10 key kotak surat" <<flow>> as f_F6_10
rectangle "F6.11 rantai + identity_pk;\nsertifikat k ke supplier" <<flow>> as f_F6_11
rectangle "F6.12 rantai" <<flow>> as f_F6_12
rectangle "F6.13 rantai valid" <<flow>> as f_F6_13
rectangle "F6.14 rantai" <<flow>> as f_F6_14
rectangle "F6.15 entri bertag,\nsettled" <<flow>> as f_F6_15
rectangle "F6.16 allowlist" <<flow>> as f_F6_16
rectangle "F6.17 laporan: on_time, late,\ndefaults, open" <<flow>> as f_F6_17
rectangle "F6.18 UndisclosedSuccessor\n(bisa griefing)" <<flow>> as f_F6_18
rectangle "F6.19 laporan, invoice,\nsertifikat k" <<flow>> as f_F6_19
rectangle "F6.20 standar minimal" <<flow>> as f_F6_20
rectangle "F6.21 lulus / tolak" <<flow>> as f_F6_21
rectangle "F6.22 history_tag +\nsertifikat k" <<flow>> as f_F6_22
rectangle "F6.23 allowlist financier,\nstandar minimal" <<flow>> as f_F6_23
rectangle "F6.24 policy" <<flow>> as f_F6_24
rectangle "F6.25 cek riwayat saya" <<flow>> as f_F6_25
rectangle "F6.26 sertifikat 0..k" <<flow>> as f_F6_26
rectangle "F6.27 snapshot papan" <<flow>> as f_F6_27
rectangle "F6.28 status per invoice" <<flow>> as f_F6_28
F_1 -- f_F6_01
f_F6_01 --> P1
P1 -- f_F6_02
f_F6_02 --> D7_1
P2 <-- f_F6_03
f_F6_03 -- D7_2
B_2 <-- f_F6_04
f_F6_04 -- P2
B_2 -- f_F6_05
f_F6_05 --> P2
P2 <-- f_F6_06
f_F6_06 -- D3_2
P2 <-- f_F6_07
f_F6_07 -- D13_2
P2 -- f_F6_08
f_F6_08 --> D13_2
P3 <-- f_F6_09
f_F6_09 -- D13_3
P3 <-- f_F6_10
f_F6_10 -- D3_3
P3 -- f_F6_11
f_F6_11 --> D7_3
P4 <-- f_F6_12
f_F6_12 -- D7_4
P4 -- f_F6_13
f_F6_13 --> D4_4
P5 <-- f_F6_14
f_F6_14 -- D4_5
P5 <-- f_F6_15
f_F6_15 -- D10_5
P5 <-- f_F6_16
f_F6_16 -- D5_5
P5 -- f_F6_17
f_F6_17 --> D4_5
F_5 <-- f_F6_18
f_F6_18 -- P5
P6 <-- f_F6_19
f_F6_19 -- D4_6
P6 <-- f_F6_20
f_F6_20 -- D5_6
F_6 <-- f_F6_21
f_F6_21 -- P6
P6 -- f_F6_22
f_F6_22 --> D4_6
F_7 -- f_F6_23
f_F6_23 --> P7
P7 -- f_F6_24
f_F6_24 --> D5_7
B_8 -- f_F6_25
f_F6_25 --> P8
P8 <-- f_F6_26
f_F6_26 -- D13_8
P8 <-- f_F6_27
f_F6_27 -- D12_8
B_8 <-- f_F6_28
f_F6_28 -- P8
rectangle " " <<spacer>> as sp_P3_a
rectangle " " <<spacer>> as sp_P3_b
sp_P3_a -[hidden]- sp_P3_b
sp_P3_b -[hidden]- P3
rectangle " " <<spacer>> as sp_P4_a
rectangle " " <<spacer>> as sp_P4_b
sp_P4_a -[hidden]- sp_P4_b
sp_P4_b -[hidden]- P4
@enduml
```

## Proses

| Proses | Isi | Status | Kode / item |
|---|---|---|---|
| 6.1 Minta riwayat | Financier meminta rantai untuk deal N | USULAN (relay) | P-04 |
| 6.2 Terbitkan sertifikat | JTSH 277 byte, ditandatangani key identitas | ADA (fungsi, kartu di layar Buyer) | wasm `buyerHistoryCert` |
| 6.3 Kirim rantai | Rantai ke financier yang diminta; sertifikat k ke supplier untuk entri bertag | USULAN | P-04, P-09 |
| 6.4 Verifikasi rantai | Mulai dari 0, tanpa celah, satu identitas, N berbeda | ADA | `verify_certs` |
| 6.5 Cocokkan dengan papan | Satu entri bertag per sertifikat, equivocation, penerus tersembunyi, hasil dari entri settled, allowlist. Entri palsu bertag penerus memicu `UndisclosedSuccessor` (griefing, Spec #1) | ADA (dengan celah griefing) | `board::history::verify_history` |
| 6.6 Terapkan standar minimal | Batas gagal bayar, persentase tepat waktu, plafon buyer baru; sertifikat k cocok dengan invoice | ADA di flow; layar Financier hanya `verifyHistory` tanpa standar | `MinimumStandard::evaluate`, `check_buyer` |
| 6.7 Kelola allowlist dan standar | Financier menetapkan allowlist dan standar minimal | ADA (struktur), USULAN (layar) | `HistoryPolicy` |
| 6.8 Cek riwayat sendiri | Buyer memeriksa rantainya terhadap papan | PARSIAL (snapshot USULAN) | wasm `verifyHistory` |

## Aliran data

| Aliran | Dari | Ke | Data |
|---|---|---|---|
| F6.01 | Financier | 6.1 Minta riwayat | N, financier_pk |
| F6.02 | 6.1 Minta riwayat | D7 Kotak surat terenkripsi | permintaan riwayat |
| F6.03 | D7 Kotak surat terenkripsi | 6.2 Terbitkan sertifikat | permintaan |
| F6.04 | 6.2 Terbitkan sertifikat | Buyer | permintaan dari financier X |
| F6.05 | Buyer | 6.2 Terbitkan sertifikat | persetujuan |
| F6.06 | D3 Key sesi (memori tab) | 6.2 Terbitkan sertifikat | key identitas, key invoice |
| F6.07 | D13 Rantai sertifikat buyer | 6.2 Terbitkan sertifikat | sertifikat k-1 |
| F6.08 | 6.2 Terbitkan sertifikat | D13 Rantai sertifikat buyer | sertifikat k |
| F6.09 | D13 Rantai sertifikat buyer | 6.3 Kirim rantai | sertifikat 0..k |
| F6.10 | D3 Key sesi (memori tab) | 6.3 Kirim rantai | key kotak surat |
| F6.11 | 6.3 Kirim rantai | D7 Kotak surat terenkripsi | rantai + identity_pk; sertifikat k ke supplier |
| F6.12 | D7 Kotak surat terenkripsi | 6.4 Verifikasi rantai | rantai |
| F6.13 | 6.4 Verifikasi rantai | D4 Dokumen deal (lokal) | rantai valid |
| F6.14 | D4 Dokumen deal (lokal) | 6.5 Cocokkan dengan papan | rantai |
| F6.15 | D10 Hasil pindai papan (node, memori) | 6.5 Cocokkan dengan papan | entri bertag, settled |
| F6.16 | D5 Allowlist dan policy | 6.5 Cocokkan dengan papan | allowlist |
| F6.17 | 6.5 Cocokkan dengan papan | D4 Dokumen deal (lokal) | laporan: on_time, late, defaults, open |
| F6.18 | 6.5 Cocokkan dengan papan | Financier | UndisclosedSuccessor (bisa griefing) |
| F6.19 | D4 Dokumen deal (lokal) | 6.6 Terapkan standar minimal | laporan, invoice, sertifikat k |
| F6.20 | D5 Allowlist dan policy | 6.6 Terapkan standar minimal | standar minimal |
| F6.21 | 6.6 Terapkan standar minimal | Financier | lulus / tolak |
| F6.22 | 6.6 Terapkan standar minimal | D4 Dokumen deal (lokal) | history_tag + sertifikat k |
| F6.23 | Financier | 6.7 Kelola allowlist dan standar | allowlist financier, standar minimal |
| F6.24 | 6.7 Kelola allowlist dan standar | D5 Allowlist dan policy | policy |
| F6.25 | Buyer | 6.8 Cek riwayat sendiri (buyer) | cek riwayat saya |
| F6.26 | D13 Rantai sertifikat buyer | 6.8 Cek riwayat sendiri (buyer) | sertifikat 0..k |
| F6.27 | D12 Snapshot papan (relay) | 6.8 Cek riwayat sendiri (buyer) | snapshot papan |
| F6.28 | 6.8 Cek riwayat sendiri (buyer) | Buyer | status per invoice |
