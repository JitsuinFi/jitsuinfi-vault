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
- Belum: semua layar supplier (T2, T4 – T9, Dave).

## Hasil vs KPI (angka riil)
| KPI | Target | Aktual |
|---|---|---|
| Langkah salin-tempel | 0 | — |

## Status
**PARSIAL.** T1 DONE. T3 PARSIAL: store selesai dan teruji di browser, tetapi belum ada layar yang menyimpan deal ke store (audit BL-D1-02, BL-D22-07, BL-D22-10 gagal karena itu).

## Risiko tersisa
- Key per invoice bergantung pada `invoice_pk(k)` dari buyer: supplier harus menerima key buyer sebelum membuat invoice (urutan SEQ-01 bagian 1 sudah disesuaikan).
- Skrip yang berjalan di tab saat store terbuka tetap bisa membaca dokumen (lihat [[Threat Model]]).

## Bukti
- Commit: `a252568` (jitsuinfi-zcash `a252568` (jitsuinfi-zcash PR #8, di-merge `dbfc422`)); `c7d4b1b` (jitsuinfi-frontend `c7d4b1b` (jitsuinfi-frontend PR #1, di-merge `7fa4fae`))
- ID tes: U-HNK-24.1 PASS, U-HNK-24.3 PASS, I-HNK-24.2 PASS
- Persetujuan user untuk push/deploy: push + PR disetujui 2026-10-20 ("Gas"); [JitsuinFi/jitsuinfi-zcash#8](https://github.com/JitsuinFi/jitsuinfi-zcash/pull/8), [JitsuinFi/jitsuinfi-frontend#1](https://github.com/JitsuinFi/jitsuinfi-frontend/pull/1); di-merge 2026-10-20 setelah CI hijau (`dbfc422`, `7fa4fae`)
