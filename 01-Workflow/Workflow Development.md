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

## Langkah 6: Audit flow diagram (ditambahkan 2026-10-20, D-32)

Permintaan user 2026-10-20: "tambahin workflow untuk audit jika backlog selesai, audit terhadap flow diagramnya dan berikan label selesai atau apapun itu di backlog diagram tersebut". Langkah ini berjalan setelah langkah 4 untuk setiap task yang dirujuk backlog diagram (`08-FlowDiagrams/*-backlogs.md`), dan sebelum langkah 5 (push tetap menunggu persetujuan user).

1. **Pemicu.** Semua task backlog (`HNK-xx.Tn`) yang dirujuk satu baris `BL-…` berstatus `DONE` di [[Backlog]]. `python3 scripts/sync-vault.py` menampilkan baris itu di **AUDIT QUEUE**. Ubah Status baris `BL-…` menjadi `AUDIT`.
2. **Audit terhadap diagram.** Buka elemen di kolom "Elemen" (proses dan aliran DFD-2.x, bagian SEQ, kotak PG-01) dan cocokkan dengan perilaku aktual:
   - aliran data: setiap aliran masuk dan keluar proses itu benar-benar ada di kode atau layar (sumber, tujuan, isi);
   - urutan: pesan dan state mengikuti sequence (termasuk jalur tolak dan error);
   - kriteria "Selesai bila" terbukti dengan bukti nyata (commit, ID tes, txid, tangkapan layar);
   - tidak ada kebocoran baru terhadap [[Threat Model]].
3. **Lulus.** Status baris menjadi `SELESAI (YYYY-MM-DD, bukti)`. Perbarui diagramnya:
   - DFD: status proses di `scripts/dfd_model.py` (`kind` usulan → ada, kolom Status di `ptable`), lalu `python3 scripts/build-dfd.py`;
   - SEQ: catatan kuning atau biru untuk langkah itu menjadi hijau (ADA);
   - PG-01: kotak `<<new>>` menjadi `<<have>>`;
   - FD-00 §6: temuan kode yang tertutup dihapus atau ditandai selesai.
   Lalu `python3 scripts/render-diagrams.py`.
4. **Gagal.** Status baris menjadi `GAGAL AUDIT (YYYY-MM-DD, alasan)`, task backlog dibuka lagi (status `PARSIAL`). Kalau yang salah justru diagramnya, ubah diagram dan catat sebagai `DEV-xx` di [[Backlog]] (keputusan user final).
5. **Tutup.** `python3 scripts/sync-vault.py`: AUDIT QUEUE, MISMATCH, UNKNOWN TASK, dan BAD STATUS = 0, Broken = 0, balancing DFD lulus. Frontmatter `progress:` tiap file `-backlogs` diperbarui otomatis. `python3 scripts/check-backlogs.py --strict` harus lulus sebelum minta izin push.

Label Status yang sah: `TODO`, `DIKERJAKAN`, `AUDIT`, `SELESAI (…)`, `GAGAL AUDIT (…)`, `DITUNDA` (hanya dengan keputusan user), `ATURAN` (baris aturan, tanpa task).

## Penerapan di proyek JitsuinFi

| Langkah | Di proyek ini | Tempat bukti |
|---|---|---|
| 1. Eksekusi | **DB** = skema app DB (kalau ada) dan inisialisasi wallet DB (`zcash_client_sqlite`). **Typecheck + build:** Rust `cargo check` + `cargo clippy -- -D warnings` + `cargo build`; TypeScript `npx tsc --noEmit` + `npm run build`. Lalu commit lokal | Hash commit di file ES |
| 2. Sinkronisasi dokumen | Isi status per kriteria di file AC (tanggal + bukti). Deviasi → file AC bagian Deviasi **dan** [[Backlog]] Log Deviasi. Perbarui [[Format Data]], [[Arsitektur JitsuinFi]], atau [[Threat Model]] bila terdampak | [[AC Hub]] |
| 3. Test tiga lapis | Unit: `cargo test` untuk logika murni (format invoice, nullifier, encoding memo). Integrasi: vs lightwalletd dan mainnet dengan artefak `TES-`. E2E: checklist untuk user | [[Testing Hub]] |
| 4. Exec summary | Satu file per item | [[Exec Summary Hub]] |
| 5. Commit & push | Commit lokal di langkah 1. **Push ke GitHub dan deploy ke Railway hanya setelah user setuju** | Baris "Persetujuan user" di file ES |
| 6. Audit flow diagram | Baris `BL-…` di file `-backlogs` diaudit terhadap diagramnya setelah semua task-nya DONE; label `SELESAI` / `GAGAL AUDIT`; diagram diperbarui (ADA) | Kolom Status di `08-FlowDiagrams/*-backlogs.md`, output `scripts/check-backlogs.py` |

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
5. Audit baris `BL-…` yang masuk AUDIT QUEUE terhadap flow diagramnya, beri label, perbarui diagram (langkah 6).
6. Minta persetujuan user → baru push/deploy (langkah 5).
7. Jalankan `sync-vault.py` → `Broken: 0`, antrean audit 0.
