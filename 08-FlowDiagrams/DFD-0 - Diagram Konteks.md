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
rectangle "K1 credential, PRF,\nassertion" <<flow>> as k1
rectangle "K2 create(), get(),\nchallenge" <<flow>> as k2
rectangle "K3 daftar/masuk, invoice,\npenawaran, keputusan" <<flow>> as k3
rectangle "K4 kartu kontak, rincian\nentri, isi surat, status" <<flow>> as k4
rectangle "K5 daftar/masuk, keputusan,\npersetujuan riwayat" <<flow>> as k5
rectangle "K6 invoice, isi surat,\nQR, status" <<flow>> as k6
rectangle "K7 pairing, syarat, surat,\npolicy, perintah root" <<flow>> as k7
rectangle "K8 status papan, pelunasan,\nriwayat, Caught" <<flow>> as k8
rectangle "**0**\nSistem JitsuinFi\n\nweb app + jitsuin-wasm, relay dokumen,\nnode financier, papan registry" <<process>> as P
rectangle "K9 verdict, indeks,\nbukti, bundel" <<flow>> as k9
rectangle "K10 UFVK papan, bukti,\nbundel, snapshot" <<flow>> as k10
rectangle "K11 kuitansi,\nlaporan" <<flow>> as k11
rectangle "K12 daftar/masuk, UFVK,\npolicy, id setoran" <<flow>> as k12
rectangle "K13 tx advance\nshielded" <<flow>> as k13
rectangle "K14 blok, tip, urutan tx,\npembayaran, setoran" <<flow>> as k14
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
| K1 | Authenticator | Sistem | Credential, output PRF, assertion | F1 |
| K2 | Sistem | Authenticator | `create()`, `get()` dengan salt per peran, challenge | F2 |
| K3 | Supplier | Sistem | Daftar/masuk dan stempel, data invoice + file syarat, penawaran, keputusan setuju, nominal di Zodl | F8, F17, F27, F45 |
| K4 | Sistem | Supplier | Kartu kontak, backup key (saat ini), rincian entri, isi surat, status advance, status pelunasan | F9, F18, F28, F46, F61 |
| K5 | Buyer | Sistem | Daftar/masuk dan stempel, file syarat, keputusan, minta QR, persetujuan riwayat | F3, F15, F42, F58, F71 |
| K6 | Sistem | Buyer | Kartu kontak, isi invoice, isi surat, QR ZIP-321, status, permintaan riwayat | F4, F16, F43, F59, F72 |
| K7 | Financier | Sistem | Daftar/masuk, pairing node, syarat deal, PDF surat + alamat bayar, permintaan riwayat + policy, buat bundel, perintah root | F5, F25, F44, F73, F88, F96 |
| K8 | Sistem | Financier | Kartu kontak, sesi konsol, status cek papan, status pelunasan + bukti sengketa, laporan riwayat, berhenti / Caught | F6, F26, F60, F74, F82 |
| K9 | Sistem | Verifier | Bukti JTSP, verdict, indeks bunga, bundel, snapshot | F83, F90 |
| K10 | Verifier | Sistem | UFVK papan, bukti, bundel, k, memo, snapshot | F89 |
| K11 | Sistem | Anggota dana | Kuitansi setoran, laporan solvabilitas | F98 |
| K12 | Anggota dana | Sistem | Daftar/masuk, UFVK + `manager_pk`, policy, id setoran | F7, F97 |
| K13 | Sistem | Jaringan Zcash | Transaksi advance shielded | F47 |
| K14 | Jaringan Zcash | Sistem | Blok, tinggi tip, urutan tx, waktu blok, pembayaran pelunasan, setoran | F29, F62, F91, F99 |

Nomor F merujuk tabel aliran [[DFD-1 - Proses Utama]]. Posting ke papan (entri register, entri `settled`) dan root kewajiban digambar sebagai tulisan ke penyimpanan D1 dan D6 di dalam sistem; secara fisik keduanya adalah transaksi shielded ke jaringan Zcash (10 000 zat + fee ZIP-317 per posting).
