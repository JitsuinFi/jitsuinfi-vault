---
tags: [fe-tool, "FE-02"]
type: fe-tool
id: FE-02
layer: build
status: AKTIF
updated: 2026-10-20
---

# FE-02 - Vite

> **Peta link:** [[FE-00 - Peta Tools FE|Peta tools]] · [[10 - FE Vault|Hub modul]] · [[FE-01 - Batasan Platform FE|Batasan platform]]

Build tool dan dev server untuk dua halaman: landing (`index.html`) dan app (`app.html`).

## Akar
| | |
|---|---|
| Paket | `vite` 8.3.4 (devDependency), lisensi MIT, https://vite.dev |
| Bundler di dalamnya | Rolldown (Vite 8); peringatan ukuran chunk menyebut `build.rolldownOptions` |
| Konfigurasi | `jitsuinfi-frontend/vite.config.ts` |
| Dipasang | Sejak scaffold HNK-10.T1 |

## Konfigurasi yang dipakai
- `build.target: "es2022"`.
- `assetsInlineLimit: 0`: semua aset jadi file terpisah di `dist/assets/` (tidak ada `data:` URI besar), cocok dengan CSP.
- Dua input: `landing` (index.html) dan `app` (app.html).
- Ukuran build terakhir: `landing-*.js` 796 KB (three.js, anime.js, Motion, Lenis), `app-*.js` 44 KB, `jitsuin_wasm-*.js` 20 KB + `.wasm` 586 KB.

## Perintah (`package.json`)
| Script | Isi |
|---|---|
| `npm run dev` | `vite` (dev server, default port 5173) |
| `npm run build` | `tsc --noEmit && vite build` |
| `npm run preview` | `vite preview` (port 4173), dipakai untuk cek visual karena CSP |
| `npm run wasm` | build binding wasm, lihat [[FE-05 - jitsuin-wasm Bindings]] |

Konfigurasi pane browser ada di `zkSNARK/.claude/launch.json`: `jitsuinfi-dev` (5173, sering pindah ke 5175) dan `jitsuinfi-preview` (4173).

## Batasan
- Dev server menyuntikkan style inline yang diblokir CSP; tampilan dev bisa tanpa gaya. Uji tampilan di preview produksi.
- Peringatan chunk > 500 KB pada landing (three.js); belum dipecah.

## Cek cepat
```bash
npm --prefix /Users/Shenhan/HansProject/zkSNARK/jitsuinfi-frontend run build
```

## Status
AKTIF.
