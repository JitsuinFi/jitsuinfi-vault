---
tags: [es, "HNK-04"]
type: es
id: HNK-04
phase: F2
lead: Hans
owners: [Hans, Dex]
status: PARSIAL
updated: 2026-10-17
---

# ES-HNK-04 - Pemindai papan registry

> **Peta link:** [[Exec Summary Hub]] · [[Backlog]] · [[AC-HNK-04 - Pemindai papan registry|AC]] · [[TEST-HNK-04 - Pemindai papan registry|Test]] · **Exec Summary**

**Lead:** Hans #hans · **Tim:** Hans #hans, Dex #dex

## Apa diubah
- Crate `jitsuin-board`: `scan` (sync + enhance + list-tx wallet watch-only, urutan tx per blok dari `GetBlock` lightwalletd), `collect` (decode entri, tolak memo rusak, urut total), `lookup` (sudut pandang pemegang invoice: entri pertama dengan signature supplier valid menang, signature invalid diabaikan, commitment financier kedua = `DoubleFinanced`).
- Modul `lwd`: klien gRPC minimal via `reqwest` HTTP/2 + protobuf manual (tanpa protoc).
- 6 unit test lulus; `fmt`, `clippy -D warnings`, `build` hijau.

## Hasil vs KPI (angka riil)
| KPI | Target | Aktual |
|---|---|---|
| Waktu scan papan uji | dicatat (target < 2 menit) | 5,9 dtk (4 tx) |
| Entri invalid yang lolos | 0 | 0 |

## Status
**PARSIAL** (lihat Risiko tersisa).

## Risiko tersisa
- CLI `jitsuin board scan` (HNK-04.T3, Dex) dan script integrasi resmi (HNK-04.T4, Dex) belum.
- Derivasi N masih menunggu DEV-04; `lookup` menerima N dari pemanggil.
- Satu panggilan `GetBlock` per tinggi blok; untuk papan besar perlu cache.

## Bukti
- Commit: `ef55987` (lokal)
- ID tes: U-HNK-04.1–3, I-HNK-04.1; tx `b8a272a87ad9023f3a00a6ffb630e8a584ba0a279af624cda939426c75809970`
- Persetujuan user untuk push/deploy: _belum_
