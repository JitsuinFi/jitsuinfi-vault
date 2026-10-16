---
tags: [spike, "SPK-15"]
type: spike
id: SPK-15
area: Video
owner: Dave
status: BLOCKED
updated: 2026-10-16
---

# SPK-15 - Tooling produksi video

> **Peta link:** [[Spikes Hub]] · [[Backlog]] · [[Rencana Fase]]

**Owner:** Dave #dave · **Area:** Video · **Dipakai oleh:** HNK-14

## Tujuan
Pastikan alat rekam dan edit siap, dan hasil memenuhi syarat ≤ 2:00.

## Hipotesis
OBS atau QuickTime + editor sederhana cukup.

## Langkah
1. Uji rekam layar 1080p.
2. Uji rekam mikrofon.
3. Uji potong dan percepat (untuk konfirmasi 75 detik).
4. Export mp4 H.264.
5. Uji upload ke host yang diterima form.

## Kriteria lulus
- [ ] Klip uji 30 detik ter-export dan terunggah.
- [ ] Durasi dan resolusi sesuai.

## Fallback kalau gagal
- QuickTime + iMovie.

## Hasil
| Status | Tanggal | Bukti | Catatan |
|---|---|---|---|
| BLOCKED | 2026-10-16 | QuickTime Player tersedia. OBS, ffmpeg, dan iMovie tidak terpasang. | Butuh keputusan user: rekam dengan QuickTime saja, atau install OBS/editor. Uji rekam 30 detik dilakukan Dave. |

## Catatan
Lihat [[Video-Workspace]].
