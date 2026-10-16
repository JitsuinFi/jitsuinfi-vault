---
tags: [reference]
---

# Glossary

## Proyek dan keuangan
- **JitsuinFi** — nama proyek: pembiayaan invoice privat tanpa pembiayaan ganda. Lihat [[JitsuinFi - Ringkasan Proyek]].
- **JitsuinFi Vault** — versi gabungan (stretch): dana bersama yang membiayai invoice, dengan bukti solvabilitas.
- **Invoice factoring** — supplier menjual hak tagih invoice ke financier dengan diskon. Lihat [[Invoice Factoring]].
- **Recourse / non-recourse** — siapa yang menanggung kalau buyer gagal bayar: supplier (recourse) atau financier (non-recourse).
- **Reverse factoring** — program yang dipimpin buyer: supplier mencairkan invoice yang sudah disetujui buyer.
- **Pembiayaan ganda** — satu invoice dibiayakan ke lebih dari satu financier. Lihat [[Pembiayaan Ganda]].
- **Attestor** — pihak yang tanda tangannya mendefinisikan keunikan aset; untuk invoice: buyer. Lihat [[Attestor]].
- **Pengalihan (assignment)** — pemindahan hak tagih dari supplier ke financier, ditandatangani supplier dan buyer.
- **Indeks suku bunga publik** — agregat bucket diskon dan tenor yang dipublikasikan tanpa nominal dan tanpa pihak.

## Zcash
- **Nullifier** — nilai unik yang mencegah pemakaian ganda. Di JitsuinFi: `N = H(tanda tangan buyer)`. Lihat [[Nullifier]].
- **Papan registry** — alamat Zcash yang IVK-nya dipublikasikan; entri memo berisi nullifier invoice yang sudah dibiayai.
- **IVK / UIVK / FVK / UFVK** — viewing key: incoming (hanya uang masuk) vs full (uang masuk dan keluar); awalan U = unified. Lihat [[Viewing Key]].
- **ZIP-32** — derivasi key hierarkis; dipakai untuk akun terpisah per peran atau per periode.
- **ZIP-321** — format URI pembayaran (alamat, nominal, memo) untuk QR. Lihat [[ZIP-321]].
- **ZIP-317** — aturan fee per logical action.
- **Memo** — data terenkripsi 512 byte per output shielded. Lihat [[Memo Zcash]].
- **Ironwood** — pool shielded aktif sejak NU6.3. Lihat [[Ironwood]].
- **Zodl** — wallet mobile referensi (dulu Zashi).
- **lightwalletd / Zaino** — server indeks untuk light client.
- **PCZT** — partially created Zcash transaction; transaksi yang disusun beberapa pihak.
- **FROST** — tanda tangan threshold (misalnya 2-of-3); spesifikasi ZIP 312 masih Draft.
- **ZSA** — Zcash Shielded Assets; belum ada di mainnet.

## Workflow
- **AC** — acceptance criteria; sumber kebenaran lulus/tidak.
- **Spike** — eksperimen singkat untuk membuktikan tool atau asumsi aman dipakai.
- **TES-** — prefix artefak uji integrasi.
- **Exec summary** — ringkasan per item: apa diubah, KPI, status, risiko, bukti.

## Obsidian
- **Vault** — folder yang dibuka Obsidian; isinya `.md` + `.obsidian/`.
- **Wikilink** — `[[Nama]]`, membentuk garis di graph.
- **Dataview** — plugin query frontmatter/tag/folder untuk daftar otomatis.
- **MOC / Hub** — note indeks yang menautkan semua note dalam satu grup.

Lanjut: [[Conventions]] · [[Quick-Reference]]
