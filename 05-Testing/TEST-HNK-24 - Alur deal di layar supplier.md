---
tags: [test, "HNK-24"]
type: test
id: HNK-24
phase: F5
unit: PARSIAL
integrasi: PARSIAL
e2e: TODO
updated: 2026-10-20
---

# TEST-HNK-24 - Alur deal di layar supplier

> **Peta link:** [[Testing Hub]] · [[Backlog]] · [[AC-HNK-24 - Alur deal di layar supplier|AC]] · **Test** · [[ES-HNK-24 - Alur deal di layar supplier|Exec Summary]]

## 1. Unit
Logika murni, cepat, tanpa DB dan tanpa chain.

| ID | Kasus | Hasil | Tanggal | Bukti |
|---|---|---|---|---|
| U-HNK-24.1 | Test vector key per invoice dan kunci penyimpanan; key stabil per (master, id, buyer_pk), berbeda bila salah satunya berubah; byte master dinolkan | PASS | 2026-10-20 | `keys::tests::*`, wasm `supplier_master_keys_and_storage_keys`; vector = Python `hashlib`; `bash scripts/check.sh` hijau (`a252568`) |
| U-HNK-24.2 | `invoice_id` kembar ditolak | TODO | — | Layar (HNK-24.T2) |
| U-HNK-24.3 | Store terenkripsi: sesi baru membaca dokumen, byte key dinolkan (juga saat gagal), nama record tidak memuat id, isi terenkripsi, key lain tidak bisa membaca, record diubah ditolak, peran terpisah, ganti dan hapus | PASS | 2026-10-20 | `npm test` (6/6, Node test runner, `c7d4b1b`); `tsc --noEmit` bersih; `vite build` lulus |

## 2. Integrasi
Skrip vs DB/chain sungguhan. Semua artefak memakai prefix `TES-` (invoice, akun, label, order).

| ID | Skenario | Hasil | Tanggal | Bukti (txid/log) |
|---|---|---|---|---|
| I-HNK-24.1 | Siklus supplier lewat relay dan node testnet | TODO | — | — |
| I-HNK-24.2 | IndexedDB di browser (dev server, pane Chromium): `openDealStore` dengan `storageKeysBytes`; persisten, bertahan setelah reload, key lain tidak membaca, master nol; landing dan `app.html` (build produksi) tanpa error console | PASS | 2026-10-20 | Skrip di pane browser; artefak `TES-INV-STORE`, `TES-INV-RELOAD` dihapus, sisa record 0 |

**Bukti pembersihan:** sisa artefak off-chain `TES-` = **0** (record IndexedDB uji dihapus, `count()` = 0, 2026-10-20). Artefak on-chain tidak bisa dihapus; catat txid-nya di tabel di atas. Data produksi tidak boleh tersentuh.

## 3. E2E
Panduan langkah demi langkah untuk user.

- [ ] Invoice baru
- [ ] Kirim ke buyer
- [ ] Tawarkan ke financier
- [ ] Tanda tangani entri
- [ ] Segel surat
- [ ] Lihat advance

| Langkah | Hasil diharapkan | Hasil aktual | Status |
|---|---|---|---|
| 1 | _TODO_ | — | TODO |
