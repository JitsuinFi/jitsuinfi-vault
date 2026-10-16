---
tags: [spike, "SPK-10"]
type: spike
id: SPK-10
area: Resource
owner: Hans
status: TODO
updated: 2026-10-16
---

# SPK-10 - Dana mainnet dan keamanan seed

> **Peta link:** [[Spikes Hub]] · [[Backlog]] · [[Rencana Fase]]

**Owner:** Hans #hans · **Area:** Resource · **Dipakai oleh:** HNK-03 – HNK-07, HNK-13

## Tujuan
Siapkan ZEC kecil untuk uji dan demo dengan pengelolaan seed yang aman.

## Hipotesis
0,02–0,05 ZEC cukup untuk semua uji dan demo.

## Langkah
1. Hitung anggaran: jumlah transaksi uji × fee + nominal demo.
2. User sendiri yang membeli atau menerima ZEC ke wallet miliknya.
3. Buat wallet `TES-` terpisah dan danai dari wallet user.
4. Simpan seed offline; tambahkan `.gitignore` dan secret scanning (gitleaks) di repo.

## Kriteria lulus
- [ ] Anggaran tercatat.
- [ ] Wallet `TES-` terdanai.
- [ ] Scan secret di repo bersih (0 temuan).

## Fallback kalau gagal
- Kurangi jumlah transaksi uji; gabungkan skenario.

## Hasil
| Status | Tanggal | Bukti | Catatan |
|---|---|---|---|
| TODO | 2026-10-16 | Estimasi anggaran: sekitar 40 transaksi uji dan demo × 0,0001 ZEC fee = 0,004 ZEC, ditambah saldo putar antar wallet `TES-` sekitar 0,01–0,02 ZEC → total sekitar 0,02–0,03 ZEC. | User sendiri yang membeli/menerima ZEC. Seed disimpan offline; tidak pernah ditulis di repo atau vault. |

## Catatan
Seed dan spending key tidak pernah ditulis ke repo, log, atau vault ini.
