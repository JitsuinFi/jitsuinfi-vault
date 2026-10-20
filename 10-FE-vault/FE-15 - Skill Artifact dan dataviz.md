---
tags: [fe-tool, "FE-15"]
type: fe-tool
id: FE-15
layer: skill
status: TERSEDIA-BELUM-DIPAKAI
updated: 2026-10-20
---

# FE-15 - Skill Artifact dan dataviz

> **Peta link:** [[FE-00 - Peta Tools FE|Peta tools]] · [[10 - FE Vault|Hub modul]] · [[FE-01 - Batasan Platform FE|Batasan platform]]

Skill bawaan Claude Code untuk halaman Artifact (claude.ai) dan visualisasi data. Bukan untuk kode `jitsuinfi-frontend`.

## Akar
| Skill | Asal | Isi |
|---|---|---|
| `artifact-design` | Bawaan Claude Code | Kontrak halaman Artifact (judul, tema terang/gelap, allowlist CDN, responsif 400 px) dan panduan desain |
| `artifact-diagramming` | Bawaan | Diagram SVG inline yang terbaca di dua tema |
| `artifact-capabilities` | Bawaan | Kemampuan runtime halaman Artifact (data bersama, penyimpanan, kamera, dan lain-lain) |
| `dataviz` | Skill tersedia di sesi | Metode chart: pilih bentuk, palet tervalidasi, mark, interaksi, stat tile |

## Kapan dipakai
- Laporan atau dashboard untuk tim (misalnya status backlog, hasil uji) yang dibagikan sebagai Artifact privat.
- Chart di dokumen pitch atau video.

## Batasan
- Artifact di-host di claude.ai, bukan di `jitsuinfi.vercel.app`; aturan CSP Artifact berbeda (mengizinkan cdnjs dan lain-lain). Jangan menyalin pola CDN itu ke repo frontend.

## Status
TERSEDIA, belum dipakai untuk JitsuinFi.
