---
tags: [fe-tool, "FE-21"]
type: fe-tool
id: FE-21
layer: mcp-riset
status: AKTIF
updated: 2026-10-20
---

# FE-21 - Refero

> **Peta link:** [[FE-00 - Peta Tools FE|Peta tools]] · [[10 - FE Vault|Hub modul]] · [[FE-01 - Batasan Platform FE|Batasan platform]]

Referensi desain: layar dan alur nyata (web dan iOS), gaya visual terkurasi, situs, aplikasi.

## Akar
| | |
|---|---|
| Server | `https://api.refero.design/mcp` (HTTP), `refero_server` 0.2.0 |
| Dipasang | 2026-10-20: `claude mcp add --transport http refero https://api.refero.design/mcp --header "Authorization: Bearer <token>"` |
| Scope | **local** (hanya proyek `zkSNARK`, hanya user ini); token disimpan di `~/.claude.json`, tidak di repo atau vault |
| Token | Pernah ditempel di chat; disarankan rotasi di dashboard Refero |
| Ketersediaan | Aktif di sesi sejak 2026-10-20 (tool `mcp__refero__refero_*`) |

## Tool (10)
| Tool | Isi |
|---|---|
| `refero_search_screens` | Cari layar UI (semantic); `query`, `platform`, `page` |
| `refero_get_screen`, `refero_get_screen_image`, `refero_get_similar_screens` | Detail, gambar (thumbnail atau penuh), layar serupa |
| `refero_search_flows`, `refero_get_flow` | Alur pengguna; tiap langkah dengan goal, action, system response |
| `refero_search_styles`, `refero_get_style` | Gaya desain terkurasi: warna, tipografi, pola; titik awal arah visual |
| `refero_search_sites`, `refero_search_apps` | Cari situs atau aplikasi iOS menurut nama atau industri |

## Skill pendamping
- Server menyarankan skill `refero-design`. **Belum dipasang.** Perintahnya (perlu izin user): `npx skills add https://github.com/referodesign/refero_skill --skill refero-design`.

## Aturan
- Hasil riset hanya **referensi**: jangan menyalin aset (gambar, video, ikon) ke repo, dan ganti pola CDN atau React dengan versi lokal ([[FE-01 - Batasan Platform FE]]). Jangan mengirim data deal, key, atau nama orang sungguhan sebagai query.

## Status
AKTIF (terhubung), belum dipakai.
