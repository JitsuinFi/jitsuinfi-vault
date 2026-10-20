---
tags: [test, "HNK-28"]
type: test
id: HNK-28
phase: F4
unit: PASS
integrasi: PARSIAL
e2e: TODO
updated: 2026-10-20
---

# TEST-HNK-28 - Verifikasi publik lengkap

> **Peta link:** [[Testing Hub]] · [[Backlog]] · [[AC-HNK-28 - Verifikasi publik lengkap|AC]] · **Test** · [[ES-HNK-28 - Verifikasi publik lengkap|Exec Summary]]

## 1. Unit
Logika murni, cepat, tanpa DB dan tanpa chain.

| ID | Kasus | Hasil | Tanggal | Bukti |
|---|---|---|---|---|
| U-HNK-28.1 | `verifyProofOnBoard` menolak posisi palsu | PASS | 2026-10-20 | `jitsuin-wasm` tes `proofs_and_the_rate_index_are_checked_against_board_data_as_in_the_cli`: posisi di papan, entri kedua hilang, tanpa posisi pertama, posisi geser, tanda tangan palsu (`32a3977`) |
| U-HNK-28.2 | `rateIndex` sama dengan `rate_index` | PASS | 2026-10-20 | Tes yang sama: k = 1, 5, 9 sama persis dengan `rate_index_json` (`32a3977`) |

## 2. Integrasi
Skrip vs DB/chain sungguhan. Semua artefak memakai prefix `TES-` (invoice, akun, label, order).

| ID | Skenario | Hasil | Tanggal | Bukti (txid/log) |
|---|---|---|---|---|
| I-HNK-28.1 | Snapshot relay dibandingkan dengan `jitsuin verify --save-board` | TODO | — | Menunggu snapshot otomatis (P-06) |
| I-HNK-28.2 | Web vs CLI pada data TES- yang sama (invoice `TES-INV-P28`, dua entri, snapshot JSON): `verifyProofOnBoard` dan `jitsuin verify --board` memberi verdict dan hasil per klaim yang sama untuk bukti lengkap (PROVEN), papan tanpa entri kedua (DOES NOT HOLD), dan bukti tanpa posisi pertama (DOES NOT HOLD); `rateIndex` sama dengan `jitsuin index --json` tanpa `version` dan `board`. Layar Verify di browser menampilkan verdict yang sama dan label "claimed, not checked" tanpa data papan | PASS | 2026-10-20 | File uji di scratchpad sesi, tidak di repo |

**Bukti pembersihan:** sisa artefak off-chain `TES-` = _TODO_ (target **0**). Artefak on-chain tidak bisa dihapus; catat txid-nya di tabel di atas. Data produksi tidak boleh tersentuh.

## 3. E2E
Panduan langkah demi langkah untuk user.

- [ ] Buka Verify, tempel bundel contoh
- [ ] Buka halaman indeks
- [ ] Buka halaman orang luar

| Langkah | Hasil diharapkan | Hasil aktual | Status |
|---|---|---|---|
| 1 | _TODO_ | — | TODO |
