---
tags: [ac, "HNK-28"]
type: ac
id: HNK-28
phase: F4
lead: Dex
owners: [Hans, Dex, Dave]
status: TODO
updated: 2026-10-20
---

# AC-HNK-28 - Verifikasi publik lengkap

> **Peta link:** [[AC Hub]] · [[Backlog]] · **AC** · [[TEST-HNK-28 - Verifikasi publik lengkap|Test]] · [[ES-HNK-28 - Verifikasi publik lengkap|Exec Summary]]

**Lead:** Dex #dex · **Tim:** Hans #hans, Dex #dex, Dave #dave · Dibuat 2026-10-20 dari [[FD-01 - Keputusan Usulan dan Gelombang Kerja]] dan [[FD-02 - Penelusuran Business Flow ke Backlog]] (D-30)

**Item:** HNK-28 · **Fase:** F4 · **Dependency:** HNK-08, HNK-09, HNK-23

## Deskripsi
Verifikasi publik tanpa unggah file: snapshot papan dari relay, bukti diperiksa terhadap papan di web, `rateIndex` untuk halaman indeks, teks Verify dan halaman orang luar yang benar, UFVK papan untuk juri (D-11 disetujui). Desain: [[SEQ-04 - Verifier dan Orang Luar]]. Task rinci: [[DFD-2.8 - Verifikasi dan Indeks Publik-backlogs]].

## Acceptance criteria
Status per kriteria: `TODO` / `PASS` / `FAIL` / `BLOCKED`, wajib dengan tanggal dan bukti (commit, txid, log, id tes).

| ID | Kriteria | Status | Tanggal | Bukti |
|---|---|---|---|---|
| AC-HNK-28.1 | Verify, status pelunasan, dan riwayat sendiri memakai snapshot tanpa unggah file. | TODO | — | — |
| AC-HNK-28.2 | Bukti tanpa posisi entri pertama FAIL di web, sama dengan CLI. | TODO | — | — |
| AC-HNK-28.3 | Halaman `#/index` menampilkan indeks yang sama dengan `jitsuin index`. | TODO | — | — |
| AC-HNK-28.4 | "every seal checks out" tidak muncul bila surat belum lengkap; halaman orang luar menyebut yang terlihat pemegang UFVK papan. | TODO | — | — |
| AC-HNK-28.5 | Juri bisa memverifikasi dari README tanpa bertanya ke tim. | TODO | — | — |

## Deviasi
_Kosong._ Kalau implementasi menyimpang dari keputusan, tulis di sini **dan** di [[Backlog]] bagian Log Deviasi. Tidak ada perubahan diam-diam.
