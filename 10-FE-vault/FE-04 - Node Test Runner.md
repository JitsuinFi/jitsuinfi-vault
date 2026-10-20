---
tags: [fe-tool, "FE-04"]
type: fe-tool
id: FE-04
layer: test
status: AKTIF
updated: 2026-10-20
---

# FE-04 - Node Test Runner

> **Peta link:** [[FE-00 - Peta Tools FE|Peta tools]] · [[10 - FE Vault|Hub modul]] · [[FE-01 - Batasan Platform FE|Batasan platform]]

Tes unit frontend tanpa dependensi tambahan: `node --test` langsung pada file `.ts`.

## Akar
| | |
|---|---|
| Runtime | Node v26.11.1 (dicek 2026-10-20; bawaan `node:test`, `node:assert/strict`) |
| Cara jalan | Type stripping bawaan Node: file `.ts` dijalankan tanpa kompilasi |
| Script | `npm test` = `node --test tests/store.test.ts tests/supplier-deal.test.ts` (+ `tests/account.test.ts` di PR #4) |

## Aturan karena type stripping
- Tidak boleh *parameter properties* di constructor (`constructor(private x: T)`); tulis field eksplisit.
- Import antar modul yang dites harus memakai ekstensi `.ts` bila berupa import nilai.
- Modul yang dites tidak boleh mengimpor wasm atau DOM; dependensi disuntikkan (contoh `Account` di `src/lib/session.ts` menerima `KeySource`).

## Isi tes sekarang
| File | Isi |
|---|---|
| `tests/store.test.ts` | Store IndexedDB terenkripsi (HNK-24.T3) |
| `tests/supplier-deal.test.ts` | Timeline deal, kode penawaran, kode permintaan entri (HNK-24) |
| `tests/account.test.ts` (PR #4) | Salt, profil, `rp.id`, sidik jari, sesi dan stempel dengan authenticator palsu (HNK-22) |

## Cek cepat
```bash
npm --prefix /Users/Shenhan/HansProject/zkSNARK/jitsuinfi-frontend test
```

## Status
AKTIF.
