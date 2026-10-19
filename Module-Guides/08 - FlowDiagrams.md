---
tags: [module, "08"]
---

# 08 - FlowDiagrams

**Tujuan:** Gambaran end to end bagaimana JitsuinFi seharusnya berjalan: auth, alur tiap peran, dan aliran data per fitur. Dibuat 2026-10-19 karena halaman internal web app masih simulasi (salin-tempel, tanpa login, tanpa peran). Setiap diagram menandai mana yang **ADA** di kode dan mana yang **USULAN**.

Kembali: [[START-HERE]]

## Mulai di sini
- [[08-FlowDiagrams/FD-00 - Arsitektur Target dan Legenda]]: legenda status, notasi, komponen target, dan 14 usulan (P-01 – P-14) yang perlu keputusan Hans.
- [[08-FlowDiagrams/PG-01 - Peta Halaman per Peran]]: halaman target per peran.

## Sequence diagram (satu peran satu sequence)
- [[08-FlowDiagrams/SEQ-00 - Autentikasi dan Onboarding]] (bersama: daftar, masuk, pilih peran, sesi, konsol node)
- [[08-FlowDiagrams/SEQ-01 - Supplier]]
- [[08-FlowDiagrams/SEQ-02 - Buyer]]
- [[08-FlowDiagrams/SEQ-03 - Financier]]
- [[08-FlowDiagrams/SEQ-04 - Verifier dan Orang Luar]]
- [[08-FlowDiagrams/SEQ-05 - Anggota Dana]]

## DFD
- Level 0: [[08-FlowDiagrams/DFD-0 - Diagram Konteks]]
- Level 1: [[08-FlowDiagrams/DFD-1 - Proses Utama]]
- Level 2:
  - [[08-FlowDiagrams/DFD-2.1 - Identitas dan Sesi]]
  - [[08-FlowDiagrams/DFD-2.2 - Penerbitan dan Tanda Tangan Invoice]]
  - [[08-FlowDiagrams/DFD-2.3 - Registrasi Papan]]
  - [[08-FlowDiagrams/DFD-2.4 - Pengalihan dan Advance]]
  - [[08-FlowDiagrams/DFD-2.5 - Pelunasan dan Settled]]
  - [[08-FlowDiagrams/DFD-2.6 - Riwayat Buyer]]
  - [[08-FlowDiagrams/DFD-2.7 - Deteksi Pembiayaan Ganda]]
  - [[08-FlowDiagrams/DFD-2.8 - Verifikasi dan Indeks Publik]]
  - [[08-FlowDiagrams/DFD-2.9 - Solvabilitas Dana]]

## Cara mengubah diagram
Sequence, DFD-0, dan PG-01: kode diagram adalah blok ` ```plantuml ` di dalam note itu (satu-satunya sumber). DFD-1 dan DFD-2.x dibuat dari `scripts/dfd_model.py` oleh `scripts/build-dfd.py`, jadi edit modelnya, bukan note-nya. Skrip itu juga menulis ulang kolom "Di level 1" di DFD-0 dan gagal bila level 0, 1, dan 2 tidak seimbang. Setelah mengedit, render ulang ke `08-FlowDiagrams/assets/*.svg`:

```bash
python3 scripts/build-dfd.py && python3 scripts/render-diagrams.py
```

Butuh `plantuml` (macOS: `brew install plantuml`). Style bersama: `08-FlowDiagrams/assets/dfd-style.iuml` (DFD, garis siku `linetype ortho`) dan `08-FlowDiagrams/assets/seq-style.iuml` (sequence).

## Konsep kunci
- Akun = passkey (WebAuthn PRF): satu passkey per orang, banyak key terisolasi per peran; tanpa email, password, atau akun di server (usulan P-01, P-02). Financier tidak mendaftar di web app: passkey-nya untuk konsol di origin node (P-05, P-11). Pemulihan passkey yang hilang belum diputuskan.
- Dokumen deal berpindah lewat kotak surat terenkripsi end-to-end; server tidak bisa membaca isinya tetapi menyimpan `mailbox_pk`, id turunan, ciphertext, dan melihat metadata (usulan P-04).
- Key financier dan spending key tinggal di node financier (usulan P-05; node sekarang PARSIAL). Advance hanya dibayar dari state `Pay` di `jitsuin-flow` (ADA); keluaran lain hanya posting papan (entri register dan `settled`, masing-masing 10 000 zat + fee).
- Protokol (N, entri papan, seal, Sign-to-Pay, settled, riwayat, bukti ganda) tidak berubah; lihat [[Format Data]].
