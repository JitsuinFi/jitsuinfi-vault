---
tags: [flow, sequence, fund]
status: DRAF
updated: 2026-10-20
---

# SEQ-05 - Anggota Dana

**Bagian dari:** [[08 - FlowDiagrams]] · Legenda: [[FD-00 - Arsitektur Target dan Legenda]] · Auth: [[SEQ-00 - Autentikasi dan Onboarding]] · DFD: [[DFD-2.9 - Solvabilitas Dana]] · Item: [[AC-HNK-15 - Stretch JitsuinFi Vault|HNK-15]]

JitsuinFi Vault (stretch, D-24): banyak anggota menyetor ZEC shielded ke satu dana; manajer dana membiayai invoice lewat JitsuinFi sebagai financier ([[SEQ-03 - Financier]]); setiap anggota menghitung sendiri apakah aset dana menutup kewajibannya, tanpa melihat buyer atau isi invoice.

Batas uji ini: sisi aset dinyatakan oleh manajer sendiri. Nilai piutang adalah `face_zat` dan jatuh tempo dari catatan JTN1 manajer; yang diperiksa hanya tanda tangan kuitansi terhadap `manager_pk`, dan tidak ada yang mengikat nilai itu ke advance atau ke invoice sungguhan. "Advance" kecil dengan nilai piutang besar dan jatuh tempo jauh dihitung `Open` dengan nilai penuh sampai jatuh tempo + tenggang, jadi dana yang tidak solvent bisa lolos sampai saat itu; pelanggaran baru terlihat sebagai gagal bayar. Usulan: batasi nilai terhadap advance (diskon dan tenor maksimum) atau wajibkan entri register yang cocok di papan.

Anggota mendaftar dengan passkey hanya untuk kotak surat (kuitansi setoran dan jalur Merkle tiap periode, [[SEQ-00 - Autentikasi dan Onboarding]]); anggota tidak menandatangani apa pun.

Kode yang dipakai: `jitsuin-flow::fund` (`fund_view`, `member_view`, `solvency`, `SolvencyPolicy`, pembacaan catatan piutang `JTN1` dan root kewajiban `JTLR`), `jitsuin-core::fund`, wallet watch-only `zcash-devtool`. Belum ada: Merkle sum tree kewajiban (HNK-15.T1, Dex), halaman anggota (HNK-15.T3, Dave). Perintah CLI: `jitsuin fund` (HNK-27.T10).

![SEQ-05](assets/seq-05-fund.svg)

[Buka diagram ukuran penuh](assets/seq-05-fund.svg)

```plantuml
@startuml seq-05-fund
!include seq-style.iuml
title SEQ-05 Anggota dana: setor, laporan periode, uji solvabilitas
actor "Anggota" as M
box "Perangkat anggota" #FAFBFE
  participant "Wallet Zodl\nanggota" as ZM
  participant "jitsuin (lokal)\n+ zcash-devtool watch-only" as LOC
  participant "Web app\n(halaman anggota, HNK-15.T3)" as W
end box
participant "Relay dokumen\n(USULAN P-04)" as R
participant "Manajer dana\n(node financier)" as MG
participant "lightwalletd" as LW
database "Chain Zcash\n(akun setoran,\nakun operasional)" as C

== Masuk ==
M -> W : daftar / masuk dengan passkey (SEQ-00),\nhanya untuk kotak surat

== 1. Setor ==
M -> ZM : kirim ZEC shielded ke alamat setoran dana
ZM -> C : transaksi shielded
MG -> MG : catat setoran sebagai daun Merkle sum tree\n(id anggota acak, nominal)
note right of MG #FFF6D6 : USULAN: HNK-15.T1 (Dex) belum ada
MG -> R : kuitansi setoran (terenkripsi ke kotak surat anggota)
R --> W : kuitansi setoran
MG -> C : pindahkan dana dari akun setoran ke akun\noperasional (akun setoran: viewing key hanya auditor)
note right of MG #FDECEC
Tanpa penggabungan, pemegang UFVK operasional
melihat nominal tiap setoran (tanpa identitas)
end note

== 2. Dana membiayai invoice ==
MG -> C : advance per invoice (SEQ-03): memo = kuitansi\nadvance + seal + catatan piutang JTN1\n(N, nilai, jatuh tempo)
C -> MG : pelunasan buyer masuk ke akun operasional\n(memo kuitansi pelunasan)

== 3. Laporan periode ==
MG -> C : self-send ke akun operasional: root kewajiban JTLR\n(periode, root, total kewajiban, key manajer,\ntanda tangan)
note right of MG #E7F3EA : ADA: post_liability_root + verifikasi JTLR (HNK-15.T2)
MG -> R : jalur Merkle tiap anggota untuk periode ini\n(terenkripsi, USULAN HNK-15.T1)
R --> W : jalur Merkle periode p

== 4. Uji solvabilitas oleh anggota (P-10: UFVK tidak ke server) ==
MG -> M : UFVK akun operasional, birthday, manager_pk\n(sekali, saluran privat)
M -> LOC : init-fvk(UFVK, birthday)
LOC -> LW : sync + enhance
LW --> LOC : transaksi akun operasional (masuk dan keluar)
LOC -> LOC : balance_zat = kas
LOC -> LOC : jitsuin fund: member_view(manager_pk, tenggang, hari ini)\nlalu fund_view: advance dengan kuitansi bertanda\ntangan manajer + JTN1 menjadi piutang;\npelunasan per N; Open / Repaid / Overdue;\nroot JTLR bertanda tangan manajer (lain diabaikan)
LOC -> LOC : solvency(potongan): kas + piutang berjalan +\npiutang lewat tempo setelah potongan\n>= total root terbaru
LOC -> LOC : bukti inklusi: jalur Merkle periode p berakhir\ndi root JTLR terbaru dan jumlah = total JTLR\n(HNK-15.T1)
LOC --> M : solvent / tidak / belum ada root,\nrincian per N (tanpa pihak)
LOC -> W : ekspor hasil pindaian lokal (opsional)
W --> M : tampilan laporan (HNK-15.T3, belum ada)
note right of LOC #DDEBFA
PARSIAL: fund_view, solvabilitas, dan perintah
jitsuin fund ADA (HNK-27.T10); halaman anggota
belum (HNK-15.T3). Tenggang masuk lewat member_view
end note
@enduml
```

## Yang dilihat anggota

| Melihat (lewat UFVK akun operasional) | Tidak melihat |
|---|---|
| Kas; setiap advance (N, nominal, jatuh tempo) dan alamat shielded penerimanya; pelunasan per N; root kewajiban; nominal tiap setoran tanpa identitas (kecuali setoran digabung) | Identitas supplier, buyer, isi invoice, identitas anggota lain |

Alamat penerima advance terlihat: wallet yang hanya memegang UFVK membaca memo JTN1 dari advance keluar lewat pemulihan OVK, dan pemulihan itu juga membuka alamat penerima (AC-HNK-15.3). Anggota melihat alamat shielded supplier, bukan identitasnya. Mitigasi: satu alamat diversified per deal di sisi supplier (lihat [[SEQ-01 - Supplier]] bagian 3). Ini menjawab keputusan 4 di [[Pra-review Spesifikasi dan Threat Model]] (TM #4); Hans tinggal mengonfirmasi.

Jalur Merkle sum juga membuka jumlah node saudara, termasuk nominal setoran minimal satu anggota lain. Catat untuk HNK-15.T1.
