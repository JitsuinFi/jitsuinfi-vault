---
tags: [workflow, plan]
---

# Rencana Fase

**Bagian dari:** [[01 - Workflow]] · Kembali: [[START-HERE]] · Terkait: [[Workflow Development]] · [[Backlog]] · [[Spikes Hub]]

Urutan fase = urutan dependency. Fase berikutnya hanya boleh dimulai kalau **gerbang** fase sebelumnya lulus (status di file AC atau spike). Tanggal 2026, perkiraan.

| Fase | Isi | Item (lead) | Tanggal target | Gerbang (harus lulus) |
|---|---|---|---|---|
| **F0** | Spike semua tools dan resource | SPK-01 – SPK-15 (Hans #hans: integrasi Zcash; Dex #dex: toolchain, infra, repo; Dave #dave: aturan, video) | 16–17 Okt | Semua spike kritis `PASS`, atau fallback diputuskan user dan dicatat di [[Decision Log]] |
| **F1** | Logika inti (tanpa chain) + quality gate | HNK-01, HNK-02 (Hans #hans), HNK-16 (Dex #dex) | 18 Okt | AC HNK-01, HNK-02, HNK-16 `PASS` |
| **F2** | Integrasi Zcash | HNK-03, HNK-04 (Hans #hans) | 19–20 Okt | AC HNK-03 dan HNK-04 `PASS` (txid mainnet tercatat) |
| **F3** | Alur bisnis | HNK-05, HNK-06, HNK-07 (Hans #hans) | 20–23 Okt | AC HNK-05 – HNK-07 `PASS` |
| **F4** | Lapisan bukti dan pasar | HNK-08, HNK-09 (Dex #dex), HNK-12 (Hans #hans, dari Dave, D-35) | 23–24 Okt | AC HNK-08, HNK-09, HNK-12 `PASS` |
| **F5** | Aplikasi, privasi, materi pitch | HNK-10, HNK-11, HNK-18 (Hans #hans, dari Dave, D-35) | 21–24 Okt (paralel) | AC HNK-10, HNK-11, HNK-18 `PASS` |
| **F6** | Validasi dan submission | HNK-13, HNK-14, HNK-17 (Hans #hans, dari Dave, D-35; submit final oleh Hans #hans) | 25–27 Okt | Status "submitted" terkunci sebelum 27 Okt 23:59 UTC |
| **F7** | Stretch: JitsuinFi Vault | HNK-15 (Hans #hans) | Hanya kalau F3 lulus paling lambat 23 Okt | Keputusan user |

Pembagian kerja dan rincian task per orang: [[Backlog]] (target awal Hans 40% · Dex 30% · Dave 30%; sejak 2026-10-20 semua task Dave dipegang Hans, D-35).

## Spike kritis (wajib PASS sebelum F1/F2)
SPK-01, SPK-02, SPK-03, SPK-05, SPK-06. SPK-04 tidak lagi kritis sejak D-15 (Zodl opsional). Detail: [[Spikes Hub]].

## Aturan potong scope (diputuskan sekarang, bukan saat panik)
- SPK-03 gagal lewat crate langsung → pindah ke `zcash-devtool` atau Zally. **Jangan** pindah ke WebZjs. _(Larangan awal "jangan pindah ke testnet NU7" ditimpa D-13 pada 2026-10-16: development memang di testnet NU7 dengan crate pre-release, lihat DEV-03.)_
- SPK-04 gagal (Zodl tidak meneruskan memo dari URI) → pembayaran demo dikirim dari wallet backend, Zodl hanya untuk penerimaan.
- F3 belum lulus 23 Okt → HNK-15 dibatalkan (catat DEV), HNK-08 dan HNK-12 dipersempit.
- HNK-10 molor → web app minimal; demo bertumpu pada CLI dan verifier.
- Setiap pemotongan scope dicatat sebagai `DEV-xx` di [[Backlog]] dan disetujui user.
