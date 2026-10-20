---
tags: [es, "HNK-24"]
type: es
id: HNK-24
phase: F5
status: PARSIAL
updated: 2026-10-20
---

# ES-HNK-24 - Alur deal di layar supplier

> **Peta link:** [[Exec Summary Hub]] · [[Backlog]] · [[AC-HNK-24 - Alur deal di layar supplier|AC]] · [[TEST-HNK-24 - Alur deal di layar supplier|Test]] · **Exec Summary**

## Apa diubah
- **T1 (Hans):** `SupplierMaster` di `jitsuin-core` (`keys.rs`): key per invoice dari master supplier, `invoice_id`, dan `invoice_pk(k)` buyer; kunci penyimpanan perangkat dari master peran. wasm: `supplierInvoicePublicKeyBytes`, `supplierInvoiceSecretBytes`, `storageKeysBytes` (master dinolkan).
- **T3 (Hans):** `src/lib/store.ts` di frontend: `DealStore` per peran di IndexedDB, AES-256-GCM, nama record HMAC, fallback memori; `openDealStore(role, master)` di `core.ts`; wasm frontend dibangun ulang dari `a252568`; `npm test`.
- **T2, T4 – T9 (Dave, backup Hans, DEV-15):** layar Supplier ditulis ulang: unlock passkey supplier atau test secret; invoice dengan key turunan (tanpa unduhan, nomor ganda ditolak); daftar deal dan timeline; cek tanda tangan buyer; penawaran (kode salin-tempel sementara); entri papan dengan kelas dan tag; surat dibaca dan PDF dicek sebelum segel; status advance. `src/lib/supplier-deal.ts` (murni, teruji).

## Hasil vs KPI (angka riil)
| KPI | Target | Aktual |
|---|---|---|
| Langkah salin-tempel | 0 | — |

## Status
**PARSIAL.** T1 – T4, T6 – T8 DONE. T5 PARSIAL: penawaran butuh relay (HNK-23). T9 PARSIAL: kartu entri sekarang menunggu kode permintaan entri dari financier (`7a0b911`); langkah pelunasan butuh `settled` lewat relay. AC 24.2 – 24.5 PASS; AC 24.1 (tanpa salin-tempel) menunggu relay.

## Risiko tersisa
- Key per invoice bergantung pada `invoice_pk(k)` dari buyer: supplier harus menerima key buyer sebelum membuat invoice (urutan SEQ-01 bagian 1 sudah disesuaikan).
- Skrip yang berjalan di tab saat store terbuka tetap bisa membaca dokumen (lihat [[Threat Model]]).

## Bukti
- Commit: `7a0b911` (jitsuinfi-frontend `7a0b911` (jitsuinfi-frontend PR #3, di-merge `7fe0118`)); `17a01ea` (jitsuinfi-frontend `17a01ea` (PR #2, di-merge `2180881`)); `a252568` (jitsuinfi-zcash `a252568` (jitsuinfi-zcash PR #8, di-merge `dbfc422`)); `c7d4b1b` (jitsuinfi-frontend `c7d4b1b` (jitsuinfi-frontend PR #1, di-merge `7fa4fae`))
- ID tes: U-HNK-24.1 – .5 PASS, I-HNK-24.2 – .4 PASS
- Persetujuan user untuk push/deploy: push + PR disetujui 2026-10-20 ("Gas"); [JitsuinFi/jitsuinfi-zcash#8](https://github.com/JitsuinFi/jitsuinfi-zcash/pull/8), [JitsuinFi/jitsuinfi-frontend#1](https://github.com/JitsuinFi/jitsuinfi-frontend/pull/1); di-merge 2026-10-20 setelah CI hijau (`dbfc422`, `7fa4fae`)
