---
tags: [workflow]
---

# Workflow Development

**Bagian dari:** [[01 - Workflow]] · Kembali: [[START-HERE]] · Terkait: [[Rencana Fase]] · [[Backlog]]

## Aturan (verbatim dari user)

**5 langkah per item/fase — tidak boleh dilewati:**

1. **EKSEKUSI** — migrasi DB (bila ada) → kode → verifikasi `typecheck` + `build` hijau → **commit lokal**.
2. **SINKRONISASI DOKUMEN** — cek acceptance criteria vs hasil **aktual**: tandai `PASS/FAIL/BLOCKED` + tanggal + bukti; bila implementasi menyimpang dari keputusan, **perbaiki entri backlog secara eksplisit** (bukan diam-diam); perbarui dokumen terdampak (skema DB, catatan modul, tabel agregat di hub).
3. **TEST — tiga lapis**, dicatat di hub testing → satu file per item:
   - **Unit** — logika murni, cepat, tanpa DB.
   - **Integrasi** — skrip vs DB sungguhan; gunakan artefak ber-prefix tes (`TES-`) dan **wajib bersihkan** (bukti sisa = 0); data produksi tidak boleh tersentuh.
   - **E2E** — panduan langkah-demi-langkah untuk user (format checkbox + tabel hasil).
4. **EXECUTIVE SUMMARY per item** — satu file per item: Apa diubah · Hasil vs KPI (angka riil) · Status SELESAI/PARSIAL/BLOCKED · Risiko tersisa · Bukti commit/id tes.
5. **COMMIT & PUSH** — commit lokal setiap selesai langkah 1; **push (deploy) HANYA setelah user menyetujui** hasil langkah 2–4. Tanpa persetujuan = tetap lokal.

**Prinsip:**
- Urutan fase = urutan dependency; tiap fase punya gerbang verifikasi (AC) sendiri sebelum lanjut ke fase berikutnya.
- Migrasi DB dijalankan **sebelum** kode yang memakainya live.
- Kriteria lulus = sumber kebenaran di hub Acceptance Criteria, bukan perasaan "sudah jalan".
- Dokumen yang tumbuh per item (AC, testing, exec summary) wajib pola **Hub + satu file per item** + header peta link dua-arah antar artefak; ID stabil konsisten lintas dokumen.
- Setelah edit vault: jalankan script sync + cek link → target broken link 0.
- Deviasi dari rencana ditulis eksplisit di backlog — keputusan user final, tidak ada perubahan diam-diam.

## Penerapan di proyek JitsuinFi

| Langkah | Di proyek ini | Tempat bukti |
|---|---|---|
| 1. Eksekusi | **DB** = skema app DB (kalau ada) dan inisialisasi wallet DB (`zcash_client_sqlite`). **Typecheck + build:** Rust `cargo check` + `cargo clippy -- -D warnings` + `cargo build`; TypeScript `npx tsc --noEmit` + `npm run build`. Lalu commit lokal | Hash commit di file ES |
| 2. Sinkronisasi dokumen | Isi status per kriteria di file AC (tanggal + bukti). Deviasi → file AC bagian Deviasi **dan** [[Backlog]] Log Deviasi. Perbarui [[Format Data]], [[Arsitektur JitsuinFi]], atau [[Threat Model]] bila terdampak | [[AC Hub]] |
| 3. Test tiga lapis | Unit: `cargo test` untuk logika murni (format invoice, nullifier, encoding memo). Integrasi: vs lightwalletd dan mainnet dengan artefak `TES-`. E2E: checklist untuk user | [[Testing Hub]] |
| 4. Exec summary | Satu file per item | [[Exec Summary Hub]] |
| 5. Commit & push | Commit lokal di langkah 1. **Push ke GitHub dan deploy ke Railway hanya setelah user setuju** | Baris "Persetujuan user" di file ES |

### Adaptasi yang wajib diketahui
- **Artefak on-chain tidak bisa dihapus.** Aturan "wajib bersihkan, bukti sisa = 0" berlaku penuh untuk artefak **off-chain** (DB, file, akun lokal). Untuk transaksi mainnet: pakai akun/alamat khusus berlabel `TES-`, nominal sekecil mungkin, dan catat semua txid di file TEST. Dicatat eksplisit sebagai **DEV-01** di [[Backlog]].
- **"Data produksi"** = dana dan key milik user di luar akun `TES-`, serta papan registry produksi (kalau nanti dibedakan dari papan uji). Uji integrasi memakai papan uji terpisah dengan prefix `TES-`.
- **Pola Hub + satu file per item** dibuat otomatis: `python3 scripts/new-item.py --kind item --id HNK-xx --title "..." --phase Fx`.
- **Setelah edit vault:** `python3 scripts/sync-vault.py` → harus `Broken: 0`.

## Siklus satu item (ringkas)
1. Cek gerbang fase sebelumnya di [[Rencana Fase]] dan AC dependency sudah `PASS`.
2. Kerjakan langkah 1 → commit lokal.
3. Isi file AC (langkah 2) dan file TEST (langkah 3).
4. Tulis file ES (langkah 4).
5. Minta persetujuan user → baru push/deploy (langkah 5).
6. Jalankan `sync-vault.py` → `Broken: 0`.
