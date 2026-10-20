---
tags: [fe-tool, "FE-19"]
type: fe-tool
id: FE-19
layer: mcp-riset
status: AKTIF
updated: 2026-10-20
---

# FE-19 - ScreensDesign

> **Peta link:** [[FE-00 - Peta Tools FE|Peta tools]] · [[10 - FE Vault|Hub modul]] · [[FE-01 - Batasan Platform FE|Batasan platform]]

Riset aplikasi mobile: layar dan alur terekam, screenshot App Store, ulasan, developer, koleksi.

## Akar
| | |
|---|---|
| Server | `https://api.screensdesign.com/v1/mcp` (HTTP), scope **user** |
| Kuota | Setiap hasil memakai jatah riset; cek dengan `describe_screensdesign_mcp` |

## Tool (19)
| Kelompok | Tool |
|---|---|
| Aplikasi | `search_apps`, `similar_apps`, `app_detail`, `app_screens`, `app_store_reviews` |
| Layar dan alur terekam | `search_screens`, `screen_detail`, `find_similar_screens`, `search_flows` |
| Kreatif App Store | `search_store_screens` |
| Pasar luas | `search_market_apps`, `similar_market_apps`, `market_app_detail` (gambar = kreatif listing, bukan UI terverifikasi) |
| Lain | `search_developers`, `list_collections`, `get_collection`, `get_me`, `describe_screensdesign_mcp`, `get_screensdesign_skill` |

## Aturan pemakaian
- Hanya riset: jangan mengklaim tool ini membuat atau merender layar.
- Salin URL publik persis seperti yang dikembalikan; jangan membuat URL sendiri.
- Hasil riset hanya **referensi**: jangan menyalin aset (gambar, video, ikon) ke repo, dan ganti pola CDN atau React dengan versi lokal ([[FE-01 - Batasan Platform FE]]). Jangan mengirim data deal, key, atau nama orang sungguhan sebagai query.

## Relevansi
Fokus mobile app; JitsuinFi adalah web app. Berguna untuk pola mobile (layar 375 px, alur wallet, passkey di iOS).

## Status
AKTIF (terhubung), belum dipakai untuk JitsuinFi.
