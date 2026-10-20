---
tags: [spike, "SPK-14"]
type: spike
id: SPK-14
area: Aturan
owner: Dex
status: TODO
updated: 2026-10-16
---

# SPK-14 - Repo baru lisensi dan originalitas

> **Peta link:** [[Spikes Hub]] · [[Backlog]] · [[Rencana Fase]]

**Owner:** Dex #dex · **Area:** Aturan · **Dipakai oleh:** Semua item

## Tujuan
Pastikan repo memenuhi aturan Originality dan open source.

## Hipotesis
Repo baru + lisensi permisif + audit dependency cukup.

## Langkah
1. Buat repo baru; commit pertama di dalam build window.
2. Pilih lisensi (MIT atau Apache-2.0).
3. Audit lisensi dependency (`cargo-deny` atau `cargo-license`); hindari AGPL.
4. Pastikan semua kode ditulis selama build window; tidak ada file dari proyek lain.

## Kriteria lulus
- [ ] Repo siap dipublikasikan.
- [ ] 0 dependency AGPL.
- [ ] 0 file dari luar build window (selain library).

## Fallback kalau gagal
- Ganti dependency yang lisensinya bermasalah.

## Hasil
| Status | Tanggal | Bukti | Catatan |
|---|---|---|---|
| TODO | 2026-10-16 | GitHub CLI siap (`repo`, `workflow`). | Repo baru dibuat setelah persetujuan user (membuat repo publik = publikasi). Audit lisensi setelah dependency final. |

## Catatan
Lihat D-03 di [[Decision Log]].
