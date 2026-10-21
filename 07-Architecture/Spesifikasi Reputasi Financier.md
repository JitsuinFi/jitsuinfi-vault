---
tags: [spec, "HNK-30.T21", "D-47"]
type: spec
status: USULAN
updated: 2026-10-21
---

# Spesifikasi Reputasi Financier

> **Peta link:** [[Decision Log]] (D-47) · [[Backlog]] (HNK-30.T21) · [[Threat Model]] · [[Format Data]] · [[SEQ-03 - Financier]]

Tujuan: supplier bisa melihat bahwa financier di direktori (D-47) sudah benar-benar membiayai dan menagih deal sampai lunas, **tanpa** ada yang tahu deal mana miliknya, berapa nominalnya, atau kapan persisnya.

## Kenapa tidak bisa dihitung dari papan
- Entri register membawa `financier_commitment = BLAKE2b(financier_pk ‖ salt)` dengan salt baru per invoice (P-08). Pemegang UFVK publik tidak bisa menautkan dua entri ke financier yang sama. Ini disengaja: kalau bisa, volume dan portofolio financier bocor.
- Statistik yang diisi financier sendiri tidak bisa diverifikasi.
- Jadi reputasi harus **dibuktikan oleh financier**, yang memegang semua `salt` (dari `commitment_opening(key, N)`) dan N deal-nya.

## Klaim yang dibuktikan
"Pemilik key financier P punya **k** entri register di papan dalam periode [t0, t1], semua N berbeda, dan setiap N punya entri `settled` dengan flag tepat waktu." Opsional: berapa yang lewat tempo.

## Opsi A: atestasi penyedia (bisa dibangun sebelum deadline, ±1 hari)
1. Financier (konsol node) mengirim `financier.reputation_request` tersegel ke penyedia: daftar `(N, salt)` miliknya untuk periode itu.
2. Penyedia memeriksa di papan: setiap `BLAKE2b(P ‖ salt)` cocok dengan commitment entri register untuk N itu, dan `settled_tag(N)` ada dengan flag tepat waktu.
3. Penyedia menandatangani `{P, periode, kelas_jumlah, kelas_tepat_waktu}` dan memasukkannya ke listing direktori (`reputation`). App supplier memverifikasi dengan tanda tangan direktori yang sudah ada.
4. **Yang dipublikasikan hanya kelas, bukan angka persis:** jumlah `1–4`, `5–19`, `20+`; tepat waktu `≥ 95 %`, `80–95 %`, `< 80 %`. Diperbarui per bulan. Angka persis plus pembaruan sering membuka waktu tiap deal lewat selisihnya.
- **Kebocoran:** penyedia mengetahui deal milik financier. Dalam model node terkelola (D-43) penyedia sudah menjalankan node financier, jadi tidak ada pihak baru yang tahu.
- **Kepercayaan:** supplier harus memercayai penyedia sebagai pengatestasi. Siapa pun yang memegang `(N, salt)` bisa memeriksa ulang atestasi yang sama, jadi auditor bisa diberi akses yang sama.

## Opsi B: bukti zkSNARK (v2, 1–3 minggu, setelah deadline)
- Sistem bukti Halo 2 (tanpa trusted setup, sama dengan Zcash).
- **Butuh perubahan format untuk deal baru:** commitment v2 = Poseidon(P_pallas, salt) dengan key reputasi di kurva Pallas (BLAKE2b dan Ed25519 di dalam sirkuit terlalu mahal). Deal lama tidak ikut.
- **Butuh root papan:** pohon Merkle atas entri register per epoch, root dipublikasikan penyedia dan dijangkarkan di memo papan.
- Input publik: root, k, P_pallas, rentang epoch. Witness: k daun + jalur, salt, pasangan settled. Keluaran: bukti π yang diverifikasi di browser (wasm) saat app supplier mengurutkan direktori.
- **Risiko:** bug soundness sirkuit tidak terlihat (bukti palsu lolos); prover di browser bisa makan detik sampai menit; butuh review.

## Usulan
Bangun **Opsi A** sekarang (ke direktori sebagai `reputation`, kelas saja), tulis Opsi B sebagai v2. Keputusan user dibutuhkan; dicatat di [[Decision Log]] bila dipilih.
