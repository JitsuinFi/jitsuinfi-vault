---
tags: [hub, spike]
---

# Spikes Hub

**Bagian dari:** [[02 - Spikes]] · Kembali: [[START-HERE]] · Terkait: [[Rencana Fase]] · [[Dashboard]] · [[Backlog]]

Spike = eksperimen singkat untuk membuktikan bahwa skenario, tools, dan resource **aman dipakai sebelum build**. Fase F0 di [[Rencana Fase]].

## Aturan
- Setiap spike punya owner, tujuan, hipotesis, langkah, kriteria lulus, dan fallback.
- Hasil ditulis dengan status `PASS` / `FAIL` / `BLOCKED` + tanggal + bukti (txid, log, screenshot path).
- **Spike kritis wajib PASS** (atau fallback disetujui user dan dicatat di [[Decision Log]]) sebelum F1/F2 dimulai.
- Artefak uji memakai prefix `TES-`. Seed dan key tidak pernah ditulis di vault.
- Spike baru: `python3 scripts/new-item.py --kind spike --id SPK-xx --title "..." --area "..."`.

## Daftar spike

| ID | Spike | Owner | Jam | Area | Kritis | Dipakai oleh |
|---|---|---|---|---|---|---|
| SPK-01 | [[SPK-01 - Toolchain Rust dan crate Zcash stabil\|Toolchain Rust dan crate Zcash stabil]] | Dex #dex | 2 | Tooling | Ya | HNK-01 – HNK-04 |
| SPK-02 | [[SPK-02 - Endpoint lightwalletd mainnet\|Endpoint lightwalletd mainnet]] | Dex #dex | 1 | Infra | Ya | HNK-03, HNK-04, HNK-09 |
| SPK-03 | [[SPK-03 - Kirim dan terima shielded dengan memo di mainnet\|Kirim dan terima shielded dengan memo di mainnet]] | Hans #hans | 3 | Zcash | Ya | HNK-03, HNK-05 – HNK-07 |
| SPK-04 | [[SPK-04 - Pembayaran Zodl lewat URI ZIP-321 dengan memo\|Pembayaran Zodl lewat URI ZIP-321 dengan memo]] | Hans #hans | 1 | Wallet | — | HNK-05, HNK-06, HNK-10 |
| SPK-05 | [[SPK-05 - Pemindaian watch-only dengan viewing key\|Pemindaian watch-only dengan viewing key]] | Hans #hans | 2 | Zcash | Ya | HNK-04, HNK-09, HNK-15 |
| SPK-06 | [[SPK-06 - Kripto inti Ed25519 hash dan layout memo\|Kripto inti Ed25519 hash dan layout memo]] | Hans #hans | 2 | Kripto | Ya | HNK-01, HNK-02, HNK-07 |
| SPK-07 | [[SPK-07 - Transaksi multi-output dan fee ZIP-317\|Transaksi multi-output dan fee ZIP-317]] | Hans #hans | 1 | Zcash | — | HNK-05, HNK-06, HNK-15 |
| SPK-08 | [[SPK-08 - Latensi konfirmasi dan urutan entri\|Latensi konfirmasi dan urutan entri]] | Hans #hans | 1 | Zcash | — | HNK-04, HNK-05, HNK-07 |
| SPK-09 | [[SPK-09 - Hosting Railway dan hardening web\|Hosting Railway dan hardening web]] | Dex #dex | 2 | Infra | — | HNK-10, HNK-14 |
| SPK-10 | [[SPK-10 - Dana mainnet dan keamanan seed\|Dana mainnet dan keamanan seed]] | Hans #hans | 1 | Resource | — | HNK-03 – HNK-07, HNK-13 |
| SPK-11 | [[SPK-11 - Distribusi verifier CLI di mesin bersih\|Distribusi verifier CLI di mesin bersih]] | Dex #dex | 1 | Tooling | — | HNK-09 |
| SPK-12 | [[SPK-12 - Kepastian aturan dan form ZECATHON\|Kepastian aturan dan form ZECATHON]] | Hans #hans | 1 | Aturan | — | HNK-14 |
| SPK-13 | [[SPK-13 - Dampak NU7 dan versi crate\|Dampak NU7 dan versi crate]] | Dex #dex | 1 | Zcash | — | Semua item |
| SPK-14 | [[SPK-14 - Repo baru lisensi dan originalitas\|Repo baru lisensi dan originalitas]] | Dex #dex | 1 | Aturan | — | Semua item |
| SPK-15 | [[SPK-15 - Tooling produksi video\|Tooling produksi video]] | Hans #hans | 1 | Video | — | HNK-14 |
| SPK-16 | [[SPK-16 - Block explorer untuk demo\|Block explorer untuk demo]] | Hans #hans | 1 | Resource | — | HNK-11, HNK-14 |
| SPK-17 | [[SPK-17 - Toolchain frontend dan aset offline\|Toolchain frontend dan aset offline]] | Hans #hans | 1 | Tooling | — | HNK-10, HNK-11, HNK-08 |
| SPK-18 | [[SPK-18 - Akses tim dan kesamaan environment\|Akses tim dan kesamaan environment]] | Dex #dex | 1 | Infra | — | Semua item |
| SPK-19 | [[SPK-19 - Testnet NU7 untuk development\|Testnet NU7 untuk development]] | Hans #hans | 2 | Zcash | — | HNK-03 – HNK-07 (opsional) |

## Bagian
- [[SPK-01 - Toolchain Rust dan crate Zcash stabil]] — Dex #dex
- [[SPK-02 - Endpoint lightwalletd mainnet]] — Dex #dex
- [[SPK-03 - Kirim dan terima shielded dengan memo di mainnet]] — Hans #hans
- [[SPK-04 - Pembayaran Zodl lewat URI ZIP-321 dengan memo]] — Hans #hans
- [[SPK-05 - Pemindaian watch-only dengan viewing key]] — Hans #hans
- [[SPK-06 - Kripto inti Ed25519 hash dan layout memo]] — Hans #hans
- [[SPK-07 - Transaksi multi-output dan fee ZIP-317]] — Hans #hans
- [[SPK-08 - Latensi konfirmasi dan urutan entri]] — Hans #hans
- [[SPK-09 - Hosting Railway dan hardening web]] — Dex #dex
- [[SPK-10 - Dana mainnet dan keamanan seed]] — Hans #hans
- [[SPK-11 - Distribusi verifier CLI di mesin bersih]] — Dex #dex
- [[SPK-12 - Kepastian aturan dan form ZECATHON]] — Hans #hans
- [[SPK-13 - Dampak NU7 dan versi crate]] — Dex #dex
- [[SPK-14 - Repo baru lisensi dan originalitas]] — Dex #dex
- [[SPK-15 - Tooling produksi video]] — Hans #hans
- [[SPK-16 - Block explorer untuk demo]] — Hans #hans
- [[SPK-17 - Toolchain frontend dan aset offline]] — Hans #hans
- [[SPK-18 - Akses tim dan kesamaan environment]] — Dex #dex
- [[SPK-19 - Testnet NU7 untuk development]] — Hans #hans

## Status (auto)
```dataview
TABLE WITHOUT ID file.link AS "Spike", owner AS "Owner", area AS "Area", status AS "Status", updated AS "Update"
FROM "02-Spikes"
WHERE type = "spike"
SORT id ASC
```
