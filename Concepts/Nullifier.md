---
tags: [concept]
---

# Nullifier

**Definisi:** Nilai unik yang dipublikasikan untuk mencegah sesuatu dipakai dua kali, tanpa membuka isinya.

**Detail:** Di Zcash, setiap note yang dibelanjakan menghasilkan nullifier; nullifier yang sama tidak bisa muncul dua kali, sehingga double-spending mustahil tanpa membuka pengirim, penerima, atau nominal. JitsuinFi memakai ide yang sama untuk invoice: `N = BLAKE2b-256("JitsuinNullifier", tanda tangan buyer)`. Karena N diturunkan dari tanda tangan buyer yang tidak bisa ditebak, orang luar tidak bisa menghitung N tanpa memegang invoice.

**Referensi:** [[Format Data]], [[Arsitektur JitsuinFi]]

**Related:** [[Pembiayaan Ganda]], [[Attestor]]
