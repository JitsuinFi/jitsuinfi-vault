---
tags: [fe-tool, "FE-03"]
type: fe-tool
id: FE-03
layer: build
status: AKTIF
updated: 2026-10-20
---

# FE-03 - TypeScript

> **Peta link:** [[FE-00 - Peta Tools FE|Peta tools]] · [[10 - FE Vault|Hub modul]] · [[FE-01 - Batasan Platform FE|Batasan platform]]

Bahasa semua kode frontend (vanilla TypeScript, tanpa framework UI).

## Akar
| | |
|---|---|
| Paket | `typescript` 5.9.3 (devDependency), Apache-2.0 |
| Konfigurasi | `jitsuinfi-frontend/tsconfig.json`: `target ES2022`, `module ESNext`, `moduleResolution Bundler`, `strict`, `noUnusedLocals`, `noUnusedParameters`, `isolatedModules`, `types: ["vite/client"]` |
| Tambahan HNK-22 (branch `hans/hnk-22-passkey-account`, PR #4) | `noEmit: true`, `allowImportingTsExtensions: true`, supaya modul yang dites Node bisa mengimpor `./account.ts` |

## Pola yang dipakai
- DOM helper sendiri di `src/lib/ui.ts` (`h()`, `card()`, `field()`), tanpa `innerHTML` untuk data pengguna.
- Tipe `Uint8Array<ArrayBuffer>` untuk data WebCrypto (TS 5.9 membedakan `ArrayBufferLike`).
- Tidak ada React, jadi library atau prompt berbasis React (React Bits, Framer Motion versi React, prompt MotionSites) harus diterjemahkan ke DOM biasa.

## Cek cepat
```bash
npx --prefix /Users/Shenhan/HansProject/zkSNARK/jitsuinfi-frontend tsc --noEmit -p /Users/Shenhan/HansProject/zkSNARK/jitsuinfi-frontend
```

## Status
AKTIF.
