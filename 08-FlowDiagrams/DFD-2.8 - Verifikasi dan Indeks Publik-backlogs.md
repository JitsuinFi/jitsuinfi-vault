---
tags: [flow, backlog]
status: DRAF
updated: 2026-10-20
---

# DFD-2.8 - Verifikasi dan Indeks Publik-backlogs

**Diagram:** [[DFD-2.8 - Verifikasi dan Indeks Publik]] · Rencana: [[FD-01 - Keputusan Usulan dan Gelombang Kerja]] · [[FD-02 - Penelusuran Business Flow ke Backlog]] · Backlog: [[Backlog]]

Task untuk proses 8.1 – 8.8. Aturan kolom sama dengan [[DFD-2.1 - Identitas dan Sesi-backlogs]].

## Task

| ID | Elemen | Task | Selesai bila | Ref | Calon item | Kandidat |
|---|---|---|---|---|---|---|
| BL-D28-01 | 8.1, F8.01 | Keputusan D-11: publikasi UFVK + birthday papan untuk juri | Keputusan tercatat; UFVK ada di README juri | C-26 | HNK-28 | Hans |
| BL-D28-02 | 8.1 – 8.6 | Review dan merge `jitsuin verify` / `jitsuin index` (PR #4, #5), README dengan perintah persis, image Docker (D-28) | HNK-09.T1 – T3 dan HNK-08.T1 – T2 selesai | HNK-09, HNK-08, D-28 | HNK-09 | Dex |
| BL-D28-03 | 8.4, F8.12 – F8.14 | Kartu bundel dipindah ke konsol node (origin node) | Bundel dibuat dari detail deal di konsol | HNK-21.T4, P-11 | HNK-26 | Dex |
| BL-D28-04 | 8.5, F8.17 – F8.18 | Teks verdict bundel di layar Verify sesuai status surat dan settled | "every seal checks out" tidak muncul bila surat belum lengkap | C-24 | HNK-28 | Dave |
| BL-D28-05 | 8.6, F8.19 – F8.21 | `rateIndex(snapshot, k)` di `jitsuin-wasm` + halaman indeks bunga | Halaman `#/index` menampilkan indeks yang sama dengan `jitsuin index` | K-9, HNK-08.T3 | HNK-28 | Dave |
| BL-D28-06 | 8.7, F8.22 – F8.24 | Layanan snapshot papan di relay (pindai dengan UFVK papan, JSON same-origin) | Verify, status pelunasan, dan riwayat sendiri memakai snapshot tanpa unggah file | P-06 | HNK-28 | Dex |
| BL-D28-07 | 8.8, F8.25 – F8.26 | Teks dan tabel halaman orang luar: pemegang UFVK papan melihat jenis entri, kelas, flag tepat waktu (TM #13 – #14) | Halaman tidak lagi menyebut "hanya hash dan tanda tangan" | C-25 | HNK-28 | Dave |
| BL-D28-08 | Uji | Juri menjalankan README dari mesin bersih (Docker atau `cargo install`) dan mendapat PASS untuk bundel contoh | Kasus tercatat di TEST-HNK-09 | HNK-09.T3 | HNK-17 | Dave |

## Sudah ada (tanpa task baru)

- 8.1 – 8.3 CLI (`init-fvk`, `scan`, `check_proof`), 8.4 `bundleBuild`, 8.5 `check_bundle` dan `bundleOnBoard`, 8.8 `boardMemoDescribe`.
