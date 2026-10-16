---
tags: [spike, "SPK-09"]
type: spike
id: SPK-09
area: Infra
owner: Dex
status: TODO
updated: 2026-10-16
---

# SPK-09 - Hosting Railway dan hardening web

> **Peta link:** [[Spikes Hub]] · [[Backlog]] · [[Rencana Fase]]

**Owner:** Dex #dex · **Area:** Infra · **Dipakai oleh:** HNK-10, HNK-14

## Tujuan
Pastikan backend dan frontend bisa di-deploy di Railway (paket berbayar user) dengan secrets aman, tanpa CDN pihak ketiga, dengan header CSP.

## Hipotesis
Railway cukup untuk demo; tidak perlu TEE.

## Langkah
1. Deploy hello-world backend Rust + frontend statis (setelah persetujuan user, karena deploy = push).
2. Set secrets lewat env Railway.
3. Cek header CSP dan cookie.
4. Cek DevTools Network: tidak ada request ke domain pihak ketiga.
5. Akses dari jaringan lain dalam keadaan logout.

## Kriteria lulus
- [ ] URL publik stabil.
- [ ] CSP aktif.
- [ ] 0 request pihak ketiga.
- [ ] Secrets tidak muncul di log.

## Fallback kalau gagal
- Frontend statis di Railway, backend lokal untuk video; dinyatakan di deskripsi "what is real vs mock".

## Hasil
| Status | Tanggal | Bukti | Catatan |
|---|---|---|---|
| TODO | 2026-10-16 | Railway CLI tidak terpasang. GitHub CLI login sebagai `Shenhan01-sys` (scope `repo`, `workflow`). | Butuh akses akun Railway user dan persetujuan deploy (deploy = push). Opsi: deploy lewat integrasi GitHub di dashboard Railway, atau install Railway CLI. |

## Catatan
Railway bukan TEE: operator dan host bisa membaca memori. Masukkan ke [[Threat Model]].
