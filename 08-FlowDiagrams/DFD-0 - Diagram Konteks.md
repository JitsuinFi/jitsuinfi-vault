---
tags: [flow, dfd]
status: DRAF
updated: 2026-10-19
---

# DFD-0 - Diagram Konteks

**Bagian dari:** [[08 - FlowDiagrams]] · Legenda: [[FD-00 - Arsitektur Target dan Legenda]] · Turunan: [[DFD-1 - Proses Utama]]

JitsuinFi sebagai satu proses dengan semua pihak di luarnya. Sistem mencakup web app + `jitsuin-wasm` (di perangkat pengguna), relay dokumen (usulan P-04), node financier (`jitsuin-flow` + wallet), dan papan registry (memo di chain yang dibaca lewat UFVK papan).

![DFD-0](assets/dfd-0.svg)

```plantuml
@startuml dfd-0
!include dfd-style.iuml
skinparam nodesep 30
skinparam ranksep 30
rectangle "Authenticator\npasskey" <<entity>> as A
rectangle "Supplier" <<entity>> as S
rectangle "Buyer" <<entity>> as B
rectangle "Financier" <<entity>> as F
rectangle "K1 output PRF,\nassertion" <<flow>> as k1
rectangle "K2 salt per peran,\nchallenge" <<flow>> as k2
rectangle "K3 invoice, entri,\nseal supplier" <<flow>> as k3
rectangle "K4 tanda tangan buyer,\nadvance + seal" <<flow>> as k4
rectangle "K5 tanda tangan,\nseal, sertifikat" <<flow>> as k5
rectangle "K6 invoice, surat,\nQR pelunasan" <<flow>> as k6
rectangle "K7 surat, syarat,\nroot kewajiban" <<flow>> as k7
rectangle "K8 cek papan, bukti,\nstatus pelunasan" <<flow>> as k8
rectangle "**0**\nSistem JitsuinFi\n\nweb app + jitsuin-wasm, relay dokumen,\nnode financier, papan registry" <<process>> as P
rectangle "K9 verdict,\nindeks bunga" <<flow>> as k9
rectangle "K10 bundel, bukti,\nUFVK papan" <<flow>> as k10
rectangle "K11 laporan\nsolvabilitas" <<flow>> as k11
rectangle "K12 UFVK akun\noperasional" <<flow>> as k12
rectangle "K13 tx shielded\n+ memo" <<flow>> as k13
rectangle "K14 blok, tx,\nmemo papan" <<flow>> as k14
rectangle "Verifier\n(juri, auditor,\norang luar)" <<entity>> as V
rectangle "Anggota dana" <<entity>> as M
rectangle "Jaringan Zcash\n(lightwalletd, chain)" <<entity>> as Z
A -down- k1
k1 -down-> P
P -up- k2
k2 -up-> A
S -down- k3
k3 -down-> P
P -up- k4
k4 -up-> S
B -down- k5
k5 -down-> P
P -up- k6
k6 -up-> B
F -down- k7
k7 -down-> P
P -up- k8
k8 -up-> F
P -down- k9
k9 -down-> V
V -up- k10
k10 -up-> P
P -down- k11
k11 -down-> M
M -up- k12
k12 -up-> P
P -down- k13
k13 -down-> Z
Z -up- k14
k14 -up-> P
@enduml
```

## Aliran data

| Aliran | Dari | Ke | Data | Di level 1 |
|---|---|---|---|---|
| K1 | Authenticator | Sistem | Output PRF (32 byte per salt), assertion WebAuthn | F1 |
| K2 | Sistem | Authenticator | Salt per peran, challenge | F2 |
| K3 | Supplier | Sistem | Daftar/masuk, data invoice + file syarat, penawaran, entri bertanda tangan, seal supplier | F3, F8, F12, F23 |
| K4 | Sistem | Supplier | Pembuka komitmen, surat pengalihan, advance + seal financier | F13, F22 |
| K5 | Buyer | Sistem | Daftar/masuk, tanda tangan invoice, seal buyer, sertifikat riwayat | F4, F10, F25, F40 |
| K6 | Sistem | Buyer | Invoice, surat pengalihan, QR ZIP-321 | F9, F24, F35 |
| K7 | Financier | Sistem | Daftar/masuk, syarat deal, surat pengalihan, root kewajiban (manajer dana) | F5, F14, F21, F55 |
| K8 | Sistem | Financier | Status cek papan, status pelunasan, laporan riwayat, bukti JTSP | F15, F39, F45, F48 |
| K9 | Sistem | Verifier | Verdict bukti dan bundel, indeks bunga | F50 |
| K10 | Verifier | Sistem | Bundel JTSB, bukti JTSP, UFVK papan | F49 |
| K11 | Sistem | Anggota dana | Laporan solvabilitas | F53 |
| K12 | Anggota dana | Sistem | UFVK akun operasional | F52 |
| K13 | Sistem | Jaringan Zcash | Transaksi shielded: entri papan, advance, entri settled, root kewajiban | F30 (+ posting di 3.0, 5.0, 9.0) |
| K14 | Jaringan Zcash | Sistem | Blok, transaksi penuh dan memo, urutan tx, tinggi tip, pembayaran pelunasan | F36 (+ pindai di 3.0, 8.0) |

Nomor F di kolom terakhir merujuk tabel aliran [[DFD-1 - Proses Utama]]. Di level 1, posting ke papan digambar sebagai tulisan ke penyimpanan D1 (Papan registry), yang secara fisik adalah transaksi di jaringan Zcash.
