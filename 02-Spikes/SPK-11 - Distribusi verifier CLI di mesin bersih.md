---
tags: [spike, "SPK-11"]
type: spike
id: SPK-11
area: Tooling
owner: Dex
status: PASS
updated: 2026-10-19
---

# SPK-11 - Distribusi verifier CLI di mesin bersih

> **Peta link:** [[Spikes Hub]] · [[Backlog]] · [[Rencana Fase]]

**Owner:** Dex #dex · **Area:** Tooling · **Dipakai oleh:** HNK-09

## Tujuan
Pastikan juri bisa menjalankan `hanko verify` tanpa setup rumit.

## Hipotesis
Image Docker minimal atau `cargo install` cukup.

## Langkah
1. Buat image Docker minimal dan opsi `cargo install`.
2. Uji di container/mesin bersih.
3. Ukur waktu dari nol sampai hasil verifikasi.

## Kriteria lulus
- [x] Dari nol sampai hasil ≤ 10 menit. (9 mnt 10 dtk di runner bersih 4 vCPU; margin tipis)
- [x] Instruksi README teruji persis. (CI menjalankan perintah Docker di README dan `diff` dengan output yang diharapkan)

## Fallback kalau gagal
- Binary prebuilt macOS/Linux di GitHub Releases.

## Hasil
| Status | Tanggal | Bukti | Catatan |
|---|---|---|---|
| PASS | 2026-10-19 | Workflow `verifier image` di jitsuinfi-zcash PR #4 (https://github.com/JitsuinFi/jitsuinfi-zcash/actions/runs/39239022151): runner GitHub ubuntu-latest baru (4 vCPU), tanpa cache Docker. `docker build -t jitsuin .` 550 dtk: `cargo install` zcash-devtool `b532d4c` 7 mnt 23 dtk, `cargo install --path crates/jitsuin-cli` 1 mnt 10 dtk, sisanya pull image dasar + apt. Perintah contoh dari README di dalam container < 1 dtk, output = `examples/verify/expected-output.txt` (`diff` kosong). Image 197 MB; `zcash-devtool` ada di image. | Dex menguji di runner CI karena laptop Windows Dex tidak punya Docker. Sebagian besar waktu = kompilasi zcash-devtool, jadi mesin 2 core bisa lewat 10 menit. Jalur cepat untuk juri: image jadi di registry (pull ±200 MB) atau binary prebuilt (fallback); menerbitkannya butuh izin Hans. |
| TODO | 2026-10-16 | Colima dijalankan (`colima start`): Docker server 29.5.2, VM **x86_64** (diemulasikan di Mac arm64), 4 CPU, 6 GB RAM; `docker run hello-world` berhasil. | Kriteria (instal verifier ≤ 10 menit) baru bisa diuji setelah HNK-09 ada. Pertimbangkan `colima start --arch aarch64` supaya build lebih cepat. |
| BLOCKED | 2026-10-16 | Docker CLI 29.9.0 dan Colima 0.10.3 terpasang, tapi daemon tidak berjalan (`colima is not running`). | Butuh persetujuan user untuk menjalankan `colima start`. |

## Catatan
_Kosong._
