---
tags: [fe-tool, "FE-01"]
type: fe-tool
id: FE-01
layer: platform
status: AKTIF
updated: 2026-10-20
---

# FE-01 - Batasan Platform FE

> **Peta link:** [[FE-00 - Peta Tools FE|Peta tools]] · [[10 - FE Vault|Hub modul]] · [[FE-01 - Batasan Platform FE|Batasan platform]]

Aturan yang mengikat **semua** tool di modul ini. Tool yang melanggar salah satunya tidak boleh dipakai apa adanya, hanya diadaptasi.

## Akar
| Aturan | Sumber | Bentuk di kode |
|---|---|---|
| Tanpa CDN, tanpa request pihak ketiga, tanpa tracker | Permintaan user; [[Landing Page - Brief]]; README `jitsuinfi-frontend` | Semua JS, CSS, WASM, font dibundel Vite (`vite.config.ts`, `assetsInlineLimit: 0`) |
| CSP same-origin | `vercel.json` (header produksi untuk semua path), `<meta>` CSP di `index.html` dan `app.html` | Tiga versi, lihat tabel CSP di bawah |
| Header keamanan lain | `vercel.json` | `X-Content-Type-Options: nosniff`, `Referrer-Policy: no-referrer`, `Permissions-Policy: camera=(), microphone=(), geolocation=()` |
| Relay dan backend lewat origin sendiri | D-33, [[SEQ-00 - Autentikasi dan Onboarding]] | Rewrite Vercel `/api/*` ke relay (HNK-23.T6); browser tidak memanggil Supabase atau Railway langsung |
| Key dan secret tidak pernah ke repo, vault, log | Aturan proyek | Passkey PRF di browser, `*Bytes` wasm menolkan key |
| Push, deploy, merge hanya setelah persetujuan user | [[Workflow Development]] | Merge ke `main` frontend = deploy produksi Vercel |
| Lokal dulu, repo privat sampai menjelang submit | D-17, D-25 | — |
| Dependensi baru wajib izin user | Aturan proyek | Lihat tabel library di [[FE-00 - Peta Tools FE]] |

## CSP per sumber (dicek 2026-10-20)
| Sumber | Berlaku untuk | Isi |
|---|---|---|
| `vercel.json` header | Produksi dan preview Vercel, semua path | `default-src 'self'; script-src 'self' 'wasm-unsafe-eval'; style-src 'self'; img-src 'self' data:; font-src 'self'; connect-src 'self'; object-src 'none'; base-uri 'none'; form-action 'none'; frame-ancestors 'none'` |
| `<meta>` di `index.html` | Landing, juga saat `vite dev`/`preview` | Sama dengan header, **tanpa** `frame-ancestors` (direktif itu memang tidak berlaku di `<meta>`) |
| `<meta>` di `app.html` | App, juga saat `vite dev`/`preview` | Sama dengan landing, **tanpa** `font-src` (jatuh ke `default-src 'self'`, efeknya sama) |

Di produksi browser menerapkan header dan meta sekaligus (keduanya harus lolos).

## Akibatnya untuk tool
- **Library npm**: boleh, asal dibundel. Tidak boleh memuat aset dari URL luar saat runtime (misalnya font Google, video CloudFront, gambar dari CDN).
- **Prompt atau referensi desain** (MotionSites, Mobbin, Refero, ScreensDesign): hanya inspirasi. Kode yang mereka sarankan sering memakai React, Tailwind CDN, Google Fonts, atau video dari CDN; semua itu harus diganti versi lokal.
- **Style inline**: `style-src 'self'` memblokir atribut `style` dan `<style>` inline. Akibatnya Vite dev server tampil tanpa gaya untuk sebagian elemen; cek visual memakai build produksi (`npm run build && npm run preview`). Lihat [[FE-02 - Vite]].
- **Overlay atau injeksi skrip ke halaman** (misalnya mode `live` impeccable): bisa terblokir CSP. Lihat [[FE-14 - impeccable]].
- **Kamera dan mikrofon**: dimatikan `Permissions-Policy`, jadi QR dipindai di luar browser atau ditempel.

## Cek cepat
```bash
curl -sI https://jitsuinfi.vercel.app | grep -i content-security-policy
```

## Status
AKTIF, berlaku untuk semua tool.
