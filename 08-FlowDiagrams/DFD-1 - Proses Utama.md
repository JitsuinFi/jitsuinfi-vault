---
tags: [flow, dfd]
status: DRAF
updated: 2026-10-19
---

# DFD-1 - Proses Utama

**Bagian dari:** [[08 - FlowDiagrams]] · Legenda: [[FD-00 - Arsitektur Target dan Legenda]] · Induk: [[DFD-0 - Diagram Konteks]]

Sembilan proses utama JitsuinFi. Diagram ini logis: aliran antarpihak (misalnya invoice dari supplier ke buyer) secara fisik melewati kotak surat terenkripsi (D7, usulan P-04), dan state financier disimpan di D10/D11; keduanya digambar di level 2. Satu jalur = satu proses; entitas dan penyimpanan bertanda `*` digambar ulang supaya garis tidak bersilang.

![DFD-1](assets/dfd-1.svg)

```plantuml
@startuml dfd-1
!include dfd-style.iuml
left to right direction
skinparam nodesep 12
skinparam ranksep 35
rectangle "Financier *" <<entity>> as F_9
rectangle "D6 | Akun dana *" <<store>> as D6_9
rectangle "Anggota dana" <<entity>> as M_9
rectangle "D1 | Papan registry *" <<store>> as D1_8
rectangle "Verifier" <<entity>> as V_8
rectangle "Financier *" <<entity>> as F_7
rectangle "D1 | Papan registry *" <<store>> as D1_7
rectangle "D4 | Dokumen deal *" <<store>> as D4_7
rectangle "Financier *" <<entity>> as F_6
rectangle "D4 | Dokumen deal *" <<store>> as D4_6
rectangle "D1 | Papan registry *" <<store>> as D1_6
rectangle "D5 | Allowlist\ndan policy" <<store>> as D5_6
rectangle "D3 | Key sesi\n(memori tab) *" <<store>> as D3_6
rectangle "Buyer *" <<entity>> as B_6
rectangle "Financier *" <<entity>> as F_5
rectangle "D1 | Papan registry *" <<store>> as D1_5
rectangle "D2 | Wallet dan\nkey financier *" <<store>> as D2_5
rectangle "Jaringan Zcash\n(lightwalletd) *" <<entity>> as Z_5
rectangle "Buyer *" <<entity>> as B_5
rectangle "D3 | Key sesi\n(memori tab) *" <<store>> as D3_5
rectangle "D4 | Dokumen deal *" <<store>> as D4_5
rectangle "D6 | Akun dana" <<store>> as D6_4
rectangle "Jaringan Zcash\n(lightwalletd)" <<entity>> as Z_4
rectangle "D1 | Papan registry *" <<store>> as D1_4
rectangle "D2 | Wallet dan\nkey financier *" <<store>> as D2_4
rectangle "D4 | Dokumen deal *" <<store>> as D4_4
rectangle "D3 | Key sesi\n(memori tab) *" <<store>> as D3_4
rectangle "Buyer *" <<entity>> as B_4
rectangle "Supplier *" <<entity>> as S_4
rectangle "Financier *" <<entity>> as F_4
rectangle "D1 | Papan registry" <<store>> as D1_3
rectangle "D2 | Wallet dan\nkey financier" <<store>> as D2_3
rectangle "D4 | Dokumen deal *" <<store>> as D4_3
rectangle "Financier *" <<entity>> as F_3
rectangle "Supplier *" <<entity>> as S_3
rectangle "D4 | Dokumen deal" <<store>> as D4_2
rectangle "Buyer *" <<entity>> as B_2
rectangle "Supplier *" <<entity>> as S_2
rectangle "D3 | Key sesi\n(memori tab) *" <<store>> as D3_2
rectangle "D3 | Key sesi\n(memori tab)" <<store>> as D3_1
rectangle "Financier" <<entity>> as F_1
rectangle "Buyer" <<entity>> as B_1
rectangle "Supplier" <<entity>> as S_1
rectangle "Authenticator\npasskey" <<entity>> as A_1
rectangle "**9.0**\nSolvabilitas dana" <<process>> as P9
rectangle "**8.0**\nVerifikasi dan\nindeks publik" <<process>> as P8
rectangle "**7.0**\nDeteksi pembiayaan\nganda" <<process>> as P7
rectangle "**6.0**\nRiwayat buyer" <<process>> as P6
rectangle "**5.0**\nPelunasan dan\nsettled" <<process>> as P5
rectangle "**4.0**\nPengalihan dan\nadvance" <<process>> as P4
rectangle "**3.0**\nRegistrasi papan" <<process>> as P3
rectangle "**2.0**\nTerbitkan dan\ntandatangani invoice" <<process>> as P2
rectangle "**1.0**\nIdentitas, sesi,\nkotak surat" <<process>> as P1
rectangle "F1 output PRF,\nassertion" <<flow>> as f_F1
rectangle "F2 salt peran,\nchallenge" <<flow>> as f_F2
rectangle "F3 daftar, masuk" <<flow>> as f_F3
rectangle "F4 daftar, masuk" <<flow>> as f_F4
rectangle "F5 daftar, masuk" <<flow>> as f_F5
rectangle "F6 key turunan" <<flow>> as f_F6
rectangle "F7 key supplier,\nkey buyer" <<flow>> as f_F7
rectangle "F8 data invoice,\nfile syarat" <<flow>> as f_F8
rectangle "F9 invoice" <<flow>> as f_F9
rectangle "F10 tanda tangan\nbuyer" <<flow>> as f_F10
rectangle "F11 invoice + tanda\ntangan, N" <<flow>> as f_F11
rectangle "F12 penawaran, entri\nbertanda tangan" <<flow>> as f_F12
rectangle "F13 pembuka\nkomitmen" <<flow>> as f_F13
rectangle "F14 syarat deal" <<flow>> as f_F14
rectangle "F15 status cek\npapan" <<flow>> as f_F15
rectangle "F16 invoice, N,\ntag riwayat" <<flow>> as f_F16
rectangle "F17 wallet" <<flow>> as f_F17
rectangle "F18 entri register" <<flow>> as f_F18
rectangle "F19 memo papan" <<flow>> as f_F19
rectangle "F20 entri terkonfirmasi,\nentri ditolak" <<flow>> as f_F20
rectangle "F21 surat\npengalihan" <<flow>> as f_F21
rectangle "F22 surat, advance\n+ seal" <<flow>> as f_F22
rectangle "F23 seal supplier" <<flow>> as f_F23
rectangle "F24 surat" <<flow>> as f_F24
rectangle "F25 seal buyer" <<flow>> as f_F25
rectangle "F26 key seal" <<flow>> as f_F26
rectangle "F27 entri\nterkonfirmasi" <<flow>> as f_F27
rectangle "F28 key financier,\nwallet" <<flow>> as f_F28
rectangle "F29 cek papan\nterakhir" <<flow>> as f_F29
rectangle "F30 tx advance\n+ memo" <<flow>> as f_F30
rectangle "F31 surat + seal" <<flow>> as f_F31
rectangle "F32 advance + catatan\npiutang (dana)" <<flow>> as f_F32
rectangle "F33 surat (alamat,\nnominal)" <<flow>> as f_F33
rectangle "F34 key buyer" <<flow>> as f_F34
rectangle "F35 QR ZIP-321" <<flow>> as f_F35
rectangle "F36 pembayaran\nmasuk" <<flow>> as f_F36
rectangle "F37 tx wallet" <<flow>> as f_F37
rectangle "F38 entri settled" <<flow>> as f_F38
rectangle "F39 status\npelunasan" <<flow>> as f_F39
rectangle "F40 sertifikat\n(persetujuan)" <<flow>> as f_F40
rectangle "F41 key identitas" <<flow>> as f_F41
rectangle "F42 allowlist,\nstandar minimal" <<flow>> as f_F42
rectangle "F43 entri bertag,\nsettled" <<flow>> as f_F43
rectangle "F44 tag riwayat" <<flow>> as f_F44
rectangle "F45 laporan riwayat" <<flow>> as f_F45
rectangle "F46 entri ditolak +\nentri ditawarkan" <<flow>> as f_F46
rectangle "F47 entri pertama" <<flow>> as f_F47
rectangle "F48 bukti JTSP" <<flow>> as f_F48
rectangle "F49 bundel, bukti,\nUFVK papan" <<flow>> as f_F49
rectangle "F50 verdict,\nindeks bunga" <<flow>> as f_F50
rectangle "F51 memo papan" <<flow>> as f_F51
rectangle "F52 UFVK akun\noperasional" <<flow>> as f_F52
rectangle "F53 laporan\nsolvabilitas" <<flow>> as f_F53
rectangle "F54 transaksi\nakun dana" <<flow>> as f_F54
rectangle "F55 root kewajiban\n(manajer)" <<flow>> as f_F55
rectangle "F56 root JTLR" <<flow>> as f_F56
A_1 -- f_F1
f_F1 --> P1
A_1 <-- f_F2
f_F2 -- P1
S_1 -- f_F3
f_F3 --> P1
B_1 -- f_F4
f_F4 --> P1
F_1 -- f_F5
f_F5 --> P1
P1 -- f_F6
f_F6 --> D3_1
P2 <-- f_F7
f_F7 -- D3_2
S_2 -- f_F8
f_F8 --> P2
B_2 <-- f_F9
f_F9 -- P2
B_2 -- f_F10
f_F10 --> P2
P2 -- f_F11
f_F11 --> D4_2
S_3 -- f_F12
f_F12 --> P3
S_3 <-- f_F13
f_F13 -- P3
F_3 -- f_F14
f_F14 --> P3
F_3 <-- f_F15
f_F15 -- P3
P3 <-- f_F16
f_F16 -- D4_3
P3 <-- f_F17
f_F17 -- D2_3
P3 -- f_F18
f_F18 --> D1_3
P3 <-- f_F19
f_F19 -- D1_3
P3 -- f_F20
f_F20 --> D4_3
F_4 -- f_F21
f_F21 --> P4
S_4 <-- f_F22
f_F22 -- P4
S_4 -- f_F23
f_F23 --> P4
B_4 <-- f_F24
f_F24 -- P4
B_4 -- f_F25
f_F25 --> P4
P4 <-- f_F26
f_F26 -- D3_4
P4 <-- f_F27
f_F27 -- D4_4
P4 <-- f_F28
f_F28 -- D2_4
P4 <-- f_F29
f_F29 -- D1_4
Z_4 <-- f_F30
f_F30 -- P4
P4 -- f_F31
f_F31 --> D4_4
P4 -- f_F32
f_F32 --> D6_4
P5 <-- f_F33
f_F33 -- D4_5
P5 <-- f_F34
f_F34 -- D3_5
B_5 <-- f_F35
f_F35 -- P5
Z_5 -- f_F36
f_F36 --> P5
P5 <-- f_F37
f_F37 -- D2_5
P5 -- f_F38
f_F38 --> D1_5
F_5 <-- f_F39
f_F39 -- P5
B_6 -- f_F40
f_F40 --> P6
P6 <-- f_F41
f_F41 -- D3_6
P6 <-- f_F42
f_F42 -- D5_6
P6 <-- f_F43
f_F43 -- D1_6
P6 -- f_F44
f_F44 --> D4_6
F_6 <-- f_F45
f_F45 -- P6
P7 <-- f_F46
f_F46 -- D4_7
P7 <-- f_F47
f_F47 -- D1_7
F_7 <-- f_F48
f_F48 -- P7
V_8 -- f_F49
f_F49 --> P8
V_8 <-- f_F50
f_F50 -- P8
P8 <-- f_F51
f_F51 -- D1_8
M_9 -- f_F52
f_F52 --> P9
M_9 <-- f_F53
f_F53 -- P9
P9 <-- f_F54
f_F54 -- D6_9
F_9 -- f_F55
f_F55 --> P9
P9 -- f_F56
f_F56 --> D6_9
@enduml
```

## Proses

| Proses | Isi | Status | Kode / item |
|---|---|---|---|
| 1.0 Identitas, sesi, kotak surat | Daftar dan masuk dengan passkey, turunkan key per peran, kunci sesi, kotak surat terenkripsi | PARSIAL (buyer ADA; P-01 – P-07) | [[DFD-2.1 - Identitas dan Sesi]] |
| 2.0 Terbitkan dan tandatangani invoice | Invoice kanonik, N, tanda tangan buyer | ADA (core, wasm); relay USULAN | [[DFD-2.2 - Penerbitan dan Tanda Tangan Invoice]] |
| 3.0 Registrasi papan | Cek papan, entri bertanda tangan supplier, posting, konfirmasi | ADA (flow); API USULAN | [[DFD-2.3 - Registrasi Papan]] |
| 4.0 Pengalihan dan advance | Surat pengalihan, seal berantai, Sign-to-Pay | ADA (flow, wasm) | [[DFD-2.4 - Pengalihan dan Advance]] |
| 5.0 Pelunasan dan settled | QR ZIP-321, watchdog, entri settled dua tanda tangan | ADA (flow, wasm) | [[DFD-2.5 - Pelunasan dan Settled]] |
| 6.0 Riwayat buyer | Sertifikat berantai, jangkar papan, standar minimal | ADA (core, flow, wasm) | [[DFD-2.6 - Riwayat Buyer]] |
| 7.0 Deteksi pembiayaan ganda | Berhenti sebelum bayar, bukti tanda tangan ganda | ADA | [[DFD-2.7 - Deteksi Pembiayaan Ganda]] |
| 8.0 Verifikasi dan indeks publik | `jitsuin verify`, `jitsuin index`, layar Verify, halaman orang luar | ADA (CLI, wasm); snapshot USULAN | [[DFD-2.8 - Verifikasi dan Indeks Publik]] |
| 9.0 Solvabilitas dana | Root kewajiban, tampilan dana, uji solvabilitas (stretch) | PARSIAL | [[DFD-2.9 - Solvabilitas Dana]] |

## Penyimpanan data (semua level)

D1–D6 muncul di level 1; D7–D17 hanya di level 2 (lokal di dalam satu proses, atau lapisan fisik dari aliran logis level 1).

| Penyimpanan | Isi | Status |
|---|---|---|
| D1 | Papan registry | ADA |
| D2 | Wallet dan key financier | ADA |
| D3 | Key sesi (memori tab) | ADA |
| D4 | Dokumen deal | ADA |
| D5 | Allowlist dan policy | ADA |
| D6 | Akun dana | ADA |
| D7 | Kotak surat terenkripsi | USULAN |
| D8 | Profil lokal (non-rahasia) | USULAN |
| D9 | Credential terdaftar di node | USULAN |
| D10 | Hasil pindai papan | ADA |
| D11 | Status deal (state machine) | ADA |
| D12 | Snapshot papan (relay) | USULAN |
| D13 | Rantai sertifikat buyer | USULAN |
| D14 | Wallet watch-only papan | ADA |
| D15 | Merkle sum tree kewajiban | USULAN |
| D16 | Wallet watch-only dana | ADA |
| D17 | Tampilan dana (lokal) | ADA |

## Aliran data

| Aliran | Dari | Ke | Data |
|---|---|---|---|
| F1 | Authenticator passkey | 1.0 Identitas, sesi, kotak surat | output PRF, assertion |
| F2 | 1.0 Identitas, sesi, kotak surat | Authenticator passkey | salt peran, challenge |
| F3 | Supplier | 1.0 Identitas, sesi, kotak surat | daftar, masuk |
| F4 | Buyer | 1.0 Identitas, sesi, kotak surat | daftar, masuk |
| F5 | Financier | 1.0 Identitas, sesi, kotak surat | daftar, masuk |
| F6 | 1.0 Identitas, sesi, kotak surat | D3 | Key sesi (memori tab) | key turunan |
| F7 | D3 | Key sesi (memori tab) | 2.0 Terbitkan dan tandatangani invoice | key supplier, key buyer |
| F8 | Supplier | 2.0 Terbitkan dan tandatangani invoice | data invoice, file syarat |
| F9 | 2.0 Terbitkan dan tandatangani invoice | Buyer | invoice |
| F10 | Buyer | 2.0 Terbitkan dan tandatangani invoice | tanda tangan buyer |
| F11 | 2.0 Terbitkan dan tandatangani invoice | D4 | Dokumen deal | invoice + tanda tangan, N |
| F12 | Supplier | 3.0 Registrasi papan | penawaran, entri bertanda tangan |
| F13 | 3.0 Registrasi papan | Supplier | pembuka komitmen |
| F14 | Financier | 3.0 Registrasi papan | syarat deal |
| F15 | 3.0 Registrasi papan | Financier | status cek papan |
| F16 | D4 | Dokumen deal | 3.0 Registrasi papan | invoice, N, tag riwayat |
| F17 | D2 | Wallet dan key financier | 3.0 Registrasi papan | wallet |
| F18 | 3.0 Registrasi papan | D1 | Papan registry | entri register |
| F19 | D1 | Papan registry | 3.0 Registrasi papan | memo papan |
| F20 | 3.0 Registrasi papan | D4 | Dokumen deal | entri terkonfirmasi, entri ditolak |
| F21 | Financier | 4.0 Pengalihan dan advance | surat pengalihan |
| F22 | 4.0 Pengalihan dan advance | Supplier | surat, advance + seal |
| F23 | Supplier | 4.0 Pengalihan dan advance | seal supplier |
| F24 | 4.0 Pengalihan dan advance | Buyer | surat |
| F25 | Buyer | 4.0 Pengalihan dan advance | seal buyer |
| F26 | D3 | Key sesi (memori tab) | 4.0 Pengalihan dan advance | key seal |
| F27 | D4 | Dokumen deal | 4.0 Pengalihan dan advance | entri terkonfirmasi |
| F28 | D2 | Wallet dan key financier | 4.0 Pengalihan dan advance | key financier, wallet |
| F29 | D1 | Papan registry | 4.0 Pengalihan dan advance | cek papan terakhir |
| F30 | 4.0 Pengalihan dan advance | Jaringan Zcash (lightwalletd) | tx advance + memo |
| F31 | 4.0 Pengalihan dan advance | D4 | Dokumen deal | surat + seal |
| F32 | 4.0 Pengalihan dan advance | D6 | Akun dana | advance + catatan piutang (dana) |
| F33 | D4 | Dokumen deal | 5.0 Pelunasan dan settled | surat (alamat, nominal) |
| F34 | D3 | Key sesi (memori tab) | 5.0 Pelunasan dan settled | key buyer |
| F35 | 5.0 Pelunasan dan settled | Buyer | QR ZIP-321 |
| F36 | Jaringan Zcash (lightwalletd) | 5.0 Pelunasan dan settled | pembayaran masuk |
| F37 | D2 | Wallet dan key financier | 5.0 Pelunasan dan settled | tx wallet |
| F38 | 5.0 Pelunasan dan settled | D1 | Papan registry | entri settled |
| F39 | 5.0 Pelunasan dan settled | Financier | status pelunasan |
| F40 | Buyer | 6.0 Riwayat buyer | sertifikat (persetujuan) |
| F41 | D3 | Key sesi (memori tab) | 6.0 Riwayat buyer | key identitas |
| F42 | D5 | Allowlist dan policy | 6.0 Riwayat buyer | allowlist, standar minimal |
| F43 | D1 | Papan registry | 6.0 Riwayat buyer | entri bertag, settled |
| F44 | 6.0 Riwayat buyer | D4 | Dokumen deal | tag riwayat |
| F45 | 6.0 Riwayat buyer | Financier | laporan riwayat |
| F46 | D4 | Dokumen deal | 7.0 Deteksi pembiayaan ganda | entri ditolak + entri ditawarkan |
| F47 | D1 | Papan registry | 7.0 Deteksi pembiayaan ganda | entri pertama |
| F48 | 7.0 Deteksi pembiayaan ganda | Financier | bukti JTSP |
| F49 | Verifier | 8.0 Verifikasi dan indeks publik | bundel, bukti, UFVK papan |
| F50 | 8.0 Verifikasi dan indeks publik | Verifier | verdict, indeks bunga |
| F51 | D1 | Papan registry | 8.0 Verifikasi dan indeks publik | memo papan |
| F52 | Anggota dana | 9.0 Solvabilitas dana | UFVK akun operasional |
| F53 | 9.0 Solvabilitas dana | Anggota dana | laporan solvabilitas |
| F54 | D6 | Akun dana | 9.0 Solvabilitas dana | transaksi akun dana |
| F55 | Financier | 9.0 Solvabilitas dana | root kewajiban (manajer) |
| F56 | 9.0 Solvabilitas dana | D6 | Akun dana | root JTLR |
