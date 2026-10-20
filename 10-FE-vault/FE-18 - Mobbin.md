---
tags: [fe-tool, "FE-18"]
type: fe-tool
id: FE-18
layer: mcp-riset
status: AKTIF
updated: 2026-10-20
---

# FE-18 - Mobbin

> **Peta link:** [[FE-00 - Peta Tools FE|Peta tools]] · [[10 - FE Vault|Hub modul]] · [[FE-01 - Batasan Platform FE|Batasan platform]]

Perpustakaan layar dan alur aplikasi nyata (web dan iOS).

## Akar
| | |
|---|---|
| Server | `https://api.mobbin.com/mcp` (HTTP), scope **user** (semua proyek). Koneksi sempat putus (`ECONNRESET`) 2026-10-20 lalu tersambung lagi |
| Tool | `mcp__mobbin__search_screens`, `mcp__mobbin__search_flows`, `mcp__mobbin__search_sections` |

## Kemampuan
| Tool | Isi | Parameter penting |
|---|---|---|
| `search_screens` | Cari satu layar dengan bahasa alami | `query`, `platform` (`ios`/`web`), `mode` (`deep`/`standard`), `limit` ≤ 30, `exclude_screen_ids` |
| `search_flows` | Alur multi-langkah (onboarding, checkout) | `query`, `platform`, `limit` ≤ 10, `page` ≤ 20 |
| `search_sections` | Bagian situs (hero, pricing, footer) | `query`, `limit` ≤ 30, `page` |

Semua tool menerima `output_destination` (untuk proyek ini: `code`) dan `task_intent` (satu kalimat bahasa Inggris, tanpa data pribadi).

## Aturan pemakaian
- Kutip setiap layar dengan link `mobbin_url`; URL gambar kedaluwarsa 30 hari.
- Bila hasil berisi `ai_usage_notice`, tampilkan teksnya apa adanya.
- Hasil riset hanya **referensi**: jangan menyalin aset (gambar, video, ikon) ke repo, dan ganti pola CDN atau React dengan versi lokal ([[FE-01 - Batasan Platform FE]]). Jangan mengirim data deal, key, atau nama orang sungguhan sebagai query.

## Calon pemakaian
Referensi alur passkey sign-in (HNK-22), daftar deal (HNK-24), dan layar app (HNK-21).

## Status
AKTIF (terhubung), belum dipakai untuk JitsuinFi.
