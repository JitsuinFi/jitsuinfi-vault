---
tags: [flow, dfd]
status: DRAF
updated: 2026-10-19
---

# DFD-2.8 - Verifikasi dan Indeks Publik

**Bagian dari:** [[08 - FlowDiagrams]] · Legenda: [[FD-00 - Arsitektur Target dan Legenda]] · Induk: [[DFD-1 - Proses Utama]] · Sequence: [[SEQ-04 - Verifier dan Orang Luar]]

Proses 8.0 dirinci: juri dan auditor memindai papan sendiri dengan UFVK papan, memverifikasi bukti dan bundel, menghitung indeks bunga; financier menyusun bundel; relay menyajikan snapshot untuk browser; orang luar hanya melihat hash. Dasar: `jitsuin-cli` (`verify`, `index`, `board`), `jitsuin-board` (`scan`, `bundle_on_board`, `verify_proof_on_board`, `rate_index`), wasm `bundleBuild`, `verifyBundle`, `verifyProof`, `bundleOnBoard`, `boardMemoDescribe`.

Satu jalur = satu proses. Kotak bertanda `*` adalah entitas atau penyimpanan yang sama, digambar ulang supaya garis tidak bersilang. Kotak bergaris putus-putus kuning = usulan. Penyimpanan lokal proses ini (tidak muncul di level 1): D14 Wallet watch-only papan (juri), D18 Hasil pindai (juri).

![DFD-2.8](assets/dfd-2-8.svg)

```plantuml
@startuml dfd-2-8
!include dfd-style.iuml
left to right direction
skinparam nodesep 12
skinparam ranksep 35
rectangle "Verifier\n(juri, auditor) *" <<entity>> as V_8
rectangle "D12 | Snapshot papan\n(relay) *" <<storeproposal>> as D12_7
rectangle "Jaringan Zcash\n(lightwalletd) *" <<entity>> as Z_7
rectangle "D1 | Papan registry *" <<store>> as D1_7
rectangle "D18 | Hasil pindai\n(juri) *" <<store>> as D18_6
rectangle "Verifier\n(juri, auditor) *" <<entity>> as V_6
rectangle "D12 | Snapshot papan\n(relay)" <<storeproposal>> as D12_5
rectangle "D18 | Hasil pindai\n(juri) *" <<store>> as D18_5
rectangle "Verifier\n(juri, auditor) *" <<entity>> as V_5
rectangle "Verifier\n(juri, auditor) *" <<entity>> as V_4
rectangle "D4 | Dokumen deal\n(lokal)" <<store>> as D4_4
rectangle "Financier" <<entity>> as F_4
rectangle "D18 | Hasil pindai\n(juri) *" <<store>> as D18_3
rectangle "Verifier\n(juri, auditor) *" <<entity>> as V_3
rectangle "D18 | Hasil pindai\n(juri)" <<store>> as D18_2
rectangle "Verifier\n(juri, auditor) *" <<entity>> as V_2
rectangle "Jaringan Zcash\n(lightwalletd)" <<entity>> as Z_2
rectangle "D1 | Papan registry" <<store>> as D1_2
rectangle "D14 | Wallet watch-only\npapan (juri) *" <<store>> as D14_2
rectangle "D14 | Wallet watch-only\npapan (juri)" <<store>> as D14_1
rectangle "Verifier\n(juri, auditor)" <<entity>> as V_1
rectangle "**8.8**\nJelaskan memo\n(orang luar)" <<process>> as P8
rectangle "**8.7**\nSajikan snapshot\npapan (relay)" <<proposal>> as P7
rectangle "**8.6**\nHitung indeks bunga" <<process>> as P6
rectangle "**8.5**\nVerifikasi bundel" <<process>> as P5
rectangle "**8.4**\nSusun bundel\n(financier)" <<process>> as P4
rectangle "**8.3**\nVerifikasi bukti" <<process>> as P3
rectangle "**8.2**\nPindai papan" <<process>> as P2
rectangle "**8.1**\nSiapkan watch-only\npapan" <<process>> as P1
rectangle "F8.01 UFVK papan,\nbirthday" <<flow>> as f_F8_01
rectangle "F8.02 wallet watch-only" <<flow>> as f_F8_02
rectangle "F8.03 wallet" <<flow>> as f_F8_03
rectangle "F8.04 memo papan" <<flow>> as f_F8_04
rectangle "F8.05 blok, tx penuh,\nurutan txid" <<flow>> as f_F8_05
rectangle "F8.06 snapshot\n(--board)" <<flow>> as f_F8_06
rectangle "F8.07 snapshot\n(--save-board)" <<flow>> as f_F8_07
rectangle "F8.08 records, settled,\nrejected" <<flow>> as f_F8_08
rectangle "F8.09 bukti JTSP" <<flow>> as f_F8_09
rectangle "F8.10 records" <<flow>> as f_F8_10
rectangle "F8.11 PASS / FAIL\nper cek" <<flow>> as f_F8_11
rectangle "F8.12 buat bundel" <<flow>> as f_F8_12
rectangle "F8.13 invoice, sig, surat,\nseal, dok. pelunasan" <<flow>> as f_F8_13
rectangle "F8.14 bundel JTSB" <<flow>> as f_F8_14
rectangle "F8.15 bundel JTSB" <<flow>> as f_F8_15
rectangle "F8.16 records, settled" <<flow>> as f_F8_16
rectangle "F8.17 snapshot (web)" <<flow>> as f_F8_17
rectangle "F8.18 register, settled,\nexit code" <<flow>> as f_F8_18
rectangle "F8.19 k (minimal 5)" <<flow>> as f_F8_19
rectangle "F8.20 records" <<flow>> as f_F8_20
rectangle "F8.21 indeks per\nkelas tenor" <<flow>> as f_F8_21
rectangle "F8.22 memo papan\n(UFVK papan)" <<flow>> as f_F8_22
rectangle "F8.23 blok, urutan tx" <<flow>> as f_F8_23
rectangle "F8.24 snapshot JSON" <<flow>> as f_F8_24
rectangle "F8.25 satu memo papan" <<flow>> as f_F8_25
rectangle "F8.26 jenis, N, commitment,\nkelas, tag (hash)" <<flow>> as f_F8_26
V_1 -- f_F8_01
f_F8_01 --> P1
P1 -- f_F8_02
f_F8_02 --> D14_1
P2 <-- f_F8_03
f_F8_03 -- D14_2
P2 <-- f_F8_04
f_F8_04 -- D1_2
Z_2 -- f_F8_05
f_F8_05 --> P2
V_2 -- f_F8_06
f_F8_06 --> P2
V_2 <-- f_F8_07
f_F8_07 -- P2
P2 -- f_F8_08
f_F8_08 --> D18_2
V_3 -- f_F8_09
f_F8_09 --> P3
P3 <-- f_F8_10
f_F8_10 -- D18_3
V_3 <-- f_F8_11
f_F8_11 -- P3
F_4 -- f_F8_12
f_F8_12 --> P4
P4 <-- f_F8_13
f_F8_13 -- D4_4
V_4 <-- f_F8_14
f_F8_14 -- P4
V_5 -- f_F8_15
f_F8_15 --> P5
P5 <-- f_F8_16
f_F8_16 -- D18_5
P5 <-- f_F8_17
f_F8_17 -- D12_5
V_5 <-- f_F8_18
f_F8_18 -- P5
V_6 -- f_F8_19
f_F8_19 --> P6
P6 <-- f_F8_20
f_F8_20 -- D18_6
V_6 <-- f_F8_21
f_F8_21 -- P6
P7 <-- f_F8_22
f_F8_22 -- D1_7
Z_7 -- f_F8_23
f_F8_23 --> P7
P7 -- f_F8_24
f_F8_24 --> D12_7
V_8 -- f_F8_25
f_F8_25 --> P8
V_8 <-- f_F8_26
f_F8_26 -- P8
@enduml
```

## Proses

| Proses | Isi | Status | Kode / item |
|---|---|---|---|
| 8.1 Siapkan watch-only papan | `init-fvk` dengan UFVK papan dan tinggi awal; jaringan dari awalan UFVK. UFVK papan belum dipublikasikan (D-11 masih usulan) | ADA | `jitsuin-cli::board` |
| 8.2 Pindai papan | Sama dengan 3.4; snapshot bisa ditulis (`--save-board`) dan dibaca offline (`--board`) | ADA | `scan`, `to_snapshot`, `from_snapshot` |
| 8.3 Verifikasi bukti | `DoubleSignProof::verify` + posisi di papan | ADA | `verify::check_proof` |
| 8.4 Susun bundel | Financier menyusun JTSB dari dokumen deal | ADA (kartu di layar Financier) | wasm `bundleBuild` |
| 8.5 Verifikasi bundel | `Bundle::verify` + `bundle_on_board`; di web papan diunggah sebagai file | ADA | `verify::check_bundle`, wasm `bundleOnBoard` |
| 8.6 Hitung indeks bunga | Tiap N sekali; kelas diskon per kelas tenor dengan ≥ k invoice. Selama kelas selalu 0/0 (3.2), indeks kosong | ADA (CLI); halaman web HNK-08.T3 belum | `rate_index`, `jitsuin index` |
| 8.7 Sajikan snapshot papan | Relay memindai sendiri dengan UFVK papan dan menyajikan JSON same-origin | USULAN P-06, P-11 | — |
| 8.8 Jelaskan memo | Halaman orang luar menguraikan memo tanpa bisa mengecek tanda tangan | ADA | wasm `boardMemoDescribe` |

## Aliran data

| Aliran | Dari | Ke | Data |
|---|---|---|---|
| F8.01 | Verifier (juri, auditor) | 8.1 Siapkan watch-only papan | UFVK papan, birthday |
| F8.02 | 8.1 Siapkan watch-only papan | D14 Wallet watch-only papan (juri) | wallet watch-only |
| F8.03 | D14 Wallet watch-only papan (juri) | 8.2 Pindai papan | wallet |
| F8.04 | D1 Papan registry | 8.2 Pindai papan | memo papan |
| F8.05 | Jaringan Zcash (lightwalletd) | 8.2 Pindai papan | blok, tx penuh, urutan txid |
| F8.06 | Verifier (juri, auditor) | 8.2 Pindai papan | snapshot (--board) |
| F8.07 | 8.2 Pindai papan | Verifier (juri, auditor) | snapshot (--save-board) |
| F8.08 | 8.2 Pindai papan | D18 Hasil pindai (juri) | records, settled, rejected |
| F8.09 | Verifier (juri, auditor) | 8.3 Verifikasi bukti | bukti JTSP |
| F8.10 | D18 Hasil pindai (juri) | 8.3 Verifikasi bukti | records |
| F8.11 | 8.3 Verifikasi bukti | Verifier (juri, auditor) | PASS / FAIL per cek |
| F8.12 | Financier | 8.4 Susun bundel (financier) | buat bundel |
| F8.13 | D4 Dokumen deal (lokal) | 8.4 Susun bundel (financier) | invoice, sig, surat, seal, dok. pelunasan |
| F8.14 | 8.4 Susun bundel (financier) | Verifier (juri, auditor) | bundel JTSB |
| F8.15 | Verifier (juri, auditor) | 8.5 Verifikasi bundel | bundel JTSB |
| F8.16 | D18 Hasil pindai (juri) | 8.5 Verifikasi bundel | records, settled |
| F8.17 | D12 Snapshot papan (relay) | 8.5 Verifikasi bundel | snapshot (web) |
| F8.18 | 8.5 Verifikasi bundel | Verifier (juri, auditor) | register, settled, exit code |
| F8.19 | Verifier (juri, auditor) | 8.6 Hitung indeks bunga | k (minimal 5) |
| F8.20 | D18 Hasil pindai (juri) | 8.6 Hitung indeks bunga | records |
| F8.21 | 8.6 Hitung indeks bunga | Verifier (juri, auditor) | indeks per kelas tenor |
| F8.22 | D1 Papan registry | 8.7 Sajikan snapshot papan (relay) | memo papan (UFVK papan) |
| F8.23 | Jaringan Zcash (lightwalletd) | 8.7 Sajikan snapshot papan (relay) | blok, urutan tx |
| F8.24 | 8.7 Sajikan snapshot papan (relay) | D12 Snapshot papan (relay) | snapshot JSON |
| F8.25 | Verifier (juri, auditor) | 8.8 Jelaskan memo (orang luar) | satu memo papan |
| F8.26 | 8.8 Jelaskan memo (orang luar) | Verifier (juri, auditor) | jenis, N, commitment, kelas, tag (hash) |
