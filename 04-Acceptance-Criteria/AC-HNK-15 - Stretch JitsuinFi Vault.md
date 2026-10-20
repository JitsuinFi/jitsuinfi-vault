---
tags: [ac, "HNK-15"]
type: ac
id: HNK-15
phase: F7
lead: Hans
owners: [Hans]
status: PARSIAL
updated: 2026-10-17
---

# AC-HNK-15 - Stretch JitsuinFi Vault

> **Peta link:** [[AC Hub]] · [[Backlog]] · **AC** · [[TEST-HNK-15 - Stretch JitsuinFi Vault|Test]] · [[ES-HNK-15 - Stretch JitsuinFi Vault|Exec Summary]]

**Item:** HNK-15 · **Fase:** F7 · **Dependency:** HNK-07, SPK-05

**Lead:** Hans #hans · **Tim:** Hans #hans 

## Deskripsi
Dana bersama: setoran anggota → Merkle sum tree kewajiban → uji solvabilitas lewat FVK akun operasional. Hanya dikerjakan kalau F3 lulus paling lambat 23 Okt dan user setuju.

## Acceptance criteria
Status per kriteria: `TODO` / `PASS` / `FAIL` / `BLOCKED`, wajib dengan tanggal dan bukti (commit, txid, log, id tes).

| ID | Kriteria | Status | Tanggal | Bukti |
|---|---|---|---|---|
| AC-HNK-15.1 | Keputusan go/no-go user tercatat di [[Decision Log]]. | PASS | 2026-10-17 | **D-24** di [[Decision Log]]: user memutuskan go ("Gas HNK-15") |
| AC-HNK-15.2 | Root Merkle sum tree dicatat lewat memo per periode; anggota memverifikasi inklusi simpanannya. | TODO | 2026-10-17 | Bagian Hans selesai: root kewajiban periode 1 dicatat lewat memo `JTLR` bertanda tangan manajer, tx `d8c207554d7975a28213a7cac45405ecc7bc4ed536929683481ae630d642a03c`; root palsu dari pihak luar (`4692b8f092dcc0379d881bba1318a237ffd97aee9c8abf12318a70435498a815`) diabaikan anggota. **Inklusi simpanan anggota = Merkle sum tree HNK-15.T1 (Dex), belum**; root uji memakai placeholder |
| AC-HNK-15.3 | Uji solvabilitas aset ≥ kewajiban dihitung dari data chain. | PASS | 2026-10-17 | `e54ea36`. Testnet (DEV-03): anggota (wallet watch-only dari UFVK akun operasional) menghitung sendiri kas 99.547.000 + piutang berjalan 20.000 + lewat jatuh tempo 0 = aset 99.567.000 ≥ kewajiban 49.786.000 zat → solvent. Piutang dari advance `7b5687991a8df84cdb334d910f5d08850b98d5d02c7df09cd1bff4f2c167dbd9` (nominal 20.000, advance 15.000) terbaca lewat catatan `JTN1` |

## Deviasi
_Kosong._ Kalau implementasi menyimpang dari keputusan, tulis di sini **dan** di [[Backlog]] bagian Log Deviasi. Tidak ada perubahan diam-diam.
