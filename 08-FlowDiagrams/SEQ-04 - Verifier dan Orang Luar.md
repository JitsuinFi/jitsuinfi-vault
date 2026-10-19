---
tags: [flow, sequence, verifier]
status: DRAF
updated: 2026-10-20
---

# SEQ-04 - Verifier dan Orang Luar

**Bagian dari:** [[08 - FlowDiagrams]] · Legenda: [[FD-00 - Arsitektur Target dan Legenda]] · DFD: [[DFD-2.7 - Deteksi Pembiayaan Ganda]] · [[DFD-2.8 - Verifikasi dan Indeks Publik]]

Peran tanpa akun dan tanpa key. Tiga jenis pengguna:
- **Juri / auditor.** Memegang bundel (JTSB) atau bukti tanda tangan ganda (JTSP) dari pihak deal, dan UFVK papan. Memverifikasi lewat CLI `jitsuin verify` (paling kuat, memindai chain sendiri) atau lewat layar Verify di web.
- **Pengamat indeks.** Membaca indeks suku bunga publik (`jitsuin index`, halaman indeks HNK-08.T3). `jitsuin index` butuh UFVK papan.
- **Orang luar.** Dua jenis: pengamat block explorer (tidak melihat memo, hanya waktu blok, jumlah action, fee, txid) dan pemegang UFVK papan tanpa bundel (melihat isi memo: jenis entri, N, commitment, kelas, tag, flag tepat waktu, tanda tangan yang tidak bisa dicek tanpa invoice).

Kode yang dipakai: `jitsuin-cli` (`args`, `board::{load, scan, from_snapshot, to_snapshot}`, `verify::{run, check_proof, check_bundle}`, `index::run`), `jitsuin-board` (`collect`, `lookup`, `verify_proof_on_board`, `bundle_on_board`, `rate_index`), `jitsuin-wasm` (`verifyBundle`, `verifyProof`, `bundleOnBoard`, `boardMemoDescribe`; `rateIndex` USULAN), `src/pages/verify.ts`, `src/pages/outsider.ts`.

![SEQ-04](assets/seq-04-verifier.svg)

[Buka diagram ukuran penuh](assets/seq-04-verifier.svg)

```plantuml
@startuml seq-04-verifier
!include seq-style.iuml
title SEQ-04 Verifier dan orang luar: verifikasi tanpa key dan tanpa ZEC
actor "Juri / auditor" as J
actor "Orang luar" as OL
box "Mesin juri" #FAFBFE
  participant "jitsuin CLI\n(Docker / cargo install)" as CLI
  participant "Wallet watch-only\n(zcash-devtool, UFVK papan)" as WB
end box
box "Browser" #FAFBFE
  participant "Web app\n(Verify, Orang luar, Indeks)" as W
  participant "jitsuin-wasm" as X
end box
participant "Relay\n(snapshot papan, USULAN P-06)" as R
participant "lightwalletd" as LW
database "Chain Zcash\n(papan registry)" as C

== A. CLI: jitsuin verify (paling kuat) ==
J -> CLI : jitsuin verify ~--ufvk <UFVK papan> ~--birthday <tinggi>\n~--proof bukti.txt ~--bundle bundel.txt
note right of J #FFF6D6 : UFVK + birthday papan belum dipublikasikan\n(D-11 masih usulan)
CLI -> CLI : parse argumen, jaringan dari awalan UFVK\n(uview1 / uviewtest1)
alt wallet watch-only belum ada
  CLI -> WB : init-fvk(UFVK, birthday)
end
CLI -> WB : sync
WB -> LW : compact blocks
LW --> WB : blok
CLI -> WB : enhance + list_tx
WB -> LW : transaksi penuh
LW --> WB : memo papan
CLI -> LW : block_txids per tinggi (urutan tx dalam blok)
LW --> CLI : urutan
CLI -> CLI : collect: register, settled, rejected; urut total
loop setiap ~--proof
  CLI -> CLI : DoubleSignProof::verify (tanda tangan buyer, N,\ndua entri bertanda tangan supplier, komitmen berbeda)
  CLI -> CLI : verify_proof_on_board (posisi yang diklaim ada\ndi papan, entri pertama sebelum kedua);\nbukti tanpa posisi entri pertama = FAIL
end
loop setiap ~--bundle
  CLI -> CLI : Bundle::verify (tanda tangan buyer, surat + rantai\nseal, dokumen pelunasan)
  CLI -> CLI : bundle_on_board: lookup register + settled\ndua tanda tangan
end
CLI --> J : tabel entri + PASS/FAIL/INFO per cek;\nexit 0 semua lulus, 1 ada yang gagal,\n2 error input/jaringan
note right of CLI #E7F3EA
ADA (PR #4, #6). Instal dari sumber 550-868 detik
(AC-HNK-09.1 FAIL); usulan D-28: image
ghcr.io/jitsuinfi/jitsuin
end note

== B. CLI offline dari snapshot ==
J -> CLI : jitsuin verify ~--board papan.json ~--proof bukti.txt
CLI -> CLI : from_snapshot (memo 512 byte base64url)\nlalu verifikasi sama
CLI --> J : hasil (tanpa jaringan)

== C. Indeks suku bunga publik ==
J -> CLI : jitsuin index ~--ufvk <UFVK> [~--k 5]
CLI -> CLI : rate_index: tiap N sekali (entri register pertama),\nper kelas tenor, kelas diskon dengan >= k invoice;\ntanda tangan entri tidak diperiksa
CLI --> J : median kelas diskon per tenor; kelas < k tidak diberi angka
note right of CLI #FDECEC
PARSIAL: output selalu kosong selama kelas tidak
dihitung (classes_for belum dipanggil, entri 0/0,
FD-00 §6). Entri spam atau griefing ikut terhitung
end note
W -> R : GET snapshot papan
R --> W : memo papan
W -> X : rateIndex(snapshot, k) (USULAN: wrapper wasm\ndari jitsuin_board::rate_index, HNK-08.T3)
W --> OL : halaman indeks (HNK-08.T3, belum ada)

== D. Web: layar Verify ==
J -> W : buka /app.html#/verify, tempel bundel (JTSB)\natau bukti (JTSP)
alt bundel
  W -> X : verifyBundle(bundel)
  X --> W : N, invoice_id, nominal, jatuh tempo, status surat
  alt saat ini (ADA)
    J -> W : unggah file snapshot papan (JSON)
  else target (USULAN P-06, P-11)
    W -> R : GET /api/board (same-origin)
    R --> W : snapshot papan
  end
  W -> X : bundleOnBoard(bundel, snapshot)
  X --> W : register: Registered / NotFound / DoubleFinanced;\nsettled: {txid, on_time}
  W --> J : "every seal checks out" muncul juga bila surat\nbelum lengkap atau tanpa settled (lihat baris surat\ndan status settled)
else bukti tanda tangan ganda
  W -> X : verifyProof(bukti) (offline saja)
  X --> W : valid: supplier menandatangani N yang sama\nuntuk dua financier
  W --> J : banner "Caught: the supplier signed this invoice twice",\nposisi papan hanya diklaim; unduh bukti
  note right of X #FDECEC
  Web tidak memeriksa posisi di papan: file papan
  yang diunggah tidak dipakai. Bukti yang FAIL di
  jitsuin verify (tanpa posisi entri pertama) tetap
  "Caught" di web. Usulan P-14: verifyProofOnBoard
  end note
end
note right of W #DDEBFA
PARSIAL: layar Verify ADA; snapshot papan sekarang
diunggah sebagai file (P-06 belum). Snapshot dari relay
berarti percaya pada kelengkapannya; hasil web bisa
berbeda dari PASS/FAIL CLI, keputusan akhir lewat
jitsuin verify
end note

== E. Orang luar ==
OL -> C : pengamat explorer: buka block explorer
C --> OL : transaksi shielded: waktu blok, jumlah action,\nfee, txid; isi memo, nominal, alamat tersembunyi
OL -> W : halaman "What outsiders see" (/app.html#/outsider)
W --> OL : tabel publik vs tersembunyi + kartu explorer
OL -> W : pemegang UFVK papan: tempel satu memo papan
W -> X : boardMemoDescribe(memo)
X --> OL : jenis entri (0x03 = buyer memakai riwayat), N,\ncommitment, kelas diskon/tenor, tag, flag tepat waktu;\ntanda tangan tidak bisa dicek tanpa invoice
@enduml
```

## Yang bisa dan tidak bisa dipastikan

| Pengguna | Bisa memastikan | Tidak bisa |
|---|---|---|
| Juri dengan UFVK papan + bukti | Supplier menandatangani satu invoice untuk dua financier; urutan entri di chain (CLI); isi invoice di bukti (nominal, tanggal, `invoice_id`, key per invoice) | Siapa supplier, buyer, financier; apakah itu niat menipu |
| Auditor dengan bundel | Tanda tangan buyer dan satu registrasi (PASS). "Surat disegel lengkap" hanya bila baris `signatures` menyebut "sealed by supplier, buyer, financier" (surat belum lengkap = INFO `letter`). Pelunasan dua tanda tangan di papan, tepat waktu atau terlambat, hanya bila ada baris PASS `settlement`; bundel tanpa dokumen pelunasan = INFO, dokumen pelunasan tanpa entri settled = FAIL. "DEAL VERIFIED" di CLI dan "every seal checks out" di web juga muncul saat surat belum lengkap | Deal lain |
| Pengamat indeks | Agregat per kelas tenor dan diskon dengan ambang k = 5 (selama kelas 0/0, indeks kosong) | Nominal dan pihak. k hanya melindungi agregat: kelas tiap entri terbaca pemegang UFVK papan, dan entri tanpa tanda tangan yang sah ikut terhitung, jadi indeks bisa digeser |
| Pengamat explorer | Ada transaksi shielded pada waktu tertentu (jumlah action, fee, txid) | Isi memo, apakah tx itu posting papan |
| Pemegang UFVK papan tanpa bundel | Jenis entri, N, commitment, kelas, tag, flag tepat waktu tiap entri; N yang muncul dua kali | Isi invoice, pihak, keabsahan tanda tangan, apakah konflik itu penipuan atau griefing |

Temuan pra-review terkait di [[Pra-review Spesifikasi dan Threat Model]]:
- TM #3: siapa pun yang memegang N bisa menghitung `settled_tag(N)` dan menautkan entri `settled` ke register; korelasi waktu dan tenor juga bisa.
- TM #5: kelas tiap entri terbaca pemegang UFVK papan; ambang k hanya untuk agregat.
- TM #6: `identity_pk` ada di setiap sertifikat; pemegang ujung rantai bisa menghitung tag invoice berikutnya buyer.
- TM #13: pemegang UFVK papan juga melihat jenis entri (0x01 vs 0x03) dan txid.
- TM #14: tabel "What outsiders see" belum punya baris untuk kelas, flag tepat waktu, jenis entri, waktu blok.
- TM #16: bukti tanda tangan ganda juga memuat invoice penuh dan kedua entri.
