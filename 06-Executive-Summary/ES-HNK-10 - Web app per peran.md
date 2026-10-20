---
tags: [es, "HNK-10"]
type: es
id: HNK-10
phase: F5
lead: Hans
owners: [Hans, Dex]
status: PARSIAL
updated: 2026-10-18
---

# ES-HNK-10 - Web app per peran

> **Peta link:** [[Exec Summary Hub]] · [[Backlog]] · [[AC-HNK-10 - Web app per peran|AC]] · [[TEST-HNK-10 - Web app per peran|Test]] · **Exec Summary**

**Lead:** Hans #hans · **Tim:** Hans #hans, Dex #dex 

## Apa diubah
- Repo lokal `jitsuinfi-frontend` (`cdcba0d`, `98466b2`, tanpa remote, D-25): Vite + TypeScript tanpa framework dan tanpa CDN, CSP ketat, token desain terang/gelap.
- Layar supplier, buyer (passkey PRF), financier, Verify (termasuk tampilan "Caught"), dan halaman orang luar; semua kriptografi lewat `jitsuin-wasm` di browser.
- Uji klik alur penuh di build produksi: lulus; 0 request ke domain lain.

_Dikerjakan Hans (agent) atas keputusan user D-25 / DEV-11; review oleh Hans (Dave tidak lagi memegang task, D-35)._

## Hasil vs KPI (angka riil)
| KPI | Target | Aktual |
|---|---|---|
| Request pihak ketiga | 0 | — |
| Waktu muat halaman | dicatat | — |

## Status
**PARSIAL**.

## Risiko tersisa
- Aksi backend (registrasi, advance, watchdog) belum terhubung ke layar: menunggu API HNK-05.T3/HNK-10.T4 (Dex).
- Header CSP di server dan deploy (HNK-10.T5, Dex) belum; repo belum di-push (D-25).
- Halaman indeks (HNK-08.T3) dan halaman anggota dana (HNK-15.T3) belum.

## Bukti
- Commit: lihat Apa diubah (lokal)
- ID tes: _TODO_
- Persetujuan user untuk push/deploy: _belum_
