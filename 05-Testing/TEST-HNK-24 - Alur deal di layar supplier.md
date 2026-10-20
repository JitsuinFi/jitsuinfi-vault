---
tags: [test, "HNK-24"]
type: test
id: HNK-24
phase: F5
unit: PARSIAL
integrasi: PARSIAL
e2e: PARSIAL
updated: 2026-10-20
---

# TEST-HNK-24 - Alur deal di layar supplier

> **Peta link:** [[Testing Hub]] · [[Backlog]] · [[AC-HNK-24 - Alur deal di layar supplier|AC]] · **Test** · [[ES-HNK-24 - Alur deal di layar supplier|Exec Summary]]

## 1. Unit
Logika murni, cepat, tanpa DB dan tanpa chain.

| ID | Kasus | Hasil | Tanggal | Bukti |
|---|---|---|---|---|
| U-HNK-24.1 | Test vector key per invoice dan kunci penyimpanan; key stabil per (master, id, buyer_pk), berbeda bila salah satunya berubah; byte master dinolkan | PASS | 2026-10-20 | `keys::tests::*`, wasm `supplier_master_keys_and_storage_keys`; vector = Python `hashlib`; `bash scripts/check.sh` hijau (`a252568`) |
| U-HNK-24.2 | `invoice_id` kembar ditolak | PASS | 2026-10-20 | `supplier-deal.test.ts` (`invoiceIdTaken`) dan di layar (I-HNK-24.3) |
| U-HNK-24.4 | Timeline dan langkah berikutnya, urutan terbaru dulu, kode penawaran bolak-balik dan kode tidak lengkap ditolak, cek alamat shielded | PASS | 2026-10-20 | `npm test` 12/12 (`17a01ea`); `tsc --noEmit` bersih; `vite build` lulus |
| U-HNK-24.5 | Entri menunggu permintaan financier (`nextAction`); kode permintaan entri bolak-balik (dengan atau tanpa kelas dan tag); kode rusak, salt pendek, satu kelas saja, kelas 8, tag salah ditolak; permintaan untuk N lain atau financier lain tidak cocok | PASS | 2026-10-20 | `npm test` 16/16 (`7a0b911`); `tsc --noEmit` bersih; `vite build` lulus |
| U-HNK-24.3 | Store terenkripsi: sesi baru membaca dokumen, byte key dinolkan (juga saat gagal), nama record tidak memuat id, isi terenkripsi, key lain tidak bisa membaca, record diubah ditolak, peran terpisah, ganti dan hapus | PASS | 2026-10-20 | `npm test` (6/6, Node test runner, `c7d4b1b`); `tsc --noEmit` bersih; `vite build` lulus |

## 2. Integrasi
Skrip vs DB/chain sungguhan. Semua artefak memakai prefix `TES-` (invoice, akun, label, order).

| ID | Skenario | Hasil | Tanggal | Bukti (txid/log) |
|---|---|---|---|---|
| I-HNK-24.1 | Siklus supplier lewat relay dan node testnet | TODO | — | — |
| I-HNK-24.3 | Layar Supplier ujung ke ujung di browser (dev server), buyer dan financier disimulasikan dengan wasm: unlock test secret; invoice `TES-INV-S24`; nomor ganda ditolak; tanda tangan palsu ditolak, yang sah diterima; penawaran; entri dengan pembuka `financierCommitment` dan kelas 3/1 (komitmen sama, `Registered` di snapshot); surat dengan PDF salah dan financier lain ditolak, yang benar disegel (`AwaitingSeal:Buyer`); advance kurang ditandai, yang cocok menutup deal; reload: terkunci, unlock ulang menampilkan deal "Complete"; test secret lain melihat 0 deal. Build produksi di 375 px tanpa scroll horizontal | PASS | 2026-10-20 | Skrip di pane browser; database `jitsuinfi-deals` dihapus di kedua origin (sisa 0) |
| I-HNK-24.4 | Permintaan entri di browser (dev server): setelah penawaran, kartu "Wait for the entry request" tanpa isian salt, timeline "wait for the financier's entry request"; kode rusak, N lain, financier lain ditolak dan kartu tetap menunggu; permintaan sah (`financierCommitment`, kelas 3/1) lalu "Sign entry": memo `Register` dengan komitmen sama dan kelas 3/1; setelah reload dan unlock ulang tetap "Board entry signed" | PASS | 2026-10-20 | Database `jitsuinfi-deals` dihapus (sisa 0) |
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
