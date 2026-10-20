---
tags: [ac, "HNK-28"]
type: ac
id: HNK-28
phase: F4
lead: Dex
owners: [Hans, Dex]
status: PARSIAL
updated: 2026-10-20
---

# AC-HNK-28 - Verifikasi publik lengkap

> **Peta link:** [[AC Hub]] · [[Backlog]] · **AC** · [[TEST-HNK-28 - Verifikasi publik lengkap|Test]] · [[ES-HNK-28 - Verifikasi publik lengkap|Exec Summary]]

**Lead:** Dex #dex · **Tim:** Hans #hans, Dex #dex · Dibuat 2026-10-20 dari [[FD-01 - Keputusan Usulan dan Gelombang Kerja]] dan [[FD-02 - Penelusuran Business Flow ke Backlog]] (D-30)

**Item:** HNK-28 · **Fase:** F4 · **Dependency:** HNK-08, HNK-09, HNK-23

## Deskripsi
Verifikasi publik tanpa unggah file: snapshot papan dari relay, bukti diperiksa terhadap papan di web, `rateIndex` untuk halaman indeks, teks Verify dan halaman orang luar yang benar, UFVK papan untuk juri (D-11 disetujui). Desain: [[SEQ-04 - Verifier dan Orang Luar]]. Task rinci: [[DFD-2.8 - Verifikasi dan Indeks Publik-backlogs]].

## Acceptance criteria
Status per kriteria: `TODO` / `PASS` / `FAIL` / `BLOCKED`, wajib dengan tanggal dan bukti (commit, txid, log, id tes).

| ID | Kriteria | Status | Tanggal | Bukti |
|---|---|---|---|---|
| AC-HNK-28.1 | Verify, status pelunasan, dan riwayat sendiri memakai snapshot tanpa unggah file. | TODO | — | — |
| AC-HNK-28.2 | Bukti tanpa posisi entri pertama FAIL di web, sama dengan CLI. | PASS | 2026-10-20 | `32a3977`, `d13321e`; U-HNK-28.1, I-HNK-28.2 (web dan `jitsuin verify` pada data TES- yang sama) |
| AC-HNK-28.3 | Halaman `#/index` menampilkan indeks yang sama dengan `jitsuin index`. | PASS (lokal) | 2026-10-20 | `rateIndex` sama dengan CLI (U-HNK-28.2, I-HNK-28.2); halaman `#/index` (HNK-08.T3, jitsuinfi-frontend `e9f5afb`, PR #7) menampilkan tabel yang sama dengan CLI untuk papan contoh dan papan testnet |
| AC-HNK-28.4 | "every seal checks out" tidak muncul bila surat belum lengkap; halaman orang luar menyebut yang terlihat pemegang UFVK papan. | TODO | — | — |
| AC-HNK-28.5 | Juri bisa memverifikasi dari README tanpa bertanya ke tim. | PASS | 2026-10-20 | `5fdb4e3` (PR #10, `c73009b`); I-HNK-28.3 (wallet baru, hanya data README: 11 entri, bukti `TES-INV-0003` PASS 4/4), I-HNK-28.4 (layar Verify live, verdict sama), U-HNK-28.3. Publik saat repo dibuka (DEV-19) |

## Deviasi
_Kosong._ Kalau implementasi menyimpang dari keputusan, tulis di sini **dan** di [[Backlog]] bagian Log Deviasi. Tidak ada perubahan diam-diam.
