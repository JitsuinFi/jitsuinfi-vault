---
tags: [fe-tool, "FE-16"]
type: fe-tool
id: FE-16
layer: mcp-verifikasi
status: AKTIF
updated: 2026-10-20
---

# FE-16 - Claude Browser Pane

> **Peta link:** [[FE-00 - Peta Tools FE|Peta tools]] · [[10 - FE Vault|Hub modul]] · [[FE-01 - Batasan Platform FE|Batasan platform]]

Browser bawaan aplikasi Claude desktop. Alat verifikasi utama frontend: menjalankan server, membuka halaman, membaca DOM, menjalankan skrip uji, dan mengukur lebar ponsel.

## Akar
| | |
|---|---|
| Asal | Bawaan Claude desktop (Code tab), tool `mcp__Claude_Browser__*` |
| Konfigurasi server | `zkSNARK/.claude/launch.json`: `jitsuinfi-dev` (`vite`, port 5173, otomatis pindah ke 5175 bila terpakai) dan `jitsuinfi-preview` (`vite preview`, port 4173, `--strictPort`) |
| Data | Profil browser terpisah dari Chrome user; IndexedDB dan localStorage per origin (`localhost:5175`, `localhost:4173`) |

## Tool
| Kelompok | Tool |
|---|---|
| Server | `preview_start`, `preview_stop`, `preview_list`, `preview_logs` |
| Navigasi dan tab | `navigate`, `tabs_context`, `tabs_create`, `tabs_select`, `tabs_close` |
| Membaca | `read_page` (pohon aksesibilitas), `get_page_text`, `find`, `read_console_messages`, `read_network_requests` |
| Aksi | `computer` (klik, ketik, screenshot, zoom), `form_input`, `javascript_tool`, `browser_batch` |
| Viewport | `resize_window` (`mobile` 375×812, `tablet`, `desktop`; mode gelap/terang) |

## Cara dipakai di JitsuinFi
- Uji alur ujung ke ujung dengan `javascript_tool`: I-HNK-24.3, I-HNK-24.4 (layar supplier), I-HNK-22.2 (akun passkey dengan `navigator.credentials` palsu).
- Cek tampilan di **build produksi** (`jitsuinfi-preview`), karena CSP memblokir style inline dev server.
- Uji 375 px: `resize_window` preset `mobile`, lalu bandingkan `document.documentElement.scrollWidth` dengan `innerWidth`.
- Bersihkan data uji setelah tes: navigasi ke `/` (agar koneksi IndexedDB tertutup), lalu `indexedDB.deleteDatabase("jitsuinfi-deals")` dan hapus `jitsuinfi-profile` di setiap origin.

## Batasan
- Tidak ada sensor biometrik: passkey asli (Touch ID) tidak bisa diuji otomatis, hanya dengan authenticator palsu. Uji nyata oleh user (HNK-22.T7).
- Cache bundle lama bisa muncul setelah rebuild; muat ulang dengan `location.reload(true)`.

## Status
AKTIF.
