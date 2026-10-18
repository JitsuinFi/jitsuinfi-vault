---
tags: [test, "HNK-11"]
type: test
id: HNK-11
phase: F5
lead: Dave
owners: [Dave, Hans]
unit: TODO
integrasi: TODO
e2e: TODO
updated: 2026-10-18
---

# TEST-HNK-11 - Threat model dan halaman orang luar

> **Peta link:** [[Testing Hub]] · [[Backlog]] · [[AC-HNK-11 - Threat model dan halaman orang luar|AC]] · **Test** · [[ES-HNK-11 - Threat model dan halaman orang luar|Exec Summary]]

**Lead:** Dave #dave · **Tim:** Dave #dave, Hans #hans

## 1. Unit
Logika murni, cepat, tanpa DB dan tanpa chain.

| ID | Kasus | Hasil | Tanggal | Bukti |
|---|---|---|---|---|
| U-HNK-11.1 | N/A — item ini logika murni atau dokumen; tidak menyentuh DB/chain (dicatat, bukan dilewati) | PASS | 2026-10-18 | `jitsuin-wasm` `outsiders_only_see_hashes` untuk pembaca entri |

## 2. Integrasi
Skrip vs DB/chain sungguhan. Semua artefak memakai prefix `TES-` (invoice, akun, label, order).

| ID | Skenario | Hasil | Tanggal | Bukti (txid/log) |
|---|---|---|---|---|
| I-HNK-11.1 | N/A — verifikasi manual: cocokkan threat model dengan perilaku aktual di explorer | PASS | 2026-10-18 | Semua tx uji testnet `transparent=false` (log `cycle-it`, `hist-it`, `fund-it`, `proof-it`); wallet watch-only papan hanya melihat hash; explorer `testnet.zcashexplorer.app` tertinggal chain (SPK-16), jadi pembanding memakai data lightwalletd |

**Bukti pembersihan:** sisa artefak off-chain `TES-` = **0** (dokumen). Artefak on-chain tidak bisa dihapus; catat txid-nya di tabel di atas. Data produksi tidak boleh tersentuh.

## 3. E2E
Panduan langkah demi langkah untuk user.

- [ ] Pembaca baru bisa menjawab "siapa melihat apa" hanya dari halaman ini.

| Langkah | Hasil diharapkan | Hasil aktual | Status |
|---|---|---|---|
| 1 | _TODO_ | — | TODO |
