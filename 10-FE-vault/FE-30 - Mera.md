---
tags: [fe-tool, "FE-30", monad-blitz]
type: fe-tool
id: FE-30
layer: library
status: REFERENSI
updated: 2026-10-23
---

# FE-30 - Mera

> **Peta link:** [[FE-00 - Peta Tools FE|Peta tools]] · [[10 - FE Vault|Hub modul]] · [[FE-01 - Batasan Platform FE|Batasan platform]]

Akun EVM dari passkey (PRF), signing session, `toViemAccount`.

## Akar
| | |
|---|---|
| Jenis | Library |
| Sumber | https://mera.category.xyz |
| Pasang | `npm i @category-labs/mera` |
| Bobot | Kecil |
| Lisensi | MIT OR Apache-2.0 |
| Lokasi | Belum dipasang di proyek ini |
| Asal catatan | Disalin dari vault Monad Blitz (`/Users/Shenhan/HansProject/MOnadBlitz/vault`), catatan FE-03 (2026-10-23) |
| Vonis di Monad Blitz | **DIPAKAI**; dipakai di: BLZ-08 |

## Kecocokan dengan JitsuinFi
- [[FE-01 - Batasan Platform FE|FE-01]]: JitsuinFi sudah punya alur passkey + PRF sendiri (HNK-22). Mera menarik untuk dibandingkan: derivasi BIP-32 dari PRF dan signing session yang di-`end()`.

## Catatan
Diuji di SPK-06 - Mera - derivasi akun dan signing session (vault Monad Blitz). Butuh HTTPS.

## Status
REFERENSI (untuk JitsuinFi).
