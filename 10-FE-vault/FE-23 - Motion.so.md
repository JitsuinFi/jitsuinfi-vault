---
tags: [fe-tool, "FE-23"]
type: fe-tool
id: FE-23
layer: mcp-media
status: AKTIF
updated: 2026-10-20
---

# FE-23 - Motion.so

> **Peta link:** [[FE-00 - Peta Tools FE|Peta tools]] · [[10 - FE Vault|Hub modul]] · [[FE-01 - Batasan Platform FE|Batasan platform]]

Connector claude.ai untuk membuat video motion graphics yang disusun dalam kode (engine Motion).

> **Koreksi 2026-10-20:** sebelumnya keliru disebut aplikasi kalender. Yang benar: generator video motion graphics.

## Akar
| | |
|---|---|
| Server | `https://mcp.motion.so/mcp`, connector claude.ai (tool `mcp__4adc0144-…__*`) |
| Engine | `motion`, effort hanya `medium`, tanpa template |
| Lewat connector | Hanya motion graphics dalam kode (`generative_media: false`) |
| Hanya di app https://motion.so | Gambar AI, video AI, musik, audio, efek suara, voiceover |

## Tool
| Tool | Isi |
|---|---|
| `create_video` | Buat video dari `prompt`; `aspect_ratio` (16:9, 9:16, 1:1, 4:5, 21:9), `duration` (<10 s, 10 – 30 s, 30 s – 1 menit, 1 – 5 menit) |
| `create_followup` | Revisi proyek yang ada |
| `job_status`, `get_session_status` | Status render |
| `list_chats`, `get_chat`, `list_chat_messages`, `get_chat_export`, `list_chat_exports` | Riwayat dan hasil ekspor |
| `get_motion_features`, `list_engines` | Fitur dan engine yang tersedia |

## Dipakai di JitsuinFi
- Sempat dipakai untuk render hero landing; **ditolak user** ("a Motion.so render was rejected too", `MASTER.md` Amendment 3). Hero diganti diorama three.js.
- Calon pemakaian: potongan motion graphics untuk video demo 2 menit ([[Video-Workspace]]).

## Batasan
- Video yang dihasilkan tidak boleh dimuat dari server luar di situs; bila dipakai di situs, harus dibundel lokal ([[FE-01 - Batasan Platform FE]]).
- Lisensi hasil dicatat di [[VID-05 - Aset dan Lisensi]].

## Status
AKTIF (terhubung).
