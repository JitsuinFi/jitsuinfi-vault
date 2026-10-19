---
tags: [flow, dfd]
status: DRAF
updated: 2026-10-19
---

# DFD-2.1 - Identitas dan Sesi

**Bagian dari:** [[08 - FlowDiagrams]] · Legenda: [[FD-00 - Arsitektur Target dan Legenda]] · Induk: [[DFD-1 - Proses Utama]] · Sequence: [[SEQ-00 - Autentikasi dan Onboarding]]

Proses 1.0 dirinci: daftar dan masuk dengan passkey (WebAuthn PRF), turunan key per peran, kotak surat dan kartu kontak, sesi dan stempel, pairing node financier, dan sesi konsol node. Pengiriman dokumen antarpihak tidak digambar di sini: setiap proses lain menulis dan membaca D7 sendiri. Dasar: `src/lib/passkey.ts`, wasm `buyerKeys`, usulan P-01 – P-05, P-07, P-11.

Satu jalur = satu proses. Kotak bertanda `*` adalah entitas atau penyimpanan yang sama, digambar ulang supaya garis tidak bersilang. Kotak bergaris putus-putus kuning = usulan. Penyimpanan lokal proses ini (tidak muncul di level 1): D8 Profil lokal (non-rahasia), D9 Credential terdaftar di node.

![DFD-2.1](assets/dfd-2-1.svg)

```plantuml
@startuml dfd-2-1
!include dfd-style.iuml
left to right direction
skinparam nodesep 12
skinparam ranksep 35
rectangle "D9 | Credential\nterdaftar di node *" <<storeproposal>> as D9_7
rectangle "Authenticator\npasskey *" <<entity>> as A_7
rectangle "Financier *" <<entity>> as F_7
rectangle "D2 | Node financier\n(wallet, key,\nwatch-only papan)" <<store>> as D2_6
rectangle "D9 | Credential\nterdaftar di node" <<storeproposal>> as D9_6
rectangle "Financier *" <<entity>> as F_6
rectangle "D3 | Key sesi\n(memori tab) *" <<store>> as D3_5
rectangle "Authenticator\npasskey *" <<entity>> as A_5
rectangle "Buyer *" <<entity>> as B_5
rectangle "Supplier *" <<entity>> as S_5
rectangle "Financier *" <<entity>> as F_4
rectangle "Buyer *" <<entity>> as B_4
rectangle "Supplier *" <<entity>> as S_4
rectangle "D7 | Kotak surat\nterenkripsi" <<storeproposal>> as D7_4
rectangle "D3 | Key sesi\n(memori tab) *" <<store>> as D3_4
rectangle "D3 | Key sesi\n(memori tab) *" <<store>> as D3_3
rectangle "D3 | Key sesi\n(memori tab)" <<store>> as D3_2
rectangle "Authenticator\npasskey *" <<entity>> as A_2
rectangle "D8 | Profil lokal\n(non-rahasia) *" <<storeproposal>> as D8_2
rectangle "Anggota dana *" <<entity>> as M_2
rectangle "Financier *" <<entity>> as F_2
rectangle "Buyer *" <<entity>> as B_2
rectangle "Supplier *" <<entity>> as S_2
rectangle "D8 | Profil lokal\n(non-rahasia)" <<storeproposal>> as D8_1
rectangle "Authenticator\npasskey" <<entity>> as A_1
rectangle "Anggota dana" <<entity>> as M_1
rectangle "Financier" <<entity>> as F_1
rectangle "Buyer" <<entity>> as B_1
rectangle "Supplier" <<entity>> as S_1
rectangle "**1.7**\nSesi konsol\nnode financier" <<proposal>> as P7
rectangle "**1.6**\nPasangkan node\nfinancier" <<proposal>> as P6
rectangle "**1.5**\nSesi dan stempel" <<proposal>> as P5
rectangle "**1.4**\nKotak surat dan\nkartu kontak" <<proposal>> as P4
rectangle "**1.3**\nTurunkan key\nperan" <<process>> as P3
rectangle "**1.2**\nMasuk dan\nminta PRF" <<process>> as P2
rectangle "**1.1**\nDaftar passkey" <<process>> as P1
rectangle "F1.01 daftar sebagai supplier" <<flow>> as f_F1_01
rectangle "F1.02 daftar sebagai buyer" <<flow>> as f_F1_02
rectangle "F1.03 daftar sebagai financier" <<flow>> as f_F1_03
rectangle "F1.04 daftar sebagai anggota" <<flow>> as f_F1_04
rectangle "F1.05 create() + ekstensi PRF" <<flow>> as f_F1_05
rectangle "F1.06 credential, prf.enabled" <<flow>> as f_F1_06
rectangle "F1.07 peran, credential id" <<flow>> as f_F1_07
rectangle "F1.08 masuk" <<flow>> as f_F1_08
rectangle "F1.09 masuk" <<flow>> as f_F1_09
rectangle "F1.10 masuk" <<flow>> as f_F1_10
rectangle "F1.11 masuk" <<flow>> as f_F1_11
rectangle "F1.12 credential id\n(opsional)" <<flow>> as f_F1_12
rectangle "F1.13 get() + salt\nper peran" <<flow>> as f_F1_13
rectangle "F1.14 PRF first,\nPRF second" <<flow>> as f_F1_14
rectangle "F1.15 PRF (sementara)" <<flow>> as f_F1_15
rectangle "F1.16 PRF" <<flow>> as f_F1_16
rectangle "F1.17 key peran,\nkey kotak surat" <<flow>> as f_F1_17
rectangle "F1.18 key kotak surat,\nkey publik peran" <<flow>> as f_F1_18
rectangle "F1.19 mailbox_pk +\nbukti kepemilikan" <<flow>> as f_F1_19
rectangle "F1.20 mailbox_id" <<flow>> as f_F1_20
rectangle "F1.21 kartu kontak" <<flow>> as f_F1_21
rectangle "F1.22 kartu kontak\n(tanpa identity_pk)" <<flow>> as f_F1_22
rectangle "F1.23 kartu kontak" <<flow>> as f_F1_23
rectangle "F1.24 tindakan stempel" <<flow>> as f_F1_24
rectangle "F1.25 tindakan stempel" <<flow>> as f_F1_25
rectangle "F1.26 get() user\nverification" <<flow>> as f_F1_26
rectangle "F1.27 assertion\nterverifikasi" <<flow>> as f_F1_27
rectangle "F1.28 key peran" <<flow>> as f_F1_28
rectangle "F1.29 key stempel sekali pakai,\nsesi terkunci" <<flow>> as f_F1_29
rectangle "F1.30 pairing, UFVK papan\n+ birthday" <<flow>> as f_F1_30
rectangle "F1.31 public key\ncredential" <<flow>> as f_F1_31
rectangle "F1.32 wallet baru (seed di node),\nkey financier, watch-only papan" <<flow>> as f_F1_32
rectangle "F1.33 buka konsol" <<flow>> as f_F1_33
rectangle "F1.34 challenge" <<flow>> as f_F1_34
rectangle "F1.35 assertion" <<flow>> as f_F1_35
rectangle "F1.36 public key\ncredential" <<flow>> as f_F1_36
rectangle "F1.37 sesi konsol\n(cookie)" <<flow>> as f_F1_37
S_1 -- f_F1_01
f_F1_01 --> P1
B_1 -- f_F1_02
f_F1_02 --> P1
F_1 -- f_F1_03
f_F1_03 --> P1
M_1 -- f_F1_04
f_F1_04 --> P1
A_1 <-- f_F1_05
f_F1_05 -- P1
A_1 -- f_F1_06
f_F1_06 --> P1
P1 -- f_F1_07
f_F1_07 --> D8_1
S_2 -- f_F1_08
f_F1_08 --> P2
B_2 -- f_F1_09
f_F1_09 --> P2
F_2 -- f_F1_10
f_F1_10 --> P2
M_2 -- f_F1_11
f_F1_11 --> P2
P2 <-- f_F1_12
f_F1_12 -- D8_2
A_2 <-- f_F1_13
f_F1_13 -- P2
A_2 -- f_F1_14
f_F1_14 --> P2
P2 -- f_F1_15
f_F1_15 --> D3_2
P3 <-- f_F1_16
f_F1_16 -- D3_3
P3 -- f_F1_17
f_F1_17 --> D3_3
P4 <-- f_F1_18
f_F1_18 -- D3_4
P4 -- f_F1_19
f_F1_19 --> D7_4
P4 <-- f_F1_20
f_F1_20 -- D7_4
S_4 <-- f_F1_21
f_F1_21 -- P4
B_4 <-- f_F1_22
f_F1_22 -- P4
F_4 <-- f_F1_23
f_F1_23 -- P4
S_5 -- f_F1_24
f_F1_24 --> P5
B_5 -- f_F1_25
f_F1_25 --> P5
A_5 <-- f_F1_26
f_F1_26 -- P5
A_5 -- f_F1_27
f_F1_27 --> P5
P5 <-- f_F1_28
f_F1_28 -- D3_5
P5 -- f_F1_29
f_F1_29 --> D3_5
F_6 -- f_F1_30
f_F1_30 --> P6
P6 -- f_F1_31
f_F1_31 --> D9_6
P6 -- f_F1_32
f_F1_32 --> D2_6
F_7 -- f_F1_33
f_F1_33 --> P7
A_7 <-- f_F1_34
f_F1_34 -- P7
A_7 -- f_F1_35
f_F1_35 --> P7
P7 <-- f_F1_36
f_F1_36 -- D9_7
F_7 <-- f_F1_37
f_F1_37 -- P7
rectangle " " <<spacer>> as sp_P3_a
rectangle " " <<spacer>> as sp_P3_b
sp_P3_a -[hidden]- sp_P3_b
sp_P3_b -[hidden]- P3
@enduml
```

## Proses

| Proses | Isi | Status | Kode / item |
|---|---|---|---|
| 1.1 Daftar passkey | `create()` dengan `residentKey` dan `userVerification` required, ekstensi PRF; tolak authenticator tanpa PRF | ADA (buyer); USULAN peran lain | `createPasskey`, P-01 |
| 1.2 Masuk dan minta PRF | `get()` discoverable; `prf.eval.first` = SHA-256("jitsuin/<peran>/master/v1"), `second` = salt inbox | ADA (buyer, satu salt); salt lain USULAN | `masterFromPasskey`, P-02 |
| 1.3 Turunkan key peran | Buyer: key identitas + key per invoice (keyed BLAKE2b). Supplier: master untuk key per invoice (P-03). Financier: tanpa key tanda tangan di browser (P-05) | ADA (buyer) | wasm `buyerKeys` |
| 1.4 Kotak surat dan kartu kontak | X25519 dari PRF second; relay menyimpan `mailbox_pk`. Kartu buyer tidak memuat `identity_pk` (Threat Model) | USULAN | P-04 |
| 1.5 Sesi dan stempel | Key di memori tab; satu sentuhan passkey per stempel; kunci setelah 15 menit idle | PARSIAL (memori ADA; sisanya USULAN) | U-HNK-10.3, P-07 |
| 1.6 Pasangkan node financier | Node menyimpan public key credential financier; wallet dan key financier dibuat di node; UFVK papan diimpor watch-only | USULAN | P-05 |
| 1.7 Sesi konsol node financier | Challenge dari node, assertion passkey, cookie httpOnly; konsol harus same-origin (P-11) | USULAN | P-05, P-11, HNK-05.T3 |

## Aliran data

| Aliran | Dari | Ke | Data |
|---|---|---|---|
| F1.01 | Supplier | 1.1 Daftar passkey | daftar sebagai supplier |
| F1.02 | Buyer | 1.1 Daftar passkey | daftar sebagai buyer |
| F1.03 | Financier | 1.1 Daftar passkey | daftar sebagai financier |
| F1.04 | Anggota dana | 1.1 Daftar passkey | daftar sebagai anggota |
| F1.05 | 1.1 Daftar passkey | Authenticator passkey | create() + ekstensi PRF |
| F1.06 | Authenticator passkey | 1.1 Daftar passkey | credential, prf.enabled |
| F1.07 | 1.1 Daftar passkey | D8 Profil lokal (non-rahasia) | peran, credential id |
| F1.08 | Supplier | 1.2 Masuk dan minta PRF | masuk |
| F1.09 | Buyer | 1.2 Masuk dan minta PRF | masuk |
| F1.10 | Financier | 1.2 Masuk dan minta PRF | masuk |
| F1.11 | Anggota dana | 1.2 Masuk dan minta PRF | masuk |
| F1.12 | D8 Profil lokal (non-rahasia) | 1.2 Masuk dan minta PRF | credential id (opsional) |
| F1.13 | 1.2 Masuk dan minta PRF | Authenticator passkey | get() + salt per peran |
| F1.14 | Authenticator passkey | 1.2 Masuk dan minta PRF | PRF first, PRF second |
| F1.15 | 1.2 Masuk dan minta PRF | D3 Key sesi (memori tab) | PRF (sementara) |
| F1.16 | D3 Key sesi (memori tab) | 1.3 Turunkan key peran | PRF |
| F1.17 | 1.3 Turunkan key peran | D3 Key sesi (memori tab) | key peran, key kotak surat |
| F1.18 | D3 Key sesi (memori tab) | 1.4 Kotak surat dan kartu kontak | key kotak surat, key publik peran |
| F1.19 | 1.4 Kotak surat dan kartu kontak | D7 Kotak surat terenkripsi | mailbox_pk + bukti kepemilikan |
| F1.20 | D7 Kotak surat terenkripsi | 1.4 Kotak surat dan kartu kontak | mailbox_id |
| F1.21 | 1.4 Kotak surat dan kartu kontak | Supplier | kartu kontak |
| F1.22 | 1.4 Kotak surat dan kartu kontak | Buyer | kartu kontak (tanpa identity_pk) |
| F1.23 | 1.4 Kotak surat dan kartu kontak | Financier | kartu kontak |
| F1.24 | Supplier | 1.5 Sesi dan stempel | tindakan stempel |
| F1.25 | Buyer | 1.5 Sesi dan stempel | tindakan stempel |
| F1.26 | 1.5 Sesi dan stempel | Authenticator passkey | get() user verification |
| F1.27 | Authenticator passkey | 1.5 Sesi dan stempel | assertion terverifikasi |
| F1.28 | D3 Key sesi (memori tab) | 1.5 Sesi dan stempel | key peran |
| F1.29 | 1.5 Sesi dan stempel | D3 Key sesi (memori tab) | key stempel sekali pakai, sesi terkunci |
| F1.30 | Financier | 1.6 Pasangkan node financier | pairing, UFVK papan + birthday |
| F1.31 | 1.6 Pasangkan node financier | D9 Credential terdaftar di node | public key credential |
| F1.32 | 1.6 Pasangkan node financier | D2 Node financier (wallet, key, watch-only papan) | wallet baru (seed di node), key financier, watch-only papan |
| F1.33 | Financier | 1.7 Sesi konsol node financier | buka konsol |
| F1.34 | 1.7 Sesi konsol node financier | Authenticator passkey | challenge |
| F1.35 | Authenticator passkey | 1.7 Sesi konsol node financier | assertion |
| F1.36 | D9 Credential terdaftar di node | 1.7 Sesi konsol node financier | public key credential |
| F1.37 | 1.7 Sesi konsol node financier | Financier | sesi konsol (cookie) |
