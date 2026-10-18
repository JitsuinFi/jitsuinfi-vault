---
tags: [architecture, security]
---

# Mode Confidential

**Bagian dari:** [[07 - Architecture]] · Kembali: [[START-HERE]] · Terkait: [[Threat Model]] · [[Desain Jitsuin Seal]] · [[AC-HNK-06 - Pengalihan hak tagih dan pelunasan|AC-HNK-06]]

> HNK-06.T6 (2026-10-18). Opsi, **bukan** alur default.

## Apa itu
Dalam factoring biasa (*notified*), buyer diberi tahu bahwa piutangnya sudah dialihkan dan membayar langsung ke financier. Di JitsuinFi ini adalah alur default: buyer menyegel surat pengalihan dan membayar ke alamat financier.

Dalam **mode confidential** (*undisclosed factoring*), buyer tidak diberi tahu. Buyer tetap membayar ke supplier seperti biasa, lalu supplier meneruskan pembayaran itu ke financier. Supplier memilih mode ini kalau tidak mau buyer tahu bahwa ia membiayakan invoice-nya.

## Bedanya dengan alur default

| Langkah | Default (notified) | Confidential |
|---|---|---|
| Surat pengalihan | Disegel Supplier → Buyer → Financier | Disegel Supplier → Financier saja; buyer tidak menerima surat |
| Advance (Sign-to-Pay) | Setelah seal Supplier dan Buyer | Setelah seal Supplier; financier menerima risiko tanpa pengakuan buyer |
| Pelunasan | Buyer membayar ke financier dengan kuitansi + klaim | Buyer membayar ke supplier; supplier meneruskan ke financier dengan kuitansi bertanda tangan supplier |
| Entri `settled` | Ditandatangani buyer dan financier | Ditandatangani supplier dan financier (buyer tidak tahu ada pengalihan) |
| Riwayat buyer (HNK-20) | Ikut terhitung | Tidak terhitung (buyer tidak menerbitkan sertifikat) |
| Registry dan deteksi pembiayaan ganda | Sama | Sama: N tetap dari invoice bertanda tangan buyer |

## Risiko (wajib ditampilkan ke financier sebelum memilih mode ini)
1. **Financier bergantung pada supplier untuk meneruskan pembayaran.** Kalau supplier menahan uang pelunasan, financier tidak punya pengakuan buyer untuk menagih langsung.
2. **Tidak ada pengakuan tertulis buyer.** Menurut Pasal 613 KUHPerdata, pengalihan baru berlaku terhadap debitur setelah diberitahukan atau diakui secara tertulis. Tanpa itu, buyer yang membayar ke supplier sudah sah melunasi utangnya.
3. **Buyer bisa membayar langsung ke supplier dengan cara lain** (tunai, transfer bank) tanpa jejak di chain, sehingga watchdog tidak melihatnya.
4. **Riwayat buyer tidak bertambah**, jadi pelunasan ini tidak memperkuat penilaian buyer berikutnya.
5. **Pembiayaan ganda tetap tertangkap.** Ini satu-satunya perlindungan yang sama kuatnya dengan mode default.

## Status implementasi
- Policy seal untuk surat pengalihan saat ini Supplier → Buyer → Financier ([[Format Data]]). Mode confidential butuh policy kedua (Supplier → Financier) dan penanda tangan `settled` yang berbeda. **Belum diimplementasikan**; dicatat sebagai roadmap.
- Untuk demo ZECATHON hanya alur default yang ditampilkan.
