---
tags: [fe-tool, "FE-06"]
type: fe-tool
id: FE-06
layer: deploy
status: AKTIF
updated: 2026-10-20
---

# FE-06 - Vercel Deploy dan CI

> **Peta link:** [[FE-00 - Peta Tools FE|Peta tools]] · [[10 - FE Vault|Hub modul]] · [[FE-01 - Batasan Platform FE|Batasan platform]]

Hosting dan satu-satunya CI frontend.

## Akar
| | |
|---|---|
| Proyek | Vercel `jitsuinfi` (tim `shenhan01-sys-projects`), Node 24.x; tertaut lewat `jitsuinfi-frontend/.vercel/project.json` |
| Domain produksi | `jitsuinfi.vercel.app` (juga `PRODUCTION_RP_ID` passkey) |
| Konfigurasi | `vercel.json`: `framework vite`, `buildCommand npm run build`, `outputDirectory dist`, header CSP dan keamanan, cache `immutable` untuk `/assets/*` |
| Pemicu | Push ke branch apa pun = preview deployment; merge ke `main` = produksi |
| GitHub Actions | Tidak ada di repo frontend |

## CI yang terlihat di PR
| Check | Arti |
|---|---|
| `Vercel` | Build dan preview deployment branch PR |
| `Vercel Preview Comments` | Integrasi komentar preview |

Tidak ada tes otomatis di CI: `npm test` dan `tsc` dijalankan lokal sebelum push.

## Aturan
- Merge PR frontend = deploy produksi, jadi hanya setelah user setuju dan (untuk perubahan login) setelah uji lokal.
- Org GitHub `JitsuinFi` paket Free + repo privat: auto-merge tidak tersedia, merge manual.
- Passkey di preview deployment berbeda dari produksi (`rp.id` per host, `vercel.app` ada di Public Suffix List).

## Cek cepat
```bash
gh pr checks <nomor> --repo JitsuinFi/jitsuinfi-frontend
```

## Status
AKTIF. Usulan tambahan (belum ada): menjalankan `npm test` di CI.
