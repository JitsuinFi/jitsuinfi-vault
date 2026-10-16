---
tags: [video, "VID-01"]
---

# VID-01 - Naskah 2 Menit

**Bagian dari:** [[Video-Workspace]] · Terkait: [[VID-02 - Storyboard dan Shot List]] · [[JitsuinFi - Ringkasan Proyek]]

> Draf. Total target 1:55 (sisakan 5 detik cadangan). Narasi bahasa Inggris (juri internasional); subtitle opsional.

| Waktu | Segmen | Layar | Narasi (draf) |
|---|---|---|---|
| 0:00–0:12 | Hook | Teks besar: "One invoice. Financed twice." | "Invoice fraud starts simple: a supplier sells the same invoice to two financiers." |
| 0:12–0:25 | Masalah | Diagram: registry terpusat vs chain publik | "Today you stop it with a central registry that sees every deal, or a public chain that shows who supplies whom. Both leak trade secrets." |
| 0:25–0:35 | Solusi | Logo JitsuinFi + tagline | "Zcash stops double-spending. JitsuinFi stops double-financing." |
| 0:35–0:55 | Demo 1: terbit dan daftar | Supplier membuat invoice, buyer menandatangani, financier A memeriksa papan dan mendaftar | "The buyer signs. The financier derives a nullifier, checks the shielded registry, and registers it." |
| 0:55–1:05 | Demo 2: tidak terlihat | Explorer menampilkan transaksi tanpa isi | "On-chain, nobody sees the invoice, the amount, or the parties." |
| 1:05–1:25 | Demo 3: momen kunci | Supplier mencoba ke financier B → tertangkap + bukti tanda tangan ganda | "Same invoice, second financier: caught instantly, with cryptographic proof the supplier signed twice." |
| 1:25–1:38 | Verifikasi juri | Terminal `jitsuin verify` atas txid mainnet + halaman indeks suku bunga | "Anyone can verify the registry, and see the public rate index: price public, participants private." |
| 1:38–1:50 | Kejujuran | Slide threat model singkat | "What leaks, what doesn't, and what's still trusted: it's all in our threat model." |
| 1:50–1:55 | Penutup | Tagline + URL repo dan demo | "JitsuinFi. Every invoice, sealed once." |

## Catatan
- Bagian demo dipercepat; tampilkan label "sped up" saat menunggu konfirmasi.
- Semua txid yang tampil harus nyata dan dicantumkan di README.
- Pakai data `TES-` yang terlihat realistis, bukan data pribadi siapa pun.
