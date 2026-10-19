---
tags: [flow, dfd]
status: DRAF
updated: 2026-10-19
---

# DFD-2.7 - Deteksi Pembiayaan Ganda

**Bagian dari:** [[08 - FlowDiagrams]] · Legenda: [[FD-00 - Arsitektur Target dan Legenda]] · Induk: [[DFD-1 - Proses Utama]] · Sequence: [[SEQ-03 - Financier]] · [[SEQ-01 - Supplier]]

Proses 7.0 dirinci: financier kedua berhenti sebelum membayar dan menyusun bukti bahwa supplier menandatangani N yang sama untuk dua financier. Dasar: `jitsuin-board::lookup`, `Flow::on_board` (`Stop`), wasm `doubleSignProof`, `verifyProof`, `jitsuin-core::proof`, `verify_proof_on_board`.

Kotak bertanda `*` adalah entitas atau penyimpanan yang sama yang digambar ulang di jalur proses lain, supaya garis tidak bersilang. Kotak bergaris putus-putus kuning = usulan.

![DFD-2.7](assets/dfd-2-7.svg)

```plantuml
@startuml dfd-2-7
!include dfd-style.iuml
left to right direction
skinparam nodesep 12
skinparam ranksep 35
rectangle "Verifier" <<entity>> as V_6
rectangle "D4 | Dokumen deal *" <<store>> as D4_6
rectangle "Financier *" <<entity>> as F_5
rectangle "D10 | Hasil pindai\npapan *" <<store>> as D10_5
rectangle "D4 | Dokumen deal *" <<store>> as D4_5
rectangle "D4 | Dokumen deal *" <<store>> as D4_4
rectangle "D4 | Dokumen deal *" <<store>> as D4_3
rectangle "D10 | Hasil pindai\npapan *" <<store>> as D10_3
rectangle "Financier" <<entity>> as F_2
rectangle "D11 | Status deal\n(state machine) *" <<store>> as D11_2
rectangle "D11 | Status deal\n(state machine)" <<store>> as D11_1
rectangle "D4 | Dokumen deal" <<store>> as D4_1
rectangle "D10 | Hasil pindai\npapan" <<store>> as D10_1
rectangle "**7.6**\nSerahkan bukti" <<process>> as P6
rectangle "**7.5**\nVerifikasi bukti" <<process>> as P5
rectangle "**7.4**\nSusun bukti JTSP" <<process>> as P4
rectangle "**7.3**\nKumpulkan\ndua entri" <<process>> as P3
rectangle "**7.2**\nHentikan sebelum\nbayar" <<process>> as P2
rectangle "**7.1**\nLookup dengan\nkey supplier" <<process>> as P1
rectangle "F7.01 records" <<flow>> as f_F7_01
rectangle "F7.02 N, supplier_pk,\nentri ditawarkan" <<flow>> as f_F7_02
rectangle "F7.03 Stopped: AlreadyFinanced\n/ DoubleFinanced" <<flow>> as f_F7_03
rectangle "F7.04 status Stopped" <<flow>> as f_F7_04
rectangle "F7.05 berhenti,\ntanpa transaksi" <<flow>> as f_F7_05
rectangle "F7.06 entri pertama\n+ posisi" <<flow>> as f_F7_06
rectangle "F7.07 entri yang\nditawarkan" <<flow>> as f_F7_07
rectangle "F7.08 pasangan entri" <<flow>> as f_F7_08
rectangle "F7.09 invoice, sig_buyer,\npasangan entri" <<flow>> as f_F7_09
rectangle "F7.10 bukti JTSP" <<flow>> as f_F7_10
rectangle "F7.11 bukti" <<flow>> as f_F7_11
rectangle "F7.12 posisi di papan" <<flow>> as f_F7_12
rectangle "F7.13 Caught: supplier\nmenandatangani dua kali" <<flow>> as f_F7_13
rectangle "F7.14 bukti" <<flow>> as f_F7_14
rectangle "F7.15 bukti (unduh)" <<flow>> as f_F7_15
P1 <-- f_F7_01
f_F7_01 -- D10_1
P1 <-- f_F7_02
f_F7_02 -- D4_1
P1 -- f_F7_03
f_F7_03 --> D11_1
P2 <-- f_F7_04
f_F7_04 -- D11_2
F_2 <-- f_F7_05
f_F7_05 -- P2
P3 <-- f_F7_06
f_F7_06 -- D10_3
P3 <-- f_F7_07
f_F7_07 -- D4_3
P3 -- f_F7_08
f_F7_08 --> D4_3
P4 <-- f_F7_09
f_F7_09 -- D4_4
P4 -- f_F7_10
f_F7_10 --> D4_4
P5 <-- f_F7_11
f_F7_11 -- D4_5
P5 <-- f_F7_12
f_F7_12 -- D10_5
F_5 <-- f_F7_13
f_F7_13 -- P5
P6 <-- f_F7_14
f_F7_14 -- D4_6
V_6 <-- f_F7_15
f_F7_15 -- P6
rectangle " " <<spacer>> as sp_P1_a
rectangle " " <<spacer>> as sp_P1_b
sp_P1_a -[hidden]- sp_P1_b
sp_P1_b -[hidden]- P1
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
| 7.1 Lookup dengan key supplier | Hanya pemegang invoice bisa memverifikasi tanda tangan supplier; entri lain diabaikan | ADA | `lookup` |
| 7.2 Hentikan sebelum bayar | `Stopped` tidak pernah memindahkan uang | ADA | `Flow::on_board`, `Stop` |
| 7.3 Kumpulkan dua entri | Entri pertama dari papan (dengan posisi) + entri yang ditawarkan supplier (boleh tidak di papan) | ADA | `EntryAt` |
| 7.4 Susun bukti JTSP | Invoice + tanda tangan buyer + dua entri dengan komitmen berbeda | ADA | wasm `doubleSignProof` |
| 7.5 Verifikasi bukti | Offline; posisi yang diklaim dicek terhadap papan | ADA | wasm `verifyProof`, `verify_proof_on_board` |
| 7.6 Serahkan bukti | Unduh di layar Verify; hanya ke pihak berwenang | ADA | `src/pages/verify.ts` |

## Aliran data

| Aliran | Dari | Ke | Data |
|---|---|---|---|
| F7.01 | D10 | Hasil pindai papan | 7.1 Lookup dengan key supplier | records |
| F7.02 | D4 | Dokumen deal | 7.1 Lookup dengan key supplier | N, supplier_pk, entri ditawarkan |
| F7.03 | 7.1 Lookup dengan key supplier | D11 | Status deal (state machine) | Stopped: AlreadyFinanced / DoubleFinanced |
| F7.04 | D11 | Status deal (state machine) | 7.2 Hentikan sebelum bayar | status Stopped |
| F7.05 | 7.2 Hentikan sebelum bayar | Financier | berhenti, tanpa transaksi |
| F7.06 | D10 | Hasil pindai papan | 7.3 Kumpulkan dua entri | entri pertama + posisi |
| F7.07 | D4 | Dokumen deal | 7.3 Kumpulkan dua entri | entri yang ditawarkan |
| F7.08 | 7.3 Kumpulkan dua entri | D4 | Dokumen deal | pasangan entri |
| F7.09 | D4 | Dokumen deal | 7.4 Susun bukti JTSP | invoice, sig_buyer, pasangan entri |
| F7.10 | 7.4 Susun bukti JTSP | D4 | Dokumen deal | bukti JTSP |
| F7.11 | D4 | Dokumen deal | 7.5 Verifikasi bukti | bukti |
| F7.12 | D10 | Hasil pindai papan | 7.5 Verifikasi bukti | posisi di papan |
| F7.13 | 7.5 Verifikasi bukti | Financier | Caught: supplier menandatangani dua kali |
| F7.14 | D4 | Dokumen deal | 7.6 Serahkan bukti | bukti |
| F7.15 | 7.6 Serahkan bukti | Verifier | bukti (unduh) |
