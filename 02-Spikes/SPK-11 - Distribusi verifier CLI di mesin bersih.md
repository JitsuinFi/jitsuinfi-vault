---
tags: [spike, "SPK-11"]
type: spike
id: SPK-11
area: Tooling
owner: Dex
status: TODO
updated: 2026-10-16
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
- [ ] Dari nol sampai hasil ≤ 10 menit.
- [ ] Instruksi README teruji persis.

## Fallback kalau gagal
- Binary prebuilt macOS/Linux di GitHub Releases.

## Hasil
| Status | Tanggal | Bukti | Catatan |
|---|---|---|---|
| TODO | 2026-10-16 | Colima dijalankan (`colima start`): Docker server 29.5.2, VM **x86_64** (diemulasikan di Mac arm64), 4 CPU, 6 GB RAM; `docker run hello-world` berhasil. | Kriteria (instal verifier ≤ 10 menit) baru bisa diuji setelah HNK-09 ada. Pertimbangkan `colima start --arch aarch64` supaya build lebih cepat. |
| BLOCKED | 2026-10-16 | Docker CLI 29.9.0 dan Colima 0.10.3 terpasang, tapi daemon tidak berjalan (`colima is not running`). | Butuh persetujuan user untuk menjalankan `colima start`. |

## Catatan
_Kosong._
