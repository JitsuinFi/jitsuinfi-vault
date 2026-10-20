---
tags: [fe-tool, "FE-22"]
type: fe-tool
id: FE-22
layer: mcp-presentasi
status: TERSEDIA-BELUM-DIPAKAI
updated: 2026-10-20
---

# FE-22 - Visualize Widget

> **Peta link:** [[FE-00 - Peta Tools FE|Peta tools]] · [[10 - FE Vault|Hub modul]] · [[FE-01 - Batasan Platform FE|Batasan platform]]

Diagram, chart, atau widget HTML interaktif yang tampil langsung di chat.

## Akar
| | |
|---|---|
| Tool | `mcp__visualize__read_me` (wajib dipanggil dulu, memuat aturan gaya per modul) dan `mcp__visualize__show_widget` |
| Salinan kedua | Server claude.ai dengan tool `read_me` dan `show_widget` yang sama |
| Modul `read_me` | `diagram`, `mockup`, `interactive`, `data_viz`, `art`, `chart`, `elicitation` |

## Kapan dipakai
- Menjelaskan alur (misalnya passkey, Sign-to-Pay) atau mockup cepat di chat sebelum menulis kode.

## Batasan
- Hanya tampil di chat; bukan bagian dari repo atau situs.

## Status
TERSEDIA, belum dipakai untuk JitsuinFi.
