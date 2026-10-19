---
tags: [flow, dfd]
status: DRAF
updated: 2026-10-19
---

# DFD-2.1 - Identitas dan Sesi

**Bagian dari:** [[08 - FlowDiagrams]] · Legenda: [[FD-00 - Arsitektur Target dan Legenda]] · Induk: [[DFD-1 - Proses Utama]] · Sequence: [[SEQ-00 - Autentikasi dan Onboarding]]

Proses 1.0 dirinci: daftar dan masuk dengan passkey (WebAuthn PRF), turunan key per peran, kotak surat terenkripsi, sesi dan stempel, serta sesi konsol node financier. Dasar: `src/lib/passkey.ts`, wasm `buyerKeys`, usulan P-01 – P-05, P-07.

Kotak bertanda `*` adalah entitas atau penyimpanan yang sama yang digambar ulang di jalur proses lain, supaya garis tidak bersilang. Kotak bergaris putus-putus kuning = usulan.

![DFD-2.1](assets/dfd-2-1.svg)

```plantuml
@startuml dfd-2-1
!include dfd-style.iuml
left to right direction
skinparam nodesep 12
skinparam ranksep 35
rectangle "D9 | Credential\nterdaftar di node" <<storeproposal>> as D9_7
rectangle "Authenticator\npasskey *" <<entity>> as A_7
rectangle "Pengguna peran\n(supplier, buyer,\nfinancier) *" <<entity>> as U_7
rectangle "D3 | Key sesi\n(memori tab) *" <<store>> as D3_6
rectangle "Authenticator\npasskey *" <<entity>> as A_6
rectangle "Pengguna peran\n(supplier, buyer,\nfinancier) *" <<entity>> as U_6
rectangle "D4 | Dokumen deal" <<store>> as D4_5
rectangle "D7 | Kotak surat\nterenkripsi *" <<storeproposal>> as D7_5
rectangle "D3 | Key sesi\n(memori tab) *" <<store>> as D3_5
rectangle "Pengguna peran\n(supplier, buyer,\nfinancier) *" <<entity>> as U_5
rectangle "Pengguna peran\n(supplier, buyer,\nfinancier) *" <<entity>> as U_4
rectangle "D7 | Kotak surat\nterenkripsi" <<storeproposal>> as D7_4
rectangle "D3 | Key sesi\n(memori tab) *" <<store>> as D3_4
rectangle "D3 | Key sesi\n(memori tab) *" <<store>> as D3_3
rectangle "D3 | Key sesi\n(memori tab)" <<store>> as D3_2
rectangle "Authenticator\npasskey *" <<entity>> as A_2
rectangle "D8 | Profil lokal\n(non-rahasia) *" <<storeproposal>> as D8_2
rectangle "Pengguna peran\n(supplier, buyer,\nfinancier) *" <<entity>> as U_2
rectangle "D8 | Profil lokal\n(non-rahasia)" <<storeproposal>> as D8_1
rectangle "Authenticator\npasskey" <<entity>> as A_1
rectangle "Pengguna peran\n(supplier, buyer,\nfinancier)" <<entity>> as U_1
rectangle "**1.7**\nSesi konsol\nnode financier" <<proposal>> as P7
rectangle "**1.6**\nSesi dan stempel" <<proposal>> as P6
rectangle "**1.5**\nKirim dan terima\ndokumen terenkripsi" <<proposal>> as P5
rectangle "**1.4**\nDaftar kotak surat" <<proposal>> as P4
rectangle "**1.3**\nTurunkan key\nperan" <<process>> as P3
rectangle "**1.2**\nMasuk dan\nminta PRF" <<process>> as P2
rectangle "**1.1**\nDaftar passkey" <<process>> as P1
rectangle "F1.01 pilih peran,\ndaftar" <<flow>> as f_F1_01
rectangle "F1.02 create()\n+ ekstensi PRF" <<flow>> as f_F1_02
rectangle "F1.03 credential,\nprf.enabled" <<flow>> as f_F1_03
rectangle "F1.04 peran,\ncredential id" <<flow>> as f_F1_04
rectangle "F1.05 masuk,\nganti peran" <<flow>> as f_F1_05
rectangle "F1.06 credential id\n(opsional)" <<flow>> as f_F1_06
rectangle "F1.07 get() + salt\nper peran" <<flow>> as f_F1_07
rectangle "F1.08 PRF first,\nPRF second" <<flow>> as f_F1_08
rectangle "F1.09 PRF (sementara)" <<flow>> as f_F1_09
rectangle "F1.10 PRF" <<flow>> as f_F1_10
rectangle "F1.11 key peran,\nkey kotak surat" <<flow>> as f_F1_11
rectangle "F1.12 key kotak surat" <<flow>> as f_F1_12
rectangle "F1.13 mailbox_pk +\nbukti kepemilikan" <<flow>> as f_F1_13
rectangle "F1.14 mailbox_id" <<flow>> as f_F1_14
rectangle "F1.15 kartu kontak (QR)" <<flow>> as f_F1_15
rectangle "F1.16 dokumen untuk\nrekan deal" <<flow>> as f_F1_16
rectangle "F1.17 key kotak surat" <<flow>> as f_F1_17
rectangle "F1.18 ciphertext" <<flow>> as f_F1_18
rectangle "F1.19 ciphertext masuk" <<flow>> as f_F1_19
rectangle "F1.20 dokumen deal\n(terdekripsi)" <<flow>> as f_F1_20
rectangle "F1.21 tindakan stempel" <<flow>> as f_F1_21
rectangle "F1.22 get() user\nverification" <<flow>> as f_F1_22
rectangle "F1.23 izin" <<flow>> as f_F1_23
rectangle "F1.24 key" <<flow>> as f_F1_24
rectangle "F1.25 hapus key\n(idle 15 menit)" <<flow>> as f_F1_25
rectangle "F1.26 buka konsol" <<flow>> as f_F1_26
rectangle "F1.27 challenge" <<flow>> as f_F1_27
rectangle "F1.28 assertion" <<flow>> as f_F1_28
rectangle "F1.29 public key\ncredential" <<flow>> as f_F1_29
rectangle "F1.30 cookie sesi" <<flow>> as f_F1_30
U_1 -- f_F1_01
f_F1_01 --> P1
A_1 <-- f_F1_02
f_F1_02 -- P1
A_1 -- f_F1_03
f_F1_03 --> P1
P1 -- f_F1_04
f_F1_04 --> D8_1
U_2 -- f_F1_05
f_F1_05 --> P2
P2 <-- f_F1_06
f_F1_06 -- D8_2
A_2 <-- f_F1_07
f_F1_07 -- P2
A_2 -- f_F1_08
f_F1_08 --> P2
P2 -- f_F1_09
f_F1_09 --> D3_2
P3 <-- f_F1_10
f_F1_10 -- D3_3
P3 -- f_F1_11
f_F1_11 --> D3_3
P4 <-- f_F1_12
f_F1_12 -- D3_4
P4 -- f_F1_13
f_F1_13 --> D7_4
P4 <-- f_F1_14
f_F1_14 -- D7_4
U_4 <-- f_F1_15
f_F1_15 -- P4
U_5 -- f_F1_16
f_F1_16 --> P5
P5 <-- f_F1_17
f_F1_17 -- D3_5
P5 -- f_F1_18
f_F1_18 --> D7_5
P5 <-- f_F1_19
f_F1_19 -- D7_5
P5 -- f_F1_20
f_F1_20 --> D4_5
U_6 -- f_F1_21
f_F1_21 --> P6
A_6 <-- f_F1_22
f_F1_22 -- P6
A_6 -- f_F1_23
f_F1_23 --> P6
P6 <-- f_F1_24
f_F1_24 -- D3_6
P6 -- f_F1_25
f_F1_25 --> D3_6
U_7 -- f_F1_26
f_F1_26 --> P7
A_7 <-- f_F1_27
f_F1_27 -- P7
A_7 -- f_F1_28
f_F1_28 --> P7
P7 <-- f_F1_29
f_F1_29 -- D9_7
U_7 <-- f_F1_30
f_F1_30 -- P7
rectangle " " <<spacer>> as sp_P3_a
rectangle " " <<spacer>> as sp_P3_b
sp_P3_a -[hidden]- sp_P3_b
sp_P3_b -[hidden]- P3
@enduml
```

## Proses

| Proses | Isi | Status | Kode / item |
|---|---|---|---|
| 1.1 Daftar passkey | `navigator.credentials.create` dengan `residentKey` dan `userVerification` required, ekstensi PRF; tolak authenticator tanpa PRF | ADA (buyer); USULAN untuk peran lain | `createPasskey`, P-01 |
| 1.2 Masuk dan minta PRF | `get()` discoverable, `prf.eval.first` = SHA-256("jitsuin/<peran>/master/v1"), `second` = salt inbox | ADA (buyer, satu salt); USULAN (salt peran, inbox) | `masterFromPasskey`, P-02 |
| 1.3 Turunkan key peran | Buyer: key identitas + key per invoice (keyed BLAKE2b). Supplier: master untuk key per invoice (P-03). Financier: tanpa key di browser (P-05) | ADA (buyer) | wasm `buyerKeys` |
| 1.4 Daftar kotak surat | X25519 dari PRF second; relay menyimpan `mailbox_pk` saja | USULAN | P-04 |
| 1.5 Kirim dan terima dokumen | Enkripsi end-to-end di browser; relay hanya menyimpan ciphertext dengan masa simpan | USULAN | P-04 |
| 1.6 Sesi dan stempel | Key hanya di memori tab; satu sentuhan passkey per stempel; kunci setelah 15 menit idle | PARSIAL (memori: ADA; sisanya USULAN) | U-HNK-10.3, P-07 |
| 1.7 Sesi konsol node financier | Challenge dari node, assertion passkey, cookie httpOnly | USULAN | P-05, HNK-05.T3 |

## Aliran data

| Aliran | Dari | Ke | Data |
|---|---|---|---|
| F1.01 | Pengguna peran (supplier, buyer, financier) | 1.1 Daftar passkey | pilih peran, daftar |
| F1.02 | 1.1 Daftar passkey | Authenticator passkey | create() + ekstensi PRF |
| F1.03 | Authenticator passkey | 1.1 Daftar passkey | credential, prf.enabled |
| F1.04 | 1.1 Daftar passkey | D8 | Profil lokal (non-rahasia) | peran, credential id |
| F1.05 | Pengguna peran (supplier, buyer, financier) | 1.2 Masuk dan minta PRF | masuk, ganti peran |
| F1.06 | D8 | Profil lokal (non-rahasia) | 1.2 Masuk dan minta PRF | credential id (opsional) |
| F1.07 | 1.2 Masuk dan minta PRF | Authenticator passkey | get() + salt per peran |
| F1.08 | Authenticator passkey | 1.2 Masuk dan minta PRF | PRF first, PRF second |
| F1.09 | 1.2 Masuk dan minta PRF | D3 | Key sesi (memori tab) | PRF (sementara) |
| F1.10 | D3 | Key sesi (memori tab) | 1.3 Turunkan key peran | PRF |
| F1.11 | 1.3 Turunkan key peran | D3 | Key sesi (memori tab) | key peran, key kotak surat |
| F1.12 | D3 | Key sesi (memori tab) | 1.4 Daftar kotak surat | key kotak surat |
| F1.13 | 1.4 Daftar kotak surat | D7 | Kotak surat terenkripsi | mailbox_pk + bukti kepemilikan |
| F1.14 | D7 | Kotak surat terenkripsi | 1.4 Daftar kotak surat | mailbox_id |
| F1.15 | 1.4 Daftar kotak surat | Pengguna peran (supplier, buyer, financier) | kartu kontak (QR) |
| F1.16 | Pengguna peran (supplier, buyer, financier) | 1.5 Kirim dan terima dokumen terenkripsi | dokumen untuk rekan deal |
| F1.17 | D3 | Key sesi (memori tab) | 1.5 Kirim dan terima dokumen terenkripsi | key kotak surat |
| F1.18 | 1.5 Kirim dan terima dokumen terenkripsi | D7 | Kotak surat terenkripsi | ciphertext |
| F1.19 | D7 | Kotak surat terenkripsi | 1.5 Kirim dan terima dokumen terenkripsi | ciphertext masuk |
| F1.20 | 1.5 Kirim dan terima dokumen terenkripsi | D4 | Dokumen deal | dokumen deal (terdekripsi) |
| F1.21 | Pengguna peran (supplier, buyer, financier) | 1.6 Sesi dan stempel | tindakan stempel |
| F1.22 | 1.6 Sesi dan stempel | Authenticator passkey | get() user verification |
| F1.23 | Authenticator passkey | 1.6 Sesi dan stempel | izin |
| F1.24 | D3 | Key sesi (memori tab) | 1.6 Sesi dan stempel | key |
| F1.25 | 1.6 Sesi dan stempel | D3 | Key sesi (memori tab) | hapus key (idle 15 menit) |
| F1.26 | Pengguna peran (supplier, buyer, financier) | 1.7 Sesi konsol node financier | buka konsol |
| F1.27 | 1.7 Sesi konsol node financier | Authenticator passkey | challenge |
| F1.28 | Authenticator passkey | 1.7 Sesi konsol node financier | assertion |
| F1.29 | D9 | Credential terdaftar di node | 1.7 Sesi konsol node financier | public key credential |
| F1.30 | 1.7 Sesi konsol node financier | Pengguna peran (supplier, buyer, financier) | cookie sesi |
