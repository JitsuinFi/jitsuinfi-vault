---
tags: [fe-tool, "FE-05"]
type: fe-tool
id: FE-05
layer: core
status: AKTIF
updated: 2026-10-20
---

# FE-05 - jitsuin-wasm Bindings

> **Peta link:** [[FE-00 - Peta Tools FE|Peta tools]] · [[10 - FE Vault|Hub modul]] · [[FE-01 - Batasan Platform FE|Batasan platform]]

Semua kriptografi di browser (invoice, N, tanda tangan, seal, bukti, key turunan) berasal dari crate Rust `jitsuin-wasm`.

## Akar
| | |
|---|---|
| Sumber | Repo `jitsuinfi-zcash`, crate `crates/jitsuin-wasm` |
| Build | `scripts/build-wasm.sh` di frontend: `cargo build -p jitsuin-wasm --target wasm32-unknown-unknown --release`, lalu `wasm-bindgen --target web --out-dir src/wasm` |
| Alat | Rust + target `wasm32-unknown-unknown`, `wasm-bindgen-cli` 0.2.129 (dicek `wasm-bindgen --version`, 2026-10-20) |
| Hasil | `src/wasm/jitsuin_wasm.js`, `.d.ts`, `jitsuin_wasm_bg.wasm` (586 KB), di-commit karena Vercel tidak punya toolchain Rust |
| Jejak versi | `src/wasm/SOURCE` = commit zcash yang dibangun (sekarang `a252568`) |

## Dipakai di
- App: `src/lib/core.ts` (`loadWasm()`, `wasm`, `openDealStore`), semua layar di `src/pages/`.
- Landing: `src/landing/wasm.ts` memuat wasm secara malas saat bab pertama membutuhkannya; key landing dari label `TES-` (SHA-256), tidak disimpan.

## Batasan
- CSP butuh `'wasm-unsafe-eval'` (satu-satunya pelonggaran).
- Fungsi `*Bytes` menerima `Uint8Array` dan menolkannya setelah dipakai; selalu kirim salinan bila masih perlu.

## Cek cepat
```bash
cat /Users/Shenhan/HansProject/zkSNARK/jitsuinfi-frontend/src/wasm/SOURCE
```

## Status
AKTIF. Lihat juga [[Format Data]].
