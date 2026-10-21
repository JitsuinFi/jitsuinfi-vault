---
tags: [video, clip, "VID-07"]
type: video
id: VID-07
status: SIAP REKAM
updated: 2026-10-21
---

# VID-07 - Klip 20 Detik Coba Curang

> **Peta link:** [[Video-Workspace]] · [[VID-01 - Naskah 2 Menit]] · [[VID-02 - Storyboard dan Shot List]] · [[AC-HNK-30 - Demo juri dan narasi dari judging|AC-HNK-30]] · [[Decision Log]] D-40

Klip M-01 lalu M-03 (HNK-30.T9) yang bisa dipahami sendiri, juga dipakai di video 2 menit (HNK-14.T1). Fixture: Case File #0417, supplier fiktif "Kurogane Trading", invoice tes `TES-INV-0003-1792179703` di papan testnet; tidak ada nama atau data perusahaan nyata.

## Cara rekam
1. Buka `https://jitsuinfi.vercel.app/app.html#/try/play` di jendela 1440 × 900 (atau 390 × 844 untuk versi ponsel).
2. Mulai rekam layar sebelum halaman selesai dimuat; halaman berjalan sendiri, tanpa klik.
3. Berhenti 3 detik setelah banner "Double signature on the board" muncul.

## Ketukan (terukur 2026-10-21, build lokal)
| Detik | Layar | Teks overlay (opsional) |
|---|---|---|
| 0 – 2 | Amplop invoice | "One invoice. Already financed." |
| 2 – 4 | Nominal diketik 0.0005, tawarkan ke financier B | "Change it?" |
| ~3,6 | Verdict 偽 Forged seal | "The buyer signed other bytes." |
| 4 – 8 | Nominal dikembalikan, tawarkan lagi | "Send it as it is?" |
| ~8,4 | Verdict 重 Already pledged | "The board already holds it." |
| 8 – 12 | Take Exhibit A | |
| ~12,1 | Banner "Double signature on the board" + baris Which invoice: not stated | "B takes home proof. Nobody sees the deal." |
| 12 – 15 | Tahan | "Zcash stops double-spending. JitsuinFi stops double-financing." |

Papan: hidup dari node; bila node mati halaman memakai papan tersimpan atau salinan bawaan dan menyebutnya (tidak mengubah ketukan).
