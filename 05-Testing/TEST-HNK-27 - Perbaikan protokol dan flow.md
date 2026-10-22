---
tags: [test, "HNK-27"]
type: test
id: HNK-27
phase: F3
unit: PASS
integrasi: TODO
e2e: TODO
updated: 2026-10-20
---

# TEST-HNK-27 - Perbaikan protokol dan flow

> **Peta link:** [[Testing Hub]] · [[Backlog]] · [[AC-HNK-27 - Perbaikan protokol dan flow|AC]] · **Test** · [[ES-HNK-27 - Perbaikan protokol dan flow|Exec Summary]]

## 1. Unit
Logika murni, cepat, tanpa DB dan tanpa chain. Semua dijalankan lewat `bash scripts/check.sh` (fmt, check, clippy `-D warnings`, test, build wasm, secret scan): **All checks passed** 2026-10-20 di commit `9826b09`.

| ID | Kasus | Hasil | Tanggal | Bukti |
|---|---|---|---|---|
| U-HNK-27.1 | Komitmen deterministik saat retry; financier atau invoice lain memberi komitmen lain; vector salt | PASS | 2026-10-20 | `entry::tests::commitment_salt_*`, wasm `financier_commitment_is_derived_and_matches_the_supplier_entry`; vector `caaf1dce…7d23` = Python `hashlib.blake2b(key, person)` |
| U-HNK-27.2 | Entri dengan kelas lain ditolak `EntryMismatch`; `deal_classes` sama dengan vector `index.rs`; kelas tak dikenal = deal tidak sah; wasm: kelas opsional, setengah atau salah ditolak | PASS | 2026-10-20 | `entry_classes_must_match_the_deal`, `deal_classes_come_from_face_advance_and_dates`, wasm `two_register_entries_…` |
| U-HNK-27.3 | `assignmentDecode` mengembalikan semua field; cocok/tidak dengan invoice | PASS | 2026-10-20 | wasm `assignment_decode_shows_what_is_sealed` |
| U-HNK-27.4 | `BoardChecked` di `Register`: tetap, `Stopped`, atau mengikuti entri sendiri yang sudah tertambang | PASS | 2026-10-20 | `a_board_check_right_before_posting_stops_or_follows` |
| U-HNK-27.5 | `sent_entry` menemukan entri yang sudah terkirim (N + komitmen), mengabaikan yang lain | PASS | 2026-10-20 | `finds_an_entry_already_sent` |
| U-HNK-27.6 | Konfirmasi dihitung ulang setelah entri ditambang ulang; `Done` hanya setelah advance tertambang; advance kedaluwarsa dibayar ulang sekali | PASS | 2026-10-20 | `a_re_mined_entry_is_counted_again`, `an_expired_advance_is_paid_again_once`, `happy_path_…`, `finds_an_advance_already_sent` |
| U-HNK-27.7 | Kuitansi dan seal sah untuk nominal lain dari advance yang disepakati ditolak | PASS | 2026-10-20 | `advance_and_last_seal_arrive_together` |
| U-HNK-27.8 | Bukti wasm dengan posisi lolos `verify_proof_on_board`; tanpa posisi gagal; urutan terbalik atau txid salah ditolak | PASS | 2026-10-20 | wasm `two_register_entries_for_two_financiers_make_a_verifiable_proof` |
| U-HNK-27.9 | Entri dari tag saja sama persis dengan entri dari sertifikat | PASS | 2026-10-20 | wasm `a_repaid_history_verifies_…` |
| U-HNK-27.10 | Secret byte dinolkan setelah dipakai (juga saat error dan panjang salah); di Node, `Uint8Array` pemanggil bernilai nol setelah `buyerKeysBytes` | PASS | 2026-10-20 | wasm `byte_secrets_are_zeroed_after_use`; skrip Node dengan binding wasm-bindgen 0.2.129 (scratchpad) |
| U-HNK-27.11 | `jitsuin fund`: parsing argumen, verdict tanpa root, teks dan JSON | PASS | 2026-10-20 | `fund::tests::*` |

## 2. Integrasi
Skrip vs DB/chain sungguhan. Semua artefak memakai prefix `TES-` (invoice, akun, label, order).

| ID | Skenario | Hasil | Tanggal | Bukti (txid/log) |
|---|---|---|---|---|
| I-HNK-27.1 | ≥ 5 deal berkelas di papan uji testnet; `jitsuin index` menampilkan kelas | PASS | 2026-10-22 | 5 entri `TES-INV-IDX-77306-0..4` (txid di jitsuinfi-zcash `examples/testnet/index-tes-inv-idx/entries.txt`, blok pertama `55933f17…`); `jitsuin index` papan live: 15 entri register, 12 invoice, kelas `31-60 days` 5 invoice, median diskon 3-5%, kelas diskon digabung `other: 5` karena masing-masing < 5 |
| I-HNK-27.2 | Crash setelah posting entri, restart, `register()` tidak memposting kedua kalinya | TODO | — | Butuh persistensi `Flow` (HNK-26.T10) untuk dijalankan ulang dari state tersimpan |
| I-HNK-27.3 | `jitsuin fund` atas akun operasional uji (HNK-15.T2) | TODO | — | Butuh UFVK dan `manager_pk` akun uji |

**Bukti pembersihan:** belum ada artefak off-chain baru (integrasi belum dijalankan).

## 3. E2E
Panduan langkah demi langkah untuk user.

- [ ] Jalankan `jitsuin index --ufvk <UFVK papan uji> --birthday <tinggi>` setelah ≥ 5 deal berkelas.
- [ ] Jalankan `jitsuin fund --ufvk <UFVK operasional> --manager-pk <hex> --birthday <tinggi>`.

| Langkah | Hasil diharapkan | Hasil aktual | Status |
|---|---|---|---|
| 1 | Kelas tenor dengan ≥ 5 invoice punya median diskon | — | TODO |
| 2 | Verdict SOLVENT / NOT SOLVENT / NO ROOT dengan batas uji | — | TODO |
