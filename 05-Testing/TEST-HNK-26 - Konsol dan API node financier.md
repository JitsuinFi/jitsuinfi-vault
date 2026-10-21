---
tags: [test, "HNK-26"]
type: test
id: HNK-26
phase: F5
unit: TODO
integrasi: TODO
e2e: TODO
updated: 2026-10-20
---

# TEST-HNK-26 - Konsol dan API node financier

> **Peta link:** [[Testing Hub]] · [[Backlog]] · [[AC-HNK-26 - Konsol dan API node financier|AC]] · **Test** · [[ES-HNK-26 - Konsol dan API node financier|Exec Summary]]

## 1. Unit
Logika murni, cepat, tanpa DB dan tanpa chain.

| ID | Kasus | Hasil | Tanggal | Bukti |
|---|---|---|---|---|
| U-HNK-26.1 | Verifikasi assertion: challenge kedaluwarsa dan origin salah ditolak | PASS | 2026-10-21 | Challenge tak dikenal atau sudah dipakai 410 (tes node `sign_in_needs_a_paired_passkey_and_a_live_challenge`, uji replay browser); POST dari Origin asing 403 di produksi; origin di clientData dicek webauthn-rs. Jalur kedaluwarsa waktu (2 menit) belum punya tes sendiri |
| U-HNK-26.2 | Serialisasi `Flow` roundtrip | PASS | 2026-10-20 | `jitsuin-flow` tes `a_restored_snapshot_resumes_the_deal_in_every_state` (setiap state dari `Check` sampai `Done`, termasuk advance kedaluwarsa, `AlreadyFinanced`, `DoubleFinanced`, history tag; deal dilanjutkan dari flow hasil pemulihan, byte identik) dan `a_damaged_or_edited_snapshot_is_refused` (magic, versi, byte sisa, terpotong, `Pay` dengan satu segel, segel buyer rusak, entri financier lain) (`23be34a`) |
| U-HNK-26.3 | Penjadwal tidak memposting ulang txid tersimpan | TODO | — | — |
| U-HNK-26.4 | `Flow::double_sign_proof` | PASS | 2026-10-20 | `jitsuin-flow` tes `a_double_financed_deal_gives_a_proof_that_holds_on_the_board` (bukti di `Stopped(DoubleFinanced)`: entri pertama dan konflik dengan posisi, lolos `verify_proof_on_board`, roundtrip byte, tanda tangan buyer rusak ditolak, tanpa bukti sebelum berhenti) dan `already_financed_gives_no_proof` (`0ee55c6`) |
| U-HNK-26.5 | File bukti pelunasan `Evidence` | PASS | 2026-10-20 | `jitsuin-flow` tes `evidence_recomputes_the_status_from_signed_contents` (buyer klaim 50.000 kirim 1.000 + receipt palsu: `Disputed` setelah tenggang, `Claimed` di dalam tenggang, `Overdue` tanpa klaim; roundtrip byte) dan `edited_evidence_is_refused` (klaim kunci lain, receipt invoice lain, receipt advance, nominal receipt diubah tidak dihitung, magic, versi, byte sisa, terpotong) (`2fd155e`) |

## 2. Integrasi
Skrip vs DB/chain sungguhan. Semua artefak memakai prefix `TES-` (invoice, akun, label, order).

| ID | Skenario | Hasil | Tanggal | Bukti (txid/log) |
|---|---|---|---|---|
| I-HNK-26.1 | Deal testnet lewat API dan konsol | TODO | — | — |
| I-HNK-26.2 | Restart node di state `AwaitConfirmation` | TODO | — | — |
| I-HNK-26.3 | Kasus `AlreadyFinanced` dan `DoubleFinanced` | TODO | — | — |

**Bukti pembersihan:** sisa artefak off-chain `TES-` = _TODO_ (target **0**). Artefak on-chain tidak bisa dihapus; catat txid-nya di tabel di atas. Data produksi tidak boleh tersentuh.

## 3. E2E
Panduan langkah demi langkah untuk user.

- [ ] Pairing passkey
- [ ] Terima penawaran
- [ ] Cek riwayat
- [ ] Posting entri
- [ ] Kumpulkan seal
- [ ] Setujui advance
- [ ] Settled otomatis

| Langkah | Hasil diharapkan | Hasil aktual | Status |
|---|---|---|---|
| 1 | _TODO_ | — | TODO |
