---
tags: [flow, dfd]
status: DRAF
updated: 2026-10-19
---

# DFD-2.5 - Pelunasan dan Settled

**Bagian dari:** [[08 - FlowDiagrams]] · Legenda: [[FD-00 - Arsitektur Target dan Legenda]] · Induk: [[DFD-1 - Proses Utama]] · Sequence: [[SEQ-02 - Buyer]] · [[SEQ-03 - Financier]]

Proses 5.0 dirinci: buyer membayar lewat QR ZIP-321 yang membawa kuitansi dan klaim; watchdog financier mencocokkan pembayaran, menghitung status, dan mem-posting entri `settled` dua tanda tangan. Dasar: wasm `buyerRepayment`, `bundleOnBoard`; `jitsuin-flow::buyer::repayment_request`; `jitsuin-flow::settlement` (`repayment`, `Repayment::status`, `covering_height`, `settle`, `post_settled`).

Kotak bertanda `*` adalah entitas atau penyimpanan yang sama yang digambar ulang di jalur proses lain, supaya garis tidak bersilang. Kotak bergaris putus-putus kuning = usulan.

![DFD-2.5](assets/dfd-2-5.svg)

```plantuml
@startuml dfd-2-5
!include dfd-style.iuml
left to right direction
skinparam nodesep 12
skinparam ranksep 35
rectangle "Buyer *" <<entity>> as B_7
rectangle "D4 | Dokumen deal *" <<store>> as D4_7
rectangle "D12 | Snapshot papan\n(relay)" <<storeproposal>> as D12_7
rectangle "D1 | Papan registry" <<store>> as D1_6
rectangle "Jaringan Zcash\n(lightwalletd) *" <<entity>> as Z_6
rectangle "D2 | Wallet dan\nkey financier *" <<store>> as D2_6
rectangle "D11 | Status deal\n(state machine) *" <<store>> as D11_6
rectangle "D2 | Wallet dan\nkey financier *" <<store>> as D2_5
rectangle "D10 | Hasil pindai\npapan" <<store>> as D10_5
rectangle "Jaringan Zcash\n(lightwalletd) *" <<entity>> as Z_5
rectangle "D11 | Status deal\n(state machine) *" <<store>> as D11_5
rectangle "Financier" <<entity>> as F_4
rectangle "D4 | Dokumen deal *" <<store>> as D4_4
rectangle "D11 | Status deal\n(state machine) *" <<store>> as D11_4
rectangle "D11 | Status deal\n(state machine)" <<store>> as D11_3
rectangle "D4 | Dokumen deal *" <<store>> as D4_3
rectangle "D2 | Wallet dan\nkey financier *" <<store>> as D2_3
rectangle "D2 | Wallet dan\nkey financier" <<store>> as D2_2
rectangle "Jaringan Zcash\n(lightwalletd)" <<entity>> as Z_2
rectangle "D3 | Key sesi\n(memori tab)" <<store>> as D3_1
rectangle "D4 | Dokumen deal" <<store>> as D4_1
rectangle "Buyer" <<entity>> as B_1
rectangle "**5.7**\nCek status\ndi papan" <<process>> as P7
rectangle "**5.6**\nPosting settled" <<process>> as P6
rectangle "**5.5**\nCountersign\nsettled" <<process>> as P5
rectangle "**5.4**\nHitung status" <<process>> as P4
rectangle "**5.3**\nCocokkan\npembayaran" <<process>> as P3
rectangle "**5.2**\nSinkron wallet\nfinancier" <<process>> as P2
rectangle "**5.1**\nBuat permintaan\nbayar (QR)" <<process>> as P1
rectangle "F5.01 minta QR" <<flow>> as f_F5_01
rectangle "F5.02 invoice, surat" <<flow>> as f_F5_02
rectangle "F5.03 key invoice buyer" <<flow>> as f_F5_03
rectangle "F5.04 QR ZIP-321:\nalamat, nominal, memo" <<flow>> as f_F5_04
rectangle "F5.05 tx masuk, memo" <<flow>> as f_F5_05
rectangle "F5.06 tx tersinkron" <<flow>> as f_F5_06
rectangle "F5.07 tx + memo" <<flow>> as f_F5_07
rectangle "F5.08 dokumen pelunasan,\nbuyer_pk" <<flow>> as f_F5_08
rectangle "F5.09 paid, pending,\nklaim, ditolak" <<flow>> as f_F5_09
rectangle "F5.10 repayment" <<flow>> as f_F5_10
rectangle "F5.11 jatuh tempo,\ntenggang" <<flow>> as f_F5_11
rectangle "F5.12 Unpaid ... Settled /\nDisputed / Overdue" <<flow>> as f_F5_12
rectangle "F5.13 status, sengketa" <<flow>> as f_F5_13
rectangle "F5.14 Settled, klaim buyer" <<flow>> as f_F5_14
rectangle "F5.15 waktu blok\npembayaran penutup" <<flow>> as f_F5_15
rectangle "F5.16 settled yang\nsudah ada" <<flow>> as f_F5_16
rectangle "F5.17 key financier" <<flow>> as f_F5_17
rectangle "F5.18 entri settled\n(flag tepat/terlambat)" <<flow>> as f_F5_18
rectangle "F5.19 entri settled" <<flow>> as f_F5_19
rectangle "F5.20 wallet" <<flow>> as f_F5_20
rectangle "F5.21 tx 10 000 zat\n+ memo settled" <<flow>> as f_F5_21
rectangle "F5.22 entri settled\n(dua tanda tangan)" <<flow>> as f_F5_22
rectangle "F5.23 snapshot papan" <<flow>> as f_F5_23
rectangle "F5.24 bundel / dokumen\npelunasan" <<flow>> as f_F5_24
rectangle "F5.25 Registered,\nsettled on_time" <<flow>> as f_F5_25
B_1 -- f_F5_01
f_F5_01 --> P1
P1 <-- f_F5_02
f_F5_02 -- D4_1
P1 <-- f_F5_03
f_F5_03 -- D3_1
B_1 <-- f_F5_04
f_F5_04 -- P1
Z_2 -- f_F5_05
f_F5_05 --> P2
P2 -- f_F5_06
f_F5_06 --> D2_2
P3 <-- f_F5_07
f_F5_07 -- D2_3
P3 <-- f_F5_08
f_F5_08 -- D4_3
P3 -- f_F5_09
f_F5_09 --> D11_3
P4 <-- f_F5_10
f_F5_10 -- D11_4
P4 <-- f_F5_11
f_F5_11 -- D4_4
P4 -- f_F5_12
f_F5_12 --> D11_4
F_4 <-- f_F5_13
f_F5_13 -- P4
P5 <-- f_F5_14
f_F5_14 -- D11_5
Z_5 -- f_F5_15
f_F5_15 --> P5
P5 <-- f_F5_16
f_F5_16 -- D10_5
P5 <-- f_F5_17
f_F5_17 -- D2_5
P5 -- f_F5_18
f_F5_18 --> D11_5
P6 <-- f_F5_19
f_F5_19 -- D11_6
P6 <-- f_F5_20
f_F5_20 -- D2_6
Z_6 <-- f_F5_21
f_F5_21 -- P6
P6 -- f_F5_22
f_F5_22 --> D1_6
P7 <-- f_F5_23
f_F5_23 -- D12_7
P7 <-- f_F5_24
f_F5_24 -- D4_7
B_7 <-- f_F5_25
f_F5_25 -- P7
rectangle " " <<spacer>> as sp_P3_a
rectangle " " <<spacer>> as sp_P3_b
sp_P3_a -[hidden]- sp_P3_b
sp_P3_b -[hidden]- P3
@enduml
```

## Proses

| Proses | Isi | Status | Kode / item |
|---|---|---|---|
| 5.1 Buat permintaan bayar | Kuitansi pelunasan JTR1 + seal klaim buyer (346 byte) di memo ZIP-321; QR hanya di layar buyer | ADA | wasm `buyerRepayment`, `repayment_request`, `qr_svg` |
| 5.2 Sinkron wallet financier | `sync` + `enhance` + `list_tx` | ADA | `Financier::repayment` |
| 5.3 Cocokkan pembayaran | Kuitansi untuk N, ditandatangani `buyer_pk`, nominal = nilai output; tertambang vs belum; klaim dikumpulkan | ADA | `settlement::repayment` |
| 5.4 Hitung status | Unpaid, Pending, Partial, Claimed, Settled, Disputed, Overdue | ADA | `Repayment::status` |
| 5.5 Countersign settled | Waktu blok pembayaran penutup menentukan flag; seal financier atas klaim buyer | ADA | `covering_height`, `lwd::block_time`, `settle` |
| 5.6 Posting settled | 10 000 zat ke papan; entri 167 byte dengan `settled_tag`, tanpa N | ADA | `post_settled` |
| 5.7 Cek status di papan | Pemegang N mencari entri settled yang valid untuk kedua key | PARSIAL (wasm ADA, snapshot USULAN P-06) | wasm `bundleOnBoard` |

## Aliran data

| Aliran | Dari | Ke | Data |
|---|---|---|---|
| F5.01 | Buyer | 5.1 Buat permintaan bayar (QR) | minta QR |
| F5.02 | D4 | Dokumen deal | 5.1 Buat permintaan bayar (QR) | invoice, surat |
| F5.03 | D3 | Key sesi (memori tab) | 5.1 Buat permintaan bayar (QR) | key invoice buyer |
| F5.04 | 5.1 Buat permintaan bayar (QR) | Buyer | QR ZIP-321: alamat, nominal, memo |
| F5.05 | Jaringan Zcash (lightwalletd) | 5.2 Sinkron wallet financier | tx masuk, memo |
| F5.06 | 5.2 Sinkron wallet financier | D2 | Wallet dan key financier | tx tersinkron |
| F5.07 | D2 | Wallet dan key financier | 5.3 Cocokkan pembayaran | tx + memo |
| F5.08 | D4 | Dokumen deal | 5.3 Cocokkan pembayaran | dokumen pelunasan, buyer_pk |
| F5.09 | 5.3 Cocokkan pembayaran | D11 | Status deal (state machine) | paid, pending, klaim, ditolak |
| F5.10 | D11 | Status deal (state machine) | 5.4 Hitung status | repayment |
| F5.11 | D4 | Dokumen deal | 5.4 Hitung status | jatuh tempo, tenggang |
| F5.12 | 5.4 Hitung status | D11 | Status deal (state machine) | Unpaid ... Settled / Disputed / Overdue |
| F5.13 | 5.4 Hitung status | Financier | status, sengketa |
| F5.14 | D11 | Status deal (state machine) | 5.5 Countersign settled | Settled, klaim buyer |
| F5.15 | Jaringan Zcash (lightwalletd) | 5.5 Countersign settled | waktu blok pembayaran penutup |
| F5.16 | D10 | Hasil pindai papan | 5.5 Countersign settled | settled yang sudah ada |
| F5.17 | D2 | Wallet dan key financier | 5.5 Countersign settled | key financier |
| F5.18 | 5.5 Countersign settled | D11 | Status deal (state machine) | entri settled (flag tepat/terlambat) |
| F5.19 | D11 | Status deal (state machine) | 5.6 Posting settled | entri settled |
| F5.20 | D2 | Wallet dan key financier | 5.6 Posting settled | wallet |
| F5.21 | 5.6 Posting settled | Jaringan Zcash (lightwalletd) | tx 10 000 zat + memo settled |
| F5.22 | 5.6 Posting settled | D1 | Papan registry | entri settled (dua tanda tangan) |
| F5.23 | D12 | Snapshot papan (relay) | 5.7 Cek status di papan | snapshot papan |
| F5.24 | D4 | Dokumen deal | 5.7 Cek status di papan | bundel / dokumen pelunasan |
| F5.25 | 5.7 Cek status di papan | Buyer | Registered, settled on_time |

Catatan: `financierSettle` di wasm (dipakai landing) menentukan tepat waktu dari tanggal kuitansi, sedangkan alur backend (5.5) memakai waktu blok. Lihat [[Pra-review Spesifikasi dan Threat Model]] Spec #5.
