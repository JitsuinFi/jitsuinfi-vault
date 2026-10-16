---
tags: [concept]
---

# Memo Zcash

**Definisi:** Data terenkripsi sampai 512 byte yang menempel pada setiap output shielded; hanya penerima dan pemegang viewing key yang bisa membacanya.

**Detail:** Byte pertama menentukan jenis isi (ZIP-302): teks UTF-8, tidak ada memo, atau `0xFF` untuk data arbitrer. JitsuinFi memakai memo untuk entri papan registry (sekitar 136 byte), kuitansi pembayaran di muka, dan pelunasan. ZIP 231 (memo bundle lebih besar) masih draft dan tidak masuk NU7, jadi tidak dipakai.

**Referensi:** [[Format Data]]

**Related:** [[ZIP-321]], [[Viewing Key]]
