---
tags: [flow, backlog]
status: DITETAPKAN
progress: 3/3 SELESAI
updated: 2026-10-20
---

# SEQ-03 - Financier-backlogs

**Diagram:** [[SEQ-03 - Financier]] · Rencana: [[FD-01 - Keputusan Usulan dan Gelombang Kerja]] · [[FD-02 - Penelusuran Business Flow ke Backlog]] · Backlog: [[Backlog]]

Aturan sama dengan [[SEQ-00 - Autentikasi dan Onboarding-backlogs]]: merujuk task backlog DFD, menambah task khusus sequence `BL-S03-xx`.

Kolom Status mengikuti langkah 6 "Audit flow diagram" di [[Workflow Development]]: `TODO` → `DIKERJAKAN` → `AUDIT` (semua task backlog-nya DONE) → `SELESAI (tanggal, bukti)` atau `GAGAL AUDIT (tanggal, alasan)`; `DITUNDA` hanya dengan keputusan user. Antrean audit tampil di setiap `python3 scripts/sync-vault.py` (lewat `scripts/check-backlogs.py`). Backlog ini ditetapkan 2026-10-20 (D-32).

## Pemetaan per bagian

| Bagian | Langkah di sequence | Task |
|---|---|---|
| Masuk | Passkey konsol, sesi dari assertion | BL-D21-15, BL-D21-16, BL-D21-17 |
| 1. Terima penawaran | Penawaran lewat `/node/mail`, cek tanda tangan buyer, syarat | BL-D21-10, BL-D23-02 |
| 1. Terima penawaran | Tolak atau kedaluwarsa | BL-D23-03 |
| 1b. Komitmen dan surat | Salt library, kelas, alamat diversified | BL-D23-04, BL-D23-05, BL-D24-01 |
| 1b. Komitmen dan surat | Surat + PDF, kirim ke supplier dan buyer | BL-D24-02, BL-D24-03, BL-D23-06 |
| 2. Cek riwayat | Permintaan bertanda tangan, `check_buyer` di node, alasan tolak | BL-D26-01, BL-D26-05, BL-D26-06, BL-D26-07 |
| 2. Cek riwayat | Policy (allowlist, standar, tenggang) | BL-D26-08 |
| 3. Cek papan | `POST /node/deals`, lookup, status | BL-D23-07, BL-D23-08 |
| 3. Cek papan (`DoubleFinanced`) | `proof_from_lookup`, kartu bukti ganda | BL-D27-01, BL-D27-02, BL-D27-04 |
| 4. Tanda tangan supplier | Permintaan entri, `check_entry`, `EntryMismatch` | BL-D23-11 |
| 5. Posting dan konfirmasi | Pemulihan `register()`, persistensi, progres | BL-D23-12, BL-D23-13, BL-D23-14 |
| 6. Kumpulkan seal | `POST /node/deals/N/seals`, seal salah | BL-D24-07 |
| 7. Bayar advance | Persetujuan operator, konfirmasi ulang, `Done` setelah konfirmasi, s2 dan txid diteruskan | BL-D24-08, BL-D24-09, BL-D24-10, BL-D24-11 |
| 8. Penjadwal pelunasan | Penjadwal, status, sengketa, txid settled, P-12, bundel ke pihak | BL-D25-03 – BL-D25-08 |
| 9. Bundel | Kartu bundel di konsol | BL-D28-03 |
| Jalur financier B | Bukti `AlreadyFinanced` | Roadmap (P-14) |
| Varian manajer dana | Root dari Merkle sum tree | BL-D29-03 |

## Task khusus sequence

| ID | Bagian | Task | Selesai bila | Ref | Task backlog | Owner | Status |
|---|---|---|---|---|---|---|---|
| BL-S03-01 | Semua | Pipeline deal di konsol (daftar deal per state `Flow`) dan detail deal (papan, entri, surat, advance, pelunasan) dengan tombol aksi per state | Operator menjalankan satu deal dari penawaran sampai settled hanya dari konsol | C-33, HNK-05.T4 | HNK-26.T16 | Hans | SELESAI (2026-10-22, audit: `Pipeline` konsol (`src/console/Home.tsx:1016-1100`); E2E lokal testnet `TES-INV-FE-36210`: operator hanya memakai konsol: terima penawaran, jalankan langkah, setujui advance dengan passkey (`14ea447c…51cb`), sampai settled (`85d12ce6…d030`); tidak ada CLI financier) |
| BL-S03-02 | Semua | Daftar endpoint API node (`/node/mail`, `/node/deals`, `/node/deals/N/commitment`, `/node/history/check`, `/node/deals/N/seals`, `/node/pairing`, `/node/session`) dengan format request dan response | Daftar ada di repo dan cocok dengan implementasi HNK-05.T3 | HNK-05.T3 | HNK-05.T3 | Hans | SELESAI (audit 2026-10-22: README jitsuinfi-node bagian "API", 25 rute dicocokkan satu per satu dengan router `src/main.rs`; nama rute berbeda dari rencana, semuanya di bawah `/node/console/` kecuali `info`, `board`, `mail`. PR #33 `2236a2a`) |
| BL-S03-03 | Semua | E2E peran financier di testnet lewat konsol: penawaran sampai settled, satu kasus `AlreadyFinanced`, satu `DoubleFinanced` | Tiga kasus lulus di HNK-17 | HNK-17 | HNK-17.T4 | Hans | SELESAI (2026-10-25, E2E production testnet): selain siklus settled, `TES-INV-DBL-24689` berhenti `DoubleFinanced` (entri production `a2f46ffd…3659`, entri financier kedua `a42152b0…9188`) dan `TES-INV-ALR-71337` berhenti `AlreadyFinanced` (entri lebih dulu `25a78d45…75b5`) di konsol; financier kedua = jitsuin-node lokal di papan publik |

## Roadmap

- Jeda acak sebelum `Pay` (menunggu TM #12 / #15).
