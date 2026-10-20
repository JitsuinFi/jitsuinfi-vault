---
tags: [ac, "HNK-30"]
type: ac
id: HNK-30
phase: F6
status: TODO
updated: 2026-10-21
---

# AC-HNK-30 - Demo juri dan narasi dari judging

> **Peta link:** [[AC Hub]] · [[Backlog]] · **AC** · [[TEST-HNK-30 - Demo juri dan narasi dari judging|Test]] · [[ES-HNK-30 - Demo juri dan narasi dari judging|Exec Summary]]

**Item:** HNK-30 · **Fase:** F6 · **Dependency:** HNK-07, HNK-09, HNK-28 · **Keputusan:** D-39, D-40, D-41 · **Sumber:** [[JDG-10 - Putaran 2 Narasi Deep Swarm]], [[JDG-05 - Register Titik Lemah]]

## Deskripsi
Adopsi hasil judging (D-40): demo tempat juri sendiri mencoba double-finance invoice di papan testnet hidup dan pulang membawa bukti, ditambah perbaikan privasi dan teks yang diminta JDG-10. Mekanik tanpa ekonomi GameFi: M-02 kit invoice tersegel, M-01 dua pintu keluar, M-03 Exhibit A, M-04 lensa "yang dilihat dunia", M-07 Case File #0417 untuk video. Narasi dan urutan video ada di [[Decision Log]] D-40.

## Acceptance criteria
Status per kriteria: `TODO` / `PASS` / `FAIL` / `BLOCKED`, wajib dengan tanggal dan bukti (commit, txid, log, id tes).

| ID | Kriteria | Status | Tanggal | Bukti |
|---|---|---|---|---|
| AC-HNK-30.1 | Fuzz kanonikalisasi invoice (≥ 10.000 mutasi field, spasi, urutan, encoding, huruf): setiap mutasi berakhir di 偽 (tanda tangan buyer tidak valid) atau 重 (N sama); nol mutasi menghasilkan N baru yang valid (W-16) | TODO | — | — |
| AC-HNK-30.2 | Kit invoice tersegel (M-02): satu tautan membuka invoice testnet yang sudah ditandatangani dan dua meja financier, tanpa connect wallet, tanpa telemetri | TODO | — | — |
| AC-HNK-30.3 | Dua pintu keluar (M-01): cek N memukul papan testnet hidup lewat UFVK publik (bukan fixture lokal); panel satu baris "yang tidak dicegah" (N-13) tampil | TODO | — | — |
| AC-HNK-30.4 | Exhibit A (M-03): bukti tanda tangan ganda berisi hanya dua tanda tangan supplier atas N dan rujukan papan (tanpa nominal, buyer, identitas financier pertama); PASS di `/verify` dan `jitsuin verify` | TODO | — | — |
| AC-HNK-30.5 | Lensa "yang dilihat dunia" (M-04) menampilkan dengan jujur semua yang terbaca lewat UFVK publik (N, ciphertext, tinggi blok, nilai tx papan, tata letak memo, waktu) | TODO | — | — |
| AC-HNK-30.6 | W-14 opsi (b): kelas diskon dan tenor di entri papan tidak terbaca pemegang UFVK publik (terenkripsi ke financier), indeks publik hanya dari agregat k ≥ 5; bila (b) tidak selesai sebelum 26 Okt, opsi (a): dampak W-14 diungkap di [[Threat Model]] dan spesifikasi (D-41) | TODO | — | — |
| AC-HNK-30.7 | Teks: semua materi memakai N-06 (W-15), label jaringan resmi (W-17), kalimat batas N-13; N-07 dipakai hanya setelah fakta Ironwood dicek dengan sumber | TODO | — | — |
| AC-HNK-30.8 | Demo tahan outage host (W-23): `/verify` dan alur emas berjalan dari snapshot statis papan bila relay atau node tidak bisa dijangkau | TODO | — | — |
| AC-HNK-30.9 | Klip M-01 + M-03 ≤ 20 detik yang bisa dipahami tanpa sisa video; fixture Case File #0417 tanpa nama atau data perusahaan nyata (M-07) | TODO | — | — |

## Deviasi
_Kosong._ Kalau implementasi menyimpang dari keputusan, tulis di sini **dan** di [[Backlog]] bagian Log Deviasi. Tidak ada perubahan diam-diam.
