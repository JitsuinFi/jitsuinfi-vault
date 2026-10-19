---
tags: [reference]
---

# Quick Reference

## Buka vault
Obsidian → `File → Open folder as vault` → pilih folder `zkSNARK/vault`. Graph View dan Dataview sudah aktif dari template.

## Script vault (macOS, Python 3)
```bash
# dari folder vault
python3 scripts/check-links.py                      # audit link → target "Broken: 0"
python3 scripts/sync-vault.py                       # regenerate _Auto-Index + stub guide + cek link
python3 scripts/new-note.py --title "Nama Konsep"   # catatan konsep ke Concepts/
python3 scripts/new-item.py --kind item --id HNK-16 --title "Judul" --phase F3   # AC + TEST + ES
python3 scripts/new-item.py --kind spike --id SPK-16 --title "Judul" --area "Tooling"
python3 scripts/build-dfd.py                        # buat DFD-1 dan DFD-2.x dari scripts/dfd_model.py + cek balancing
python3 scripts/render-diagrams.py                  # render blok plantuml di 08-FlowDiagrams ke assets/*.svg
```
Versi Windows (PowerShell, belum diuji di mesin ini): `scripts/windows/check-links.ps1`, `scripts/windows/new-note.ps1`.

## Verifikasi kode (langkah 1 workflow)
```bash
# Rust
cargo check && cargo clippy -- -D warnings && cargo build
cargo test
# TypeScript (kalau ada frontend)
npx tsc --noEmit && npm run build
```

## Fakta Zcash yang sering dipakai (Okt 2026)
| Hal | Nilai |
|---|---|
| Pool aktif | Ironwood (NU6.3, sejak 28 Jul 2026); Orchard tidak menerima dana baru |
| Node lama | zcashd berhenti 18 Jul 2026; pakai Zebra/Zakura + lightwalletd/Zaino |
| Block time mainnet | 75 detik (NU7 25 detik hanya testnet sampai deadline) |
| Memo | 512 byte per output shielded |
| Fee | 5.000 zatoshi per logical action (minimal sekitar 0,0001 ZEC) |
| Crate stabil | `zcash_client_backend` 0.24, `zcash_client_sqlite` 0.22, `pczt` 0.9.3 |
| Hindari | WebZjs (rusak, tanpa Ironwood), testnet NU7, ZSA (belum di mainnet) |
| Wallet user | Zodl (dulu Zashi), bayar lewat URI/QR ZIP-321 |

Semua fakta ini wajib diverifikasi ulang di [[Spikes Hub]] sebelum build.

## ZECATHON
- Submit: demo URL berjalan + video 2 menit + deskripsi ≤ 2.000 karakter + repo publik.
- Jangan simpan draft setelah submit (status submitted hilang).
- Detail: [[ZECATHON - Aturan dan Deadline]].

Lanjut: [[Conventions]] · [[Glossary]]
