<p align="center">
  <a href="https://jitsuinfi.vercel.app"><img src=".github/readme/banner.svg" alt="JitsuinFi: Zcash stops double-spending. JitsuinFi stops double-financing." width="100%"></a>
</p>

<p align="center">
  <img alt="Zcash testnet, Ironwood pool" src="https://img.shields.io/badge/Zcash-testnet%20%C2%B7%20Ironwood%20pool-032C7D?style=flat-square">
  <img alt="ZECATHON 2026, Private Markets" src="https://img.shields.io/badge/ZECATHON%202026-Private%20Markets-7E2A53?style=flat-square">
  <img alt="License MIT or Apache-2.0" src="https://img.shields.io/badge/license-MIT%20%7C%20Apache--2.0-461D3A?style=flat-square">
</p>

<p align="center">
  <b>Vault proyek JitsuinFi (Obsidian): workflow, spike, backlog, arsitektur, alur, desain, judging, dan produksi video.</b>
</p>

<p align="center">
  <a href="https://jitsuinfi.vercel.app"><b>Landing</b></a> ·
  <a href="https://jitsuinfi.vercel.app/app"><b>App</b></a> ·
  <a href="https://jitsuinfi.vercel.app/try"><b>Try to double-finance</b></a> ·
  <a href="https://jitsuinfi.vercel.app/verify"><b>Verify</b></a> ·
  <a href="https://jitsuinfi-console-demo.vercel.app/console"><b>Console demo</b></a> ·
  <a href="https://youtu.be/RB9hKSLarJo"><b>2-min video</b></a>
</p>

<p align="center">
  <a href="https://youtu.be/RB9hKSLarJo"><img src=".github/readme/video-thumb.jpg" alt="Watch the 2-minute demo on YouTube" width="760"></a>
  <br><sub>Video demo 2 menit (dirakit di Remotion dari folder Video-Workspace/ vault ini).</sub>
</p>

> **JitsuinFi** adalah pembiayaan invoice (factoring) yang privat di Zcash: buyer menyegel invoice dengan passkey, hanya sidik jarinya N yang masuk papan publik, pembiayaan kedua atas invoice yang sama tertangkap (重) dan menghasilkan bukti portabel (Exhibit A). Advance, segel, dan pelunasan tetap di shielded pool.

<p align="center"><img src=".github/readme/route.svg" alt="The deal route: 照 sent to the buyer, 署 buyer signs, 登 public record, 印 financing letter sealed, 金 advance, 済 settled" width="100%"></p>

<table>
  <tr>
    <td width="50%" valign="top"><img src=".github/readme/try.webp" alt="偽 lalu 重 di papan testnet hidup" width="100%"><br><b>偽 lalu 重 di papan testnet hidup</b><br><sub>/try: ubah satu digit → segel buyer patah; kirim apa adanya → N sudah ada di papan.</sub></td>
    <td width="50%" valign="top"><img src=".github/readme/console.webp" alt="Konsol financier (production, testnet)" width="100%"><br><b>Konsol financier (production, testnet)</b><br><sub>Penawaran tersegel → financing letter dengan segel 売 買 → passkey menyetujui advance.</sub></td>
  </tr>
  <tr>
    <td width="50%" valign="top"><img src=".github/readme/deal.webp" alt="Supplier dan buyer di HP" width="100%"><br><b>Supplier dan buyer di HP</b><br><sub>Invoice ditulis di HP supplier, masuk inbox HP buyer, satu sentuhan passkey menandatangani.</sub></td>
    <td width="50%" valign="top"><img src=".github/readme/verify.webp" alt="真: deal settled nyata" width="100%"><br><b>真: deal settled nyata</b><br><sub>Deal production TES-INV-MOB5-23913 diverifikasi di /verify pada HP buyer.</sub></td>
  </tr>
</table>

## Mulai dari sini

| Baca | Isi |
|---|---|
| [START-HERE](START-HERE.md) | Peta vault, tim, aturan emas |
| [JitsuinFi - Ringkasan Proyek](00-Project/JitsuinFi%20-%20Ringkasan%20Proyek.md) | Apa yang dibangun dan kenapa |
| [ZECATHON - Aturan dan Deadline](00-Project/ZECATHON%20-%20Aturan%20dan%20Deadline.md) | Aturan, kriteria juri, deadline |
| [Workflow Development](01-Workflow/Workflow%20Development.md) | 5 langkah wajib per item |
| [Backlog](03-Backlog/Backlog.md) | Item HNK-xx, task, log deviasi |
| [Decision Log](07-Architecture/Decision%20Log.md) | Keputusan D-xx |
| [FD-00 - Arsitektur Target dan Legenda](08-FlowDiagrams/FD-00%20-%20Arsitektur%20Target%20dan%20Legenda.md) | Arsitektur target, legenda diagram |
| [JDG-00 - Peta Judging](11-Judging/JDG-00%20-%20Peta%20Judging.md) | Sudut pandang juri, titik lemah W-xx, narasi N-xx |
| [Video-Workspace](Video-Workspace/Video-Workspace.md) | Naskah, storyboard, video final (Remotion: `Video-Workspace/README.md`) |

## Isi vault

| Folder | Isi |
|---|---|
| `00-Project/` | Ringkasan proyek, aturan ZECATHON, deskripsi dan runbook submission |
| `01-Workflow/` | Workflow development dan rencana fase |
| `02-Spikes/` | Spike SPK-xx: uji kelayakan tools sebelum build |
| `03-Backlog/` | Backlog HNK-xx dan log deviasi |
| `04-Acceptance-Criteria/`, `05-Testing/`, `06-Executive-Summary/` | AC, tes, dan exec summary per item |
| `07-Architecture/` | Arsitektur, format data, threat model, decision log |
| `08-FlowDiagrams/` | DFD level 0–2, sequence per peran, peta halaman (PlantUML → SVG) |
| `09-Design/`, `10-FE-vault/`, `ColorPalette-JitsuinFi/` | Referensi visual, palet DS-PAL, peta tool frontend |
| `11-Judging/` | Vonis per putaran, kartu skor, register titik lemah, benchmark |
| `Video-Workspace/` | Produksi video demo (Remotion, VO ElevenLabs, footage) |
| `Concepts/`, `Module-Guides/`, `Notes/`, `Templates/`, `scripts/` | Konsep atomik, panduan modul, catatan, template, otomasi (`scripts/sync-vault.py`) |

## Diagram

**Sistem dalam satu gambar** (ringkasan DFD-0, dalam bahasa Inggris seperti di README repo):

```mermaid
flowchart TB
    S([Supplier]):::human
    B([Buyer<br/>passkey]):::human
    F([Financier<br/>node + console]):::human
    M([Fund member]):::human
    O([Anyone<br/>auditor, judge, outsider]):::human
    subgraph J [JitsuinFi]
      W[Web app<br/>jitsuin-wasm in the page]:::sys
      R[Relay<br/>sealed mailboxes]:::sys
      N[Financier node<br/>wallet, board watch]:::sys
    end
    Z[(Zcash testnet<br/>public board: one shielded<br/>address, viewing key published)]:::zcash
    S -- invoice, offer, seals --> W
    B -- signature, seal, ZIP-321 repayment --> W
    W <-- ciphertext only --> R
    R <-- ciphertext only --> N
    F -- passkey approvals --> N
    N -- public record, advance, settled --> Z
    M -- deposits, units --> N
    O -- reads N and ciphertext --> Z
    O -- checks bundles and proofs --> W
    classDef human fill:#FCFCFE,stroke:#7E2A53,color:#461D3A,stroke-width:2px
    classDef zcash fill:#020D2F,stroke:#1D97F1,color:#C4C7F2,stroke-width:2px
    classDef sys fill:#F6F5FC,stroke:#032C7D,color:#020D2F,stroke-width:2px
    classDef seal fill:#7E2A53,stroke:#461D3A,color:#FCFCFE,stroke-width:2px
```

**Satu deal, ujung ke ujung** (ringkasan SEQ-01 – SEQ-03):

```mermaid
sequenceDiagram
    autonumber
    actor S as Supplier
    actor B as Buyer
    participant F as Financier node
    participant R as Public board (Zcash testnet)
    S->>B: 照 invoice, sealed to the buyer's inbox
    B->>S: 署 buyer signs the exact bytes (one passkey touch)
    S->>F: sealed offer (advance asked)
    F->>R: was N = H(invoice) ever registered?
    R-->>F: no, and nothing else
    F->>R: 登 public record (shielded memo)
    F->>S: financing letter
    S->>F: 印 supplier seal
    B->>F: 印 buyer seal
    F->>S: 金 advance + financier seal, one shielded tx (passkey-approved)
    B->>F: repayment from the buyer's own wallet (ZIP-321 slip)
    F->>R: 済 settled entry
    Note over R: Outsiders see a fingerprint and ciphertext.<br/>A second financier finds N on the board: 重, plus Exhibit A.
```

**Cara pembiayaan kedua tertangkap** (ringkasan DFD-2.7):

```mermaid
flowchart TD
    A[Same invoice offered<br/>to financier B]:::human --> C{Buyer's seal valid<br/>for these bytes?}
    C -- no: one digit changed --> X[偽 forged seal<br/>refused]:::seal
    C -- yes --> L{N already on<br/>the public board?}
    L -- no --> OK[register, finance once]:::sys
    L -- yes --> D[重 already pledged<br/>refused before paying]:::seal
    D --> E[Exhibit A: the supplier's key<br/>signed N for two financiers]:::zcash
    E --> V[anyone checks it on /verify<br/>or with jitsuin verify]:::sys
    classDef human fill:#FCFCFE,stroke:#7E2A53,color:#461D3A,stroke-width:2px
    classDef zcash fill:#020D2F,stroke:#1D97F1,color:#C4C7F2,stroke-width:2px
    classDef sys fill:#F6F5FC,stroke:#032C7D,color:#020D2F,stroke-width:2px
    classDef seal fill:#7E2A53,stroke:#461D3A,color:#FCFCFE,stroke-width:2px
```

**Diagram lengkap dari `08-FlowDiagrams/`** (PlantUML, klik untuk membuka):

<details>
<summary><b>DFD-0, diagram konteks</b>: semua entitas luar dan aliran K1 – K14</summary>
<p align="center"><a href="08-FlowDiagrams/assets/dfd-0.svg"><img src="08-FlowDiagrams/assets/dfd-0.svg" alt="DFD-0, diagram konteks" width="100%"></a></p>
</details>
<details>
<summary><b>DFD-1, proses utama</b>: proses 1.0 – 9.0 dan penyimpanan D1 – D19</summary>
<p align="center"><a href="08-FlowDiagrams/assets/dfd-1.svg"><img src="08-FlowDiagrams/assets/dfd-1.svg" alt="DFD-1, proses utama" width="100%"></a></p>
</details>
<details>
<summary><b>SEQ-01, supplier</b>: tulis invoice, tawarkan, segel surat, terima advance</summary>
<p align="center"><a href="08-FlowDiagrams/assets/seq-01-supplier.svg"><img src="08-FlowDiagrams/assets/seq-01-supplier.svg" alt="SEQ-01, supplier" width="100%"></a></p>
</details>
<details>
<summary><b>SEQ-02, buyer</b>: tanda tangan, segel, bayar lewat QR ZIP-321, riwayat</summary>
<p align="center"><a href="08-FlowDiagrams/assets/seq-02-buyer.svg"><img src="08-FlowDiagrams/assets/seq-02-buyer.svg" alt="SEQ-02, buyer" width="100%"></a></p>
</details>
<details>
<summary><b>SEQ-03, financier</b>: cek papan, public record, Sign-to-Pay, settled</summary>
<p align="center"><a href="08-FlowDiagrams/assets/seq-03-financier.svg"><img src="08-FlowDiagrams/assets/seq-03-financier.svg" alt="SEQ-03, financier" width="100%"></a></p>
</details>
<details>
<summary><b>SEQ-04, verifier dan orang luar</b>: apa yang bisa dicek siapa saja</summary>
<p align="center"><a href="08-FlowDiagrams/assets/seq-04-verifier.svg"><img src="08-FlowDiagrams/assets/seq-04-verifier.svg" alt="SEQ-04, verifier dan orang luar" width="100%"></a></p>
</details>
<details>
<summary><b>SEQ-05, anggota dana</b>: setoran, unit, penarikan</summary>
<p align="center"><a href="08-FlowDiagrams/assets/seq-05-fund.svg"><img src="08-FlowDiagrams/assets/seq-05-fund.svg" alt="SEQ-05, anggota dana" width="100%"></a></p>
</details>
<details>
<summary><b>DFD-2.4, pengalihan dan advance</b>: surat pengalihan, segel, Sign-to-Pay</summary>
<p align="center"><a href="08-FlowDiagrams/assets/dfd-2-4.svg"><img src="08-FlowDiagrams/assets/dfd-2-4.svg" alt="DFD-2.4, pengalihan dan advance" width="100%"></a></p>
</details>
<details>
<summary><b>DFD-2.7, deteksi pembiayaan ganda</b>: AlreadyFinanced, DoubleFinanced, Exhibit A</summary>
<p align="center"><a href="08-FlowDiagrams/assets/dfd-2-7.svg"><img src="08-FlowDiagrams/assets/dfd-2-7.svg" alt="DFD-2.7, deteksi pembiayaan ganda" width="100%"></a></p>
</details>
<details>
<summary><b>PG-01, peta halaman per peran</b>: semua halaman app dan konsol</summary>
<p align="center"><a href="08-FlowDiagrams/assets/pg-01-pages.svg"><img src="08-FlowDiagrams/assets/pg-01-pages.svg" alt="PG-01, peta halaman per peran" width="100%"></a></p>
</details>

## Repo

| Repo | What lives there |
|---|---|
| [**jitsuinfi-zcash**](https://github.com/JitsuinFi/jitsuinfi-zcash) | The protocol: canonical invoices, the fingerprint N, board entries, seals, settlement, proofs; the board scanner, the `jitsuin` CLI, `jitsuin-wasm` for the browser, and the ZIP-style spec |
| [**jitsuinfi-frontend**](https://github.com/JitsuinFi/jitsuinfi-frontend) | The web app: landing, supplier / buyer / fund-member desks, `/try`, `/verify`, `/outsider`, `/rates`, and the financier console UI |
| [**jitsuinfi-node**](https://github.com/JitsuinFi/jitsuinfi-node) | The financier's node: keys, Zcash wallet, board watch, Sign-to-Pay, deal API and console |
| [**jitsuinfi-backend**](https://github.com/JitsuinFi/jitsuinfi-backend) | The relay: sealed mailboxes between supplier, buyer and financier; it only ever sees ciphertext |

## Aturan vault

- Setelah mengedit vault: `python3 scripts/sync-vault.py` harus `Broken: 0`.
- Push dan deploy hanya setelah user menyetujui hasil langkah 2 – 4 di workflow.
- Tidak ada seed, key, atau data pribadi di vault.

<p align="center"><img src=".github/readme/outro.webp" alt="Zcash stops double-spending. JitsuinFi stops double-financing." width="640"></p>
