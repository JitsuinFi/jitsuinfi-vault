---
tags: [flow, sequence, financier]
status: DRAF
updated: 2026-10-19
---

# SEQ-03 - Financier

**Bagian dari:** [[08 - FlowDiagrams]] · Legenda: [[FD-00 - Arsitektur Target dan Legenda]] · Auth: [[SEQ-00 - Autentikasi dan Onboarding]] · Pasangan: [[SEQ-01 - Supplier]] · [[SEQ-02 - Buyer]] · DFD: [[DFD-2.3 - Registrasi Papan]] · [[DFD-2.4 - Pengalihan dan Advance]] · [[DFD-2.5 - Pelunasan dan Settled]] · [[DFD-2.6 - Riwayat Buyer]] · [[DFD-2.7 - Deteksi Pembiayaan Ganda]]

Financier memakai dua lapisan:
- **Konsol web** (browser operator) untuk membaca penawaran, membuat surat pengalihan, memeriksa riwayat buyer, dan membuat bundel.
- **Node financier** (server milik financier) yang memegang spending key wallet dan key financier. Node menjalankan state machine `jitsuin-flow::financier::Flow` dan watchdog pelunasan.

Uang hanya bergerak bila entri financier ini adalah entri valid pertama untuk N, sudah terkonfirmasi, dan surat pengalihan sudah disegel supplier dan buyer. Semua jalur lain berhenti sebelum ada uang yang keluar.

Kode yang dipakai: `jitsuin-flow::financier` (`Flow`, `State`, `Event`, `Financier::{check, register, wait_for_confirmation, pay_advance}`, `sent_advance`), `jitsuin-flow::history::check_buyer`, `jitsuin-flow::settlement` (`repayment`, `Repayment::status`, `settle`, `Financier::post_settled`), `jitsuin-board` (`scan`, `lookup`, `settled`, `lwd::{block_txids, latest_height, block_time}`), `jitsuin-wallet::Devtool`, `src/pages/financier.ts`.

![SEQ-03](assets/seq-03-financier.svg)

```plantuml
@startuml seq-03-financier
!include seq-style.iuml
title SEQ-03 Financier: cek papan, registrasi, Sign-to-Pay, watchdog pelunasan
actor "Operator\nfinancier" as O
box "Konsol (browser operator)" #FAFBFE
  participant "Web app\n(konsol Financier)" as W
  participant "jitsuin-wasm" as X
end box
box "Node financier (server financier)" #F3F6FB
  participant "API node\n(USULAN HNK-05.T3)" as API
  participant "Flow\n(state machine)" as FL
  participant "Wallet financier\n(zcash-devtool,\nspending key)" as WF
  participant "Papan watch-only\n(zcash-devtool, UFVK)" as WB
end box
participant "Relay dokumen\n(USULAN P-04)" as R
participant "Supplier" as S
participant "Buyer" as B
participant "lightwalletd" as LW
database "Chain Zcash\n(papan registry)" as C

== Masuk ==
O -> W : masuk dengan passkey (SEQ-00, konsol node)
W -> API : sesi dari assertion passkey (P-05)

== 1. Terima penawaran ==
S -> R : {invoice, sig_buyer, alamat supplier, advance}
R --> W : penawaran (didekripsi di browser)
W -> X : invoiceDecode + bundleBuild/verifyBundle(invoice, sig_buyer)
X --> W : N, nominal, jatuh tempo, tanda tangan buyer valid
O -> W : tentukan advance, min_confirmations (>= 1), bucket diskon/tenor

== 1b. Siapkan komitmen dan surat (sebelum Flow::new) ==
API -> API : salt 32 byte CSPRNG (USULAN P-08), commitment = BLAKE2b(financier_pk || salt);\nkelas diskon/tenor dari classes_for (belum dipanggil: entri selalu 0/0)
O -> W : unggah PDF surat, isi alamat bayar shielded financier
W -> X : documentHash(PDF) lalu assignmentEncode(invoice, financier_pk, alamat, terms_hash)
X --> W : surat JTSA
W -> R : pembuka komitmen {financier_pk, salt}, kelas + surat ke supplier;\nsurat ke buyer
note right of W #E7F3EA
Flow::new butuh surat dan komitmen (assignment.verify di awal).
Seal boleh dikumpulkan lebih awal, tetapi baru diterapkan di AwaitAssignment
end note

== 2. Cek riwayat buyer (HNK-20, bila policy mewajibkan) ==
W -> R : minta riwayat ke buyer
B -> R : sertifikat 0..k-1, sertifikat k baru, identity_pk
R --> W : rantai sertifikat
W -> API : POST /history/check
API -> WB : scan(papan) (lihat bagian 3)
WB --> API : records, settled
API -> API : check_buyer: verify_history (rantai dari 0, jangkar papan,\nallowlist, cabang, penerus tersembunyi) + verify_certs\n+ sertifikat k cocok dengan invoice + MinimumStandard
alt di bawah standar / rantai tidak valid
  API --> W : BelowStandard / History error
  W --> O : tolak deal, tanpa transaksi
else entri palsu bertag penerus (griefing, Spec #1)
  API --> W : UndisclosedSuccessor
  W --> O : riwayat ditolak walau buyer jujur;\nbelum ada jalur bantahan
else lulus
  API --> W : laporan (on_time, late, defaults, open) + history_tag
end

== 3. Cek papan untuk N (state Check) ==
W -> API : POST /node/deals {invoice, sig, surat, komitmen, alamat supplier,\nadvance, min_confirmations, history_tag}
API -> FL : Flow::new(Deal) (cek min_confirmations, advance, alamat, surat milik invoice)
FL --> API : state Check
API -> WB : sync (lightwalletd)
WB -> LW : compact blocks
LW --> WB : blok
API -> WB : enhance + list_tx
WB -> LW : GetTransaction (transaksi penuh, memo)
LW --> WB : transaksi + memo papan
API -> LW : block_txids(tinggi) untuk urutan tx dalam blok
LW --> API : urutan txid
API -> API : collect: decode memo, urut (tinggi, indeks tx, indeks output)
API -> LW : latest_height
LW --> API : tinggi tip
API -> API : lookup(records, N, supplier_pk dari invoice):\nentri bertanda tangan tidak valid diabaikan
API -> FL : Event BoardChecked {lookup, tip}
alt NotFound
  FL --> API : AwaitSupplierSignature
else Registered oleh komitmen lain
  FL --> API : Stopped(AlreadyFinanced)
  API --> W : "Invoice sudah dibiayai financier lain"
else Registered oleh komitmen sendiri (lanjut setelah crash)
  FL --> API : AwaitConfirmation / AwaitAssignment
else DoubleFinanced
  FL --> API : Stopped(DoubleFinanced) (bukti, lihat jalur financier B)
end

== 4. Minta tanda tangan supplier atas entri ==
API -> R : minta entri untuk komitmen ini (+ history_tag)
R -> S : permintaan (pembuka komitmen sudah dikirim di 1b)
S -> R : entri register bertanda tangan
R -> API : entri
API -> FL : Event SupplierSigned(entri)
FL -> FL : check_entry: jenis register, N, commitment,\ntag riwayat, tanda tangan supplier
FL --> API : Register
note right of FL #FDECEC
Tidak ada cek papan ulang antara SupplierSigned dan posting, dan
register() tidak punya pemulihan seperti sent_advance: crash sebelum
tertambang bisa membuat posting ganda (entri bertag ganda = Equivocation)
end note

== 5. Posting entri dan tunggu konfirmasi ==
API -> WF : sync
API -> WF : pay(alamat papan, 10 000 zat, memo entri)
WF -> LW : kirim transaksi shielded
LW -> C : tx entri
WF --> API : txid entri
API -> FL : Event EntryPosted {txid}
FL --> API : AwaitConfirmation
loop setiap poll sampai terkonfirmasi atau timeout
  API -> WB : scan + latest_height
  API -> FL : BoardChecked
  FL --> API : AwaitConfirmation / AwaitAssignment / Stopped
end
note right of FL #E7F3EA
ADA: wait_for_confirmation. Reorg (entri hilang) kembali ke
AwaitConfirmation; konflik baru menjadi Stopped
end note

== 6. Kumpulkan seal (surat dikirim di 1b) ==
S -> R : seal s0
B -> R : seal s1
R --> W : s0, s1
W -> API : POST /node/deals/N/seals [s0, s1]
API -> FL : Event AssignmentSealed([s0, s1])
FL -> FL : assignment.verify: rantai Supplier lalu Buyer,\nlangkah berikut = Financier
FL --> API : Pay

== 7. Bayar advance (Sign-to-Pay) ==
API -> WB : cek papan terakhir (scan + lookup)
alt konflik atau reorg muncul
  FL --> API : keluar dari Pay, tanpa transaksi
end
API -> WF : sync + list_tx
API -> API : sent_advance(N)? (pemulihan setelah crash: catat txid lama, tidak membayar dua kali)
API -> API : Receipt::sign(advance, N, nominal, tanggal)\n+ seal_next (seal financier s2)\n+ ReceivableNote (N, nilai, jatuh tempo)
API -> WF : pay(alamat supplier, advance, memo 394 byte)
WF -> LW : kirim transaksi shielded
LW -> C : tx advance
WF --> API : txid advance
API -> FL : Event AdvanceSent {txid}
FL --> API : Done
API -> R : txid + memo advance ke supplier (USULAN)

== 8. Watchdog pelunasan (sampai jatuh tempo + tenggang) ==
note right of API #DDEBFA
PARSIAL: fungsi ADA; penjadwal berkala belum ada. Posting settled memakai
spending key, padahal D-23 menulis watchdog akses baca saja (P-12)
end note
loop berkala
  API -> WF : sync + enhance + list_tx
  API -> API : repayment(txs, dokumen pelunasan, buyer_pk):\nkuitansi pelunasan untuk N, ditandatangani buyer_pk,\nnominal = nilai output; klaim buyer dikumpulkan
  API -> API : status: Unpaid / Pending / Partial / Claimed /\nSettled / Disputed / Overdue
end
alt Settled (pembayaran tertambang menutup nominal)
  API -> WB : scan: sudah ada settled valid?
  API -> LW : block_time(tinggi pembayaran penutup)
  LW --> API : waktu blok -> paid_date
  API -> API : settle: flag tepat waktu bila paid_date <= jatuh tempo;\ncountersign klaim buyer (seal financier)
  API -> WF : pay(alamat papan, 10 000 zat, memo settled 167 byte)
  WF -> LW : kirim
  LW -> C : entri settled (dua tanda tangan, settled_tag, tanpa N)
else Claimed lalu Disputed
  API --> W : sengketa: klaim buyer tanpa pembayaran
else Overdue
  API --> W : lewat jatuh tempo, tanpa klaim
end

== 9. Bundel untuk auditor / juri ==
O -> W : "Buat bundel"
W -> X : bundleBuild({invoice, sig_buyer, surat, seal, dokumen pelunasan})
X --> W : bundel JTSB (base64url)
W --> O : unduh / kirim ke pihak berwenang

== Jalur financier B (tertangkap) ==
group financier B menerima invoice yang sama
  API -> API : lookup = Registered (entri financier A lebih dulu)
  FL --> API : Stopped(AlreadyFinanced), tanpa transaksi
  API -> API : proof_from_offer(entri A di papan + posisi, entri B yang ditawarkan)\n(hanya bila supplier sudah memberi entri B, P-14)
  API --> W : bukti JTSP dengan posisi papan
  note right of W #FDECEC
  wasm doubleSignProof tidak mengisi posisi papan;
  bukti seperti itu ditolak jitsuin verify
  end note
  W --> O : "Caught: supplier menandatangani invoice ini dua kali"
end

== Varian manajer dana (JitsuinFi Vault, stretch) ==
group setiap periode
  API -> WF : pay(akun sendiri, root kewajiban JTLR ditandatangani manajer)
  note right of API #E7F3EA : ADA: jitsuin-flow::fund (HNK-15.T2); Merkle sum tree HNK-15.T1 belum
end
@enduml
```

## State machine `Flow`

| State | Masuk dari | Keluar ke | Uang bergerak? |
|---|---|---|---|
| `Check` | `Flow::new` | `AwaitSupplierSignature`; `AwaitConfirmation` / `AwaitAssignment` (entri sendiri sudah ada, lanjut setelah crash); `Stopped` | Tidak |
| `AwaitSupplierSignature` | papan `NotFound` | `Register` (entri lolos `check_entry`) | Tidak |
| `Register` | `SupplierSigned` | `AwaitConfirmation` | Hanya 10 000 zat ke papan |
| `AwaitConfirmation` | `EntryPosted`, reorg | `AwaitAssignment`, `Stopped` | Tidak |
| `AwaitAssignment` | konfirmasi ≥ `min_confirmations` | `Pay` (seal Supplier + Buyer valid); `AwaitConfirmation` (reorg); `Stopped` (konflik baru) | Tidak |
| `Pay` | `AssignmentSealed` | `Done`; `AwaitConfirmation` (reorg); `Stopped` (konflik baru) | Advance + seal financier dalam satu transaksi |
| `Done` | `AdvanceSent` | — | — |
| `Stopped` | `AlreadyFinanced` / `DoubleFinanced` | — | Tidak pernah |

## Ringkasan status

| Bagian | Status | Catatan |
|---|---|---|
| 1, 6, 9 (konsol) | PARSIAL | Layar Financier punya kartu surat, riwayat, bundel; penawaran lewat relay belum |
| 2 riwayat | PARSIAL | `check_buyer` ADA di flow; layar Financier hanya `verifyHistory` tanpa standar minimal |
| 3–5, 7 state machine dan wallet | ADA, diuji testnet (TEST-HNK-19 I-HNK-19.1) | Dijalankan lewat scratchpad CLI, belum lewat API |
| API node | USULAN | HNK-05.T3 (Dex), HNK-05.T4 (integrasi layar) |
| 8 watchdog | PARSIAL | Fungsi ADA (`Repayment::status`, `post_settled`); penjadwal belum ada; konflik dengan D-23 (P-12) |
| Jalur B (bukti) | PARSIAL | Butuh entri B sebelum cek papan (P-14); wasm `doubleSignProof` tanpa posisi papan |
| Jaringan | — | Development di testnet (D-13, `testnet.zec.rocks`); mainnet hanya demo akhir |
| Salt CSPRNG di library | USULAN P-08 | |
