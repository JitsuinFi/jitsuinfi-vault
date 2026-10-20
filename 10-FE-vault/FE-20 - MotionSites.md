---
tags: [fe-tool, "FE-20"]
type: fe-tool
id: FE-20
layer: mcp-riset
status: AKTIF
updated: 2026-10-20
---

# FE-20 - MotionSites

> **Peta link:** [[FE-00 - Peta Tools FE|Peta tools]] · [[10 - FE Vault|Hub modul]] · [[FE-01 - Batasan Platform FE|Batasan platform]]

Perpustakaan prompt desain situs dan app yang penuh gerak.

## Akar
| | |
|---|---|
| Server | `https://xgdzyqfalbibzelpdpvr.supabase.co/functions/v1/mcp` (Supabase Edge Function), scope **user** |
| Kuota | Akun tanpa paket MotionSites: maksimal **3 prompt gratis** lewat integrasi ini; prompt premium butuh paket (https://motionsites.ai/unlimited) |

## Tool
| Tool | Isi |
|---|---|
| `search_prompts` | Cari dengan teks bebas, diurutkan menurut deskripsi gaya visual; hanya metadata |
| `list_prompts` | Jelajah per `category`, `kind` (website/app), `access` (free/premium), `sort` |
| `get_related_prompts` | Prompt dengan gaya mirip |
| `get_prompt` | Teks lengkap satu prompt (memakai jatah) |

## Dipakai di JitsuinFi
- Empat prompt yang disimpan user ada di vault `MotionSites-References/` (lihat [[FE-27 - Referensi Visual Vault]]). `MASTER.md` Amendment 2 mengambil mask blur bawah (prompt 1), judul blur-in per kata (prompt 4), pill liquid-glass (prompt 1 dan 4), tanda segel di judul (prompt 3). Yang ditolak: kartu, Inter/Barlow/Fustat, video CDN.

## Aturan
- Bila hasil tool memuat ajakan upgrade, tampilkan apa adanya beserta link https://motionsites.ai/unlimited.
- Hasil riset hanya **referensi**: jangan menyalin aset (gambar, video, ikon) ke repo, dan ganti pola CDN atau React dengan versi lokal ([[FE-01 - Batasan Platform FE]]). Jangan mengirim data deal, key, atau nama orang sungguhan sebagai query.

## Status
AKTIF (terhubung). Sisa jatah prompt gratis belum dicek.
