---
tags: [flow, dfd]
status: DRAF
updated: 2026-10-19
---

# DFD-2.6 - Riwayat Buyer

**Bagian dari:** [[08 - FlowDiagrams]] · Legenda: [[FD-00 - Arsitektur Target dan Legenda]] · Induk: [[DFD-1 - Proses Utama]] · Sequence: [[SEQ-02 - Buyer]] · [[SEQ-03 - Financier]]

Proses 6.0 dirinci: buyer menerbitkan sertifikat riwayat dengan persetujuan, financier memeriksa rantai terhadap papan dan menerapkan standar minimal, lalu tag riwayat dipakai di entri register. Dasar: wasm `buyerHistoryCert`, `verifyHistory`; `jitsuin-core::history` (`HistoryCert::issue`, `verify_certs`); `jitsuin-board::history::verify_history`, `MinimumStandard`; `jitsuin-flow::history::check_buyer`; [[Desain Jitsuin Seal]] §7.

Kotak bertanda `*` adalah entitas atau penyimpanan yang sama yang digambar ulang di jalur proses lain, supaya garis tidak bersilang. Kotak bergaris putus-putus kuning = usulan.

![DFD-2.6](assets/dfd-2-6.svg)

```plantuml
@startuml dfd-2-6
!include dfd-style.iuml
left to right direction
skinparam nodesep 12
skinparam ranksep 35
rectangle "Financier *" <<entity>> as F_6
rectangle "D5 | Allowlist\ndan policy *" <<store>> as D5_6
rectangle "D4 | Dokumen deal *" <<store>> as D4_6
rectangle "D5 | Allowlist\ndan policy" <<store>> as D5_5
rectangle "D10 | Hasil pindai\npapan" <<store>> as D10_5
rectangle "D4 | Dokumen deal *" <<store>> as D4_5
rectangle "D4 | Dokumen deal" <<store>> as D4_4
rectangle "D7 | Kotak surat\nterenkripsi *" <<storeproposal>> as D7_4
rectangle "D7 | Kotak surat\nterenkripsi *" <<storeproposal>> as D7_3
rectangle "D13 | Rantai sertifikat\nbuyer *" <<storeproposal>> as D13_3
rectangle "D13 | Rantai sertifikat\nbuyer" <<storeproposal>> as D13_2
rectangle "D3 | Key sesi\n(memori tab)" <<store>> as D3_2
rectangle "Buyer" <<entity>> as B_2
rectangle "D7 | Kotak surat\nterenkripsi *" <<storeproposal>> as D7_2
rectangle "D7 | Kotak surat\nterenkripsi" <<storeproposal>> as D7_1
rectangle "Financier" <<entity>> as F_1
rectangle "**6.6**\nTerapkan standar\nminimal" <<process>> as P6
rectangle "**6.5**\nCocokkan dengan\npapan" <<process>> as P5
rectangle "**6.4**\nVerifikasi rantai" <<process>> as P4
rectangle "**6.3**\nKirim rantai" <<proposal>> as P3
rectangle "**6.2**\nTerbitkan sertifikat" <<process>> as P2
rectangle "**6.1**\nMinta riwayat" <<proposal>> as P1
rectangle "F6.01 N, financier_pk" <<flow>> as f_F6_01
rectangle "F6.02 permintaan riwayat" <<flow>> as f_F6_02
rectangle "F6.03 permintaan" <<flow>> as f_F6_03
rectangle "F6.04 persetujuan" <<flow>> as f_F6_04
rectangle "F6.05 key identitas,\nkey invoice" <<flow>> as f_F6_05
rectangle "F6.06 sertifikat k-1" <<flow>> as f_F6_06
rectangle "F6.07 sertifikat k" <<flow>> as f_F6_07
rectangle "F6.08 sertifikat 0..k" <<flow>> as f_F6_08
rectangle "F6.09 rantai + identity_pk;\nsertifikat k ke supplier" <<flow>> as f_F6_09
rectangle "F6.10 rantai" <<flow>> as f_F6_10
rectangle "F6.11 rantai valid" <<flow>> as f_F6_11
rectangle "F6.12 rantai" <<flow>> as f_F6_12
rectangle "F6.13 entri bertag,\nsettled" <<flow>> as f_F6_13
rectangle "F6.14 allowlist" <<flow>> as f_F6_14
rectangle "F6.15 laporan: on_time, late,\ndefaults, open" <<flow>> as f_F6_15
rectangle "F6.16 laporan, invoice,\nsertifikat k" <<flow>> as f_F6_16
rectangle "F6.17 standar minimal" <<flow>> as f_F6_17
rectangle "F6.18 lulus / tolak" <<flow>> as f_F6_18
rectangle "F6.19 history_tag\nuntuk entri" <<flow>> as f_F6_19
F_1 -- f_F6_01
f_F6_01 --> P1
P1 -- f_F6_02
f_F6_02 --> D7_1
P2 <-- f_F6_03
f_F6_03 -- D7_2
B_2 -- f_F6_04
f_F6_04 --> P2
P2 <-- f_F6_05
f_F6_05 -- D3_2
P2 <-- f_F6_06
f_F6_06 -- D13_2
P2 -- f_F6_07
f_F6_07 --> D13_2
P3 <-- f_F6_08
f_F6_08 -- D13_3
P3 -- f_F6_09
f_F6_09 --> D7_3
P4 <-- f_F6_10
f_F6_10 -- D7_4
P4 -- f_F6_11
f_F6_11 --> D4_4
P5 <-- f_F6_12
f_F6_12 -- D4_5
P5 <-- f_F6_13
f_F6_13 -- D10_5
P5 <-- f_F6_14
f_F6_14 -- D5_5
P5 -- f_F6_15
f_F6_15 --> D4_5
P6 <-- f_F6_16
f_F6_16 -- D4_6
P6 <-- f_F6_17
f_F6_17 -- D5_6
F_6 <-- f_F6_18
f_F6_18 -- P6
P6 -- f_F6_19
f_F6_19 --> D4_6
rectangle " " <<spacer>> as sp_P3_a
rectangle " " <<spacer>> as sp_P3_b
sp_P3_a -[hidden]- sp_P3_b
sp_P3_b -[hidden]- P3
rectangle " " <<spacer>> as sp_P4_a
rectangle " " <<spacer>> as sp_P4_b
sp_P4_a -[hidden]- sp_P4_b
sp_P4_b -[hidden]- P4
rectangle " " <<spacer>> as sp_P5_a
rectangle " " <<spacer>> as sp_P5_b
sp_P5_a -[hidden]- sp_P5_b
sp_P5_b -[hidden]- P5
@enduml
```

## Proses

| Proses | Isi | Status | Kode / item |
|---|---|---|---|
| 6.1 Minta riwayat | Financier meminta rantai untuk deal N | USULAN (alur relay) | P-04 |
| 6.2 Terbitkan sertifikat | JTSH 277 byte: nomor, key invoice, key supplier, N, nominal, jatuh tempo, key financier, hash sertifikat sebelumnya, tanda tangan key identitas | ADA | wasm `buyerHistoryCert`, `HistoryCert::issue` |
| 6.3 Kirim rantai | Rantai hanya ke financier yang diminta; sertifikat k ke supplier untuk tag entri | USULAN | P-04, P-09 |
| 6.4 Verifikasi rantai | Mulai dari 0, tanpa celah, satu identitas, N berbeda | ADA | `verify_certs` |
| 6.5 Cocokkan dengan papan | Satu entri bertag per sertifikat (bertanda tangan supplier), equivocation, penerus tersembunyi, hasil per invoice dari entri settled | ADA (lihat temuan Spec #1 griefing) | `board::history::verify_history` |
| 6.6 Terapkan standar minimal | Batas gagal bayar, persentase tepat waktu, plafon buyer baru; sertifikat k harus cocok dengan invoice | ADA | `MinimumStandard::evaluate`, `check_buyer` |

## Aliran data

| Aliran | Dari | Ke | Data |
|---|---|---|---|
| F6.01 | Financier | 6.1 Minta riwayat | N, financier_pk |
| F6.02 | 6.1 Minta riwayat | D7 | Kotak surat terenkripsi | permintaan riwayat |
| F6.03 | D7 | Kotak surat terenkripsi | 6.2 Terbitkan sertifikat | permintaan |
| F6.04 | Buyer | 6.2 Terbitkan sertifikat | persetujuan |
| F6.05 | D3 | Key sesi (memori tab) | 6.2 Terbitkan sertifikat | key identitas, key invoice |
| F6.06 | D13 | Rantai sertifikat buyer | 6.2 Terbitkan sertifikat | sertifikat k-1 |
| F6.07 | 6.2 Terbitkan sertifikat | D13 | Rantai sertifikat buyer | sertifikat k |
| F6.08 | D13 | Rantai sertifikat buyer | 6.3 Kirim rantai | sertifikat 0..k |
| F6.09 | 6.3 Kirim rantai | D7 | Kotak surat terenkripsi | rantai + identity_pk; sertifikat k ke supplier |
| F6.10 | D7 | Kotak surat terenkripsi | 6.4 Verifikasi rantai | rantai |
| F6.11 | 6.4 Verifikasi rantai | D4 | Dokumen deal | rantai valid |
| F6.12 | D4 | Dokumen deal | 6.5 Cocokkan dengan papan | rantai |
| F6.13 | D10 | Hasil pindai papan | 6.5 Cocokkan dengan papan | entri bertag, settled |
| F6.14 | D5 | Allowlist dan policy | 6.5 Cocokkan dengan papan | allowlist |
| F6.15 | 6.5 Cocokkan dengan papan | D4 | Dokumen deal | laporan: on_time, late, defaults, open |
| F6.16 | D4 | Dokumen deal | 6.6 Terapkan standar minimal | laporan, invoice, sertifikat k |
| F6.17 | D5 | Allowlist dan policy | 6.6 Terapkan standar minimal | standar minimal |
| F6.18 | 6.6 Terapkan standar minimal | Financier | lulus / tolak |
| F6.19 | 6.6 Terapkan standar minimal | D4 | Dokumen deal | history_tag untuk entri |
