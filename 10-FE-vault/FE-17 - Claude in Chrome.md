---
tags: [fe-tool, "FE-17"]
type: fe-tool
id: FE-17
layer: mcp-verifikasi
status: TERSEDIA-BELUM-DIPAKAI
updated: 2026-10-20
---

# FE-17 - Claude in Chrome

> **Peta link:** [[FE-00 - Peta Tools FE|Peta tools]] · [[10 - FE Vault|Hub modul]] · [[FE-01 - Batasan Platform FE|Batasan platform]]

Ekstensi yang mengendalikan Chrome asli user (dengan login milik user).

## Akar
| | |
|---|---|
| Asal | Ekstensi Claude in Chrome, tool `mcp__claude-in-chrome__*` (dimuat lewat ToolSearch) |
| Beda dengan pane | Memakai profil dan login Chrome user; pane bawaan memakai profil terpisah ([[FE-16 - Claude Browser Pane]]) |

## Tool
`tabs_context_mcp`, `tabs_create_mcp`, `tabs_close_mcp`, `navigate`, `read_page`, `get_page_text`, `find`, `form_input`, `computer`, `javascript_tool`, `read_console_messages`, `read_network_requests`, `resize_window`, `gif_creator` (rekaman GIF), `upload_image`, `file_upload`, `shortcuts_list`, `shortcuts_execute`, `list_connected_browsers`, `select_browser`, `switch_browser`, `browser_batch`.

## Kapan dipakai
- Hanya bila user memintanya, misalnya untuk merekam GIF demo atau menguji passkey dengan Chrome dan iCloud Keychain milik user.

## Batasan
- Bekerja di akun asli user: tidak boleh keluar akun, mengubah kredensial, atau bertindak di luar tugas.

## Status
TERSEDIA, belum dipakai.
