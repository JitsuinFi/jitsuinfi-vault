---
tags: [project, submission, checklist]
updated: 2026-10-27
---

# Submission - Checklist Publikasi Repo

**Bagian dari:** [[00 - Project]] · Item: HNK-14.T3 di [[Backlog]] · Terkait: [[Submission - Runbook]] · [[Submission - Deskripsi]] · [[ZECATHON - Aturan dan Deadline]] · [[Decision Log]] (D-17, D-53)

> **Status 2026-10-27 (sore): README keempat repo diperbarui dan di-merge** (user menyetujui push): `jitsuinfi-zcash` PR #33 (merge `ad29bec`), `jitsuinfi-node` PR #44 (`4355a6a`), `jitsuinfi-backend` PR #6 (`23e96fd`), `jitsuinfi-frontend` PR #83 (`dcba76e`). Visibilitas frontend dan backend dicatat sebagai D-54. Sisa: hanya bagian 4 (pembukaan `jitsuinfi-zcash`, waktu diputuskan user).
>
> Disegarkan 2026-10-27 oleh agent (hanya baca di repo kode; tidak ada repo yang diubah, dibuka publik, atau di-push). Kode yang dicek: `jitsuinfi-zcash` `614f59a`, `jitsuinfi-node` `4d5044a`, `jitsuinfi-backend` `960cea4`, `jitsuinfi-frontend` `9d30581` (semua `origin/main` setelah `git fetch`, 2026-10-27).

## Ringkasan
| Repo | Visibilitas hari ini | Lisensi | README | Txid di README | Rahasia di riwayat |
|---|---|---|---|---|---|
| `jitsuinfi-zcash` | **PRIVATE** (404 saat logout) | `LICENSE-APACHE` + `LICENSE-MIT`; GitHub membaca Apache-2.0 | Diperbarui (PR #33) | Ada (TES-INV-0003, TES-INV-E2E1-77210, dan sejak PR #33 tabel deal production langkah 6); ~~**belum ada deal production web app**~~ | Bersih |
| `jitsuinfi-node` | PUBLIC (sejak 2026-10-23, D-53) | Sama | Diperbarui (PR #44) | Tidak ada | Bersih |
| `jitsuinfi-backend` | PUBLIC (D-54) | Sama | Diperbarui (PR #6) | Tidak perlu (relay, tanpa chain) | Bersih |
| `jitsuinfi-frontend` | PUBLIC (D-54) | Sama | Diperbarui (PR #83) | Tidak ada | Bersih |
| `jitsuinfi-vault` | PRIVATE (biarkan private) | — | — | — | Tidak dipindai (tidak dipublikasikan) |

Perintah: `gh repo view JitsuinFi/<repo> --json visibility,licenseInfo` dan `curl` signed-out ke `https://github.com/JitsuinFi/<repo>` (2026-10-27).

**Catatan:** ~~`jitsuinfi-backend` dan `jitsuinfi-frontend` sudah PUBLIC, tetapi [[Decision Log]] hanya mencatat D-53 (node).~~ Dicatat sebagai D-54 (2026-10-27). Butir HNK-14.T3 sebelumnya juga masih menulis "LICENSE belum ada di repo mana pun"; itu sudah tidak benar (keempat repo punya lisensi ganda MIT / Apache-2.0). User perlu mengonfirmasi bahwa pembukaan frontend dan backend memang disengaja, lalu mencatatnya sebagai keputusan.

## 1. Lisensi
- [x] `LICENSE-APACHE` dan `LICENSE-MIT` ada di root keempat repo; README masing-masing punya bagian "License" yang sama (dual MIT OR Apache-2.0).
- [x] Dependensi pihak ketiga yang baru (jsQR 1.4.0, Apache-2.0, HNK-34.T14) cocok dengan lisensi ganda.

## 2. README: baris usang dan usulan pengganti
**Selesai 2026-10-27:** semua usulan wajib di bawah diterapkan lewat PR yang disebut di atas (README saja). Yang opsional (membuang ID internal `HNK-…`, `D-…`) tidak dikerjakan, kecuali rujukan "vault" di README backend dan node. Baris di bawah dirujuk dengan `file:baris` pada commit di atas.

### `jitsuinfi-zcash/README.md`
| Baris | Isi sekarang | Masalah | Usulan |
|---|---|---|---|
| 3 – 7 | Pembuka tanpa tautan | Juri yang datang dari form tidak melihat app live | Sisipkan setelah baris 5: `**Live:** [jitsuinfi.vercel.app](https://jitsuinfi.vercel.app) (app at [/app](https://jitsuinfi.vercel.app/app), verifier at [/verify](https://jitsuinfi.vercel.app/verify)) · financier console demo: <https://jitsuinfi-console-demo.vercel.app/console> · other repos: [jitsuinfi-node](https://github.com/JitsuinFi/jitsuinfi-node), [jitsuinfi-frontend](https://github.com/JitsuinFi/jitsuinfi-frontend), [jitsuinfi-backend](https://github.com/JitsuinFi/jitsuinfi-backend).` |
| 30 | Snapshot "entries up to block 4511024, captured 2026-10-20" | Benar sebagai fixture, tetapi papan live kini 55 entri (tip 4547249, 2026-10-27) | Tambahkan: `The live board has grown since (55 entries at block 4547249 on 2026-10-27); the snapshot stays fixed so CI can compare output byte for byte.` |
| 91 | "paste the proof text, choose the board snapshot (or your own from step 3) as board data and press Verify" | Tombol kini "Hand it to the registry"; papan live dibaca otomatis; ada tombol contoh | `**4. In the browser:** open <https://jitsuinfi.vercel.app/verify>, press "Use Case File #0417's Exhibit A" or paste a proof, bundle or Exhibit A, and press "Hand it to the registry". The page reads the live board by itself (or a board file you add) and runs the same checks compiled to WebAssembly, in the page.` |
| 93 – 108 | E2E terakhir yang tercatat: `TES-INV-E2E1-77210` (2026-10-22, skrip) | Deal production lewat web app dan konsol (HNK-34) tidak ada; deskripsi v3 menulis "Full txids in the README" | Tambahkan bagian baru setelah baris 108 (teks siap tempel di bawah tabel ini) |
| 145 | `flow --> be[financier backend]` | Namanya sekarang `jitsuinfi-node` | `flow --> be[jitsuinfi-node<br/>financier node + console]` |

Teks siap tempel untuk `jitsuinfi-zcash/README.md` setelah baris 108:

```markdown
**6. Through the live web app and console (production, testnet).** These deals ran on <https://jitsuinfi.vercel.app>, the financier console and the hosted node, by clicks only:

| Deal | Step | Testnet txid |
|---|---|---|
| `TES-INV-JUDGE3-9161` (2026-10-27, installed app, no typed URL) | Register entry (block 4545839) | `35ed74696145f5838188dffe49ef9a51cd5ae054f3de97044ec8855ed859bd55` |
| | Advance, approved with the console passkey | `1de9e9473d3e6b01f9037820908bca77a20891f203d95fe372886abb8343f48f` |
| | Repayment by the buyer's ZIP-321 QR | `668d0e0f3cca380dff846b936390a9526992de717260012fac6d0efd316d331a` |
| | Settled entry (block 4545868) | `208d9d573bc39e3e80d9771eb22695b5d666622576bffb790369c06f619735ba` |
| `TES-INV-DBL-24689` (2026-10-25) | First entry, production node (block 4540314) | `a2f46ffdeebef1e0fa4de74b8b2bb26083a48cb9528a72ab7ac26914a7103659` |
| | Second financier's entry (block 4540315): the console stops the deal as `DoubleFinanced` | `a42152b0ed19b5f54437ddfe61bc44b811dd3d405e78b863f3b060f237709188` |
| `TES-INV-ALR-71337` (2026-10-25) | Earlier entry (block 4540347): the console stops as `AlreadyFinanced` before paying | `25a78d45bc2ab59a5f48fff8b594cdc0bdc9cf1e218a36bd7ae8cbcb51bf75b5` |

The board entries read with the board UFVK above (`jitsuin verify --ufvk …` lists them); the advance and the repayment are shielded payments, so an explorer shows only that they exist.
```

Sumber txid: entri papan dibaca dari `https://jitsuinfi-console.vercel.app/node/board` (publik) pada 2026-10-27, dan dicek ulang ke `https://financier-node-production.up.railway.app/node/board` sebelum PR #33 (kelima entri ada, tinggi blok cocok; papan 55 entri, tip 4547279); advance dan pelunasan JUDGE3 dari log E2E HNK-34.T13. Txid deal video (`TES-INV-VID-03`) ditambahkan setelah rekaman.

### `jitsuinfi-node/README.md`
| Baris | Isi sekarang | Masalah | Usulan |
|---|---|---|---|
| 3 | "its console and, next, the deal API" | Deal API sudah ada (tabel API baris 69 – 98) | "…its relay mailbox, its console and the deal API that console uses." |
| 15 – 17 | Hanya konsol demo | Tidak ada tautan app live dan bukti deal | Tambahkan setelah baris 17: `Production: deals on <https://jitsuinfi.vercel.app> run against this node; their testnet txids are in the jitsuinfi-zcash README ("Through the live web app and console").` |
| 65 | `ZCASH_DEPLOY_KEY` (read-only deploy key of `jitsuinfi-zcash`) | Tidak perlu lagi setelah zcash publik | Biarkan sampai zcash publik; sesudahnya boleh ditulis "needed only while `jitsuinfi-zcash` was private" |
| 108 | "The full table is in the vault, *Threat Model*…" | Vault PRIVATE, juri tidak bisa membuka | "The protocol's security and privacy considerations are in the `jitsuinfi-zcash` specification (`docs/zip-shielded-receivable-registry.md`, sections Security considerations and Privacy considerations)." |
| 3, 13, 15, 19, 27, 30, 36, 41, 43, 45, 69, 104, 107 | ID internal `HNK-26.T…`, `D-43`, `D-46` | Rujukan ke vault private; tidak salah, hanya bising | Opsional: buang ID internal |

### `jitsuinfi-frontend/README.md`
| Baris | Isi sekarang | Masalah | Usulan |
|---|---|---|---|
| 1 – 3 | Tanpa URL live | — | Sisipkan setelah baris 3: `Live: <https://jitsuinfi.vercel.app> (landing), [/app](https://jitsuinfi.vercel.app/app) (the app; installable as a PWA), financier console demo <https://jitsuinfi-console-demo.vercel.app/console>. Testnet txids of real deals: jitsuinfi-zcash README.` |
| 3 | "supplier, buyer and financier screens" | Financier bekerja di konsol; ada peran anggota dana | "supplier, buyer and fund-member desks with a sealed inbox, the financier console, a verify page for auditors and judges, and a page showing what outsiders can see." |
| 7 | "Buyer keys come from a passkey … nothing stored." | Dokumen deal disimpan terenkripsi di perangkat (`src/lib/store.ts`) | "Keys come from a passkey (WebAuthn PRF extension): no seed phrase, no key stored. Test data stands in on devices without PRF." |
| 8 | "Secrets stay in page memory only; they are never written to storage." | Kunci memang hanya di memori, tetapi dokumen deal ditulis ke IndexedDB | "Keys stay in page memory. Deal documents are kept on the device in IndexedDB, sealed with AES-GCM under a key derived from the passkey, with HMAC record names so the store does not show which invoices it holds." |
| 9 | "run in the financier's backend wallet (`jitsuin-flow`)" | Sekarang `jitsuinfi-node` | "…run in the financier's node (`jitsuinfi-node`, built on `jitsuin-flow`)…" |
| 19 | "`/account`, `/supplier`, `/buyer`, `/member` … role desks" | Route per bagian peran (HNK-34.T12) tidak tercantum | Ganti dengan: `/supplier/invoices`, `/supplier/invoices/new`, `/supplier/deal/$ref`, `/supplier/contacts`; `/buyer/invoices`, `/buyer/invoices/key`, `/buyer/pay`, `/buyer/history`, `/buyer/contacts`; `/member/fund`, `/member/units`, `/member/contacts`; `/financier`; `/app/contact` (contact link) |
| 22 (baru) | — | Inbox, PWA, scanner tidak disebut | Tambahkan: "Signed in, a bell opens one inbox sheet for every sealed letter. `manifest.webmanifest` makes the app installable; the console host serves its own manifest. QR codes are scanned in the app (BarcodeDetector or jsQR 1.4.0) with `Permissions-Policy: camera=(self)`." |

### `jitsuinfi-backend/README.md`
| Baris | Isi sekarang | Masalah | Usulan |
|---|---|---|---|
| 48 | "give the Railway GitHub app access to this private repo" | Repo sudah PUBLIC | "…→ `JitsuinFi/jitsuinfi-backend`, branch `main`." |
| 3, 5, 13, 29, 44, 50, 54 | Rujukan `vault D-33`, `HNK-23…` | Vault private | Opsional: buang ID internal |

## 3. Pindai rahasia (2026-10-27)
**Hasil: bersih di keempat repo.** `gitleaks` dan `trufflehog` tidak terpasang, jadi pindaian memakai grep atas `git log -p --all` (semua ref termasuk cabang remote) dan atas judul + isi semua PR di GitHub.

| Repo | Commit dipindai | Sejak 2026-10-22 | PR dipindai |
|---|---|---|---|
| `jitsuinfi-zcash` | 106 | 7 | 32 |
| `jitsuinfi-node` | 97 | 16 | 43 |
| `jitsuinfi-backend` | 14 | 5 | 5 |
| `jitsuinfi-frontend` | 274 | 110 | 82 |

Pola: `AGE-SECRET-KEY-1`, `-----BEGIN … PRIVATE KEY`, token GitHub (`ghp_`, `github_pat_`, `gho_`), `sk_live/sk_test`, Slack, AWS, JWT (`eyJ…`, termasuk kunci Supabase), URI Postgres berpassword, `secret-extended-key`, viewing key Sapling, `RAILWAY_TOKEN=`, `VERCEL_TOKEN=`, `SETUP_CODE=` berisi, fragmen `pair#`, `contact#`, `invite#`, `supabase.co`, URL pooler, `api_key=`, mnemonic 12 – 24 kata, hex 64 karakter di samping kata secret / seed / master / priv / spend / token / password, UFVK / USK, `DATABASE_URL=` berisi; ditambah daftar nama file dari seluruh riwayat (`.env`, `.age`, `.key`, `.pem`, wallet, credential, sqlite).

Temuan yang dicek dan **bukan rahasia**:
- `crates/jitsuin-core/tests/vectors/invoice_v1.txt`: `buyer_seed` / `supplier_seed` adalah vektor uji Ed25519 yang dibuat ulang skrip Python publik.
- Token `0101…01` di fixture dana (zcash dan frontend): nilai uji tetap.
- `…/console/pair#ABCD-EFGH-IJKL-MNOP` di tes node dan frontend: placeholder.
- `uviewtest1wcey…`: UFVK papan publik (D-11), memang dipublikasikan.
- `zxviewtestsapling1q` di tes CLI: string tidak valid untuk menguji pesan error.
- `jitsuinfi-backend/.env.example`: `DATABASE_URL=` dan `TEST_DATABASE_URL=` kosong; README hanya memuat bentuk URI dengan `<database-password>`.
- Nama file riwayat: hanya `.env.example`, kode `passkey.ts` / `passkey.js`, dan `jitsuin-wallet` (kode), tanpa berkas kunci.
- PDF `examples/testnet/e2e-tes-inv-e2e1/*.pdf`: tanpa metadata Author / Creator.

**Bukan rahasia, tetapi akan terlihat saat zcash dibuka:** email penulis commit di riwayat `jitsuinfi-zcash` (`hansgunawan775@…`, `shenhan603@…`, satu kontributor tim dengan 4 commit). Repo publik lain sudah memuat email `hansgunawan775@…`. Mengubahnya butuh tulis ulang riwayat dan force-push; disarankan diterima apa adanya.

Pindaian ini menangkap pola yang dikenal, bukan semua kemungkinan. Bila mau lapisan kedua sebelum zcash dibuka: `brew install gitleaks && gitleaks git --log-opts="--all" .` di tiap repo.

## 4. Sisa sebelum `jitsuinfi-zcash` dibuka publik (keputusan waktu: user)
Aturan: "Open source at submission. A private repo made public on Oct 28 counts." Batas praktis: sebelum menekan Submit, paling lambat 28 Okt 23:59 UTC.

- [x] (Disarankan sebelum dibuka) README zcash diperbarui (PR #33, 2026-10-27; CI zcash tidak jalan karena billing Actions, di-merge karena README saja): tabel txid production, baris 91, baris 145, blok tautan live (bagian 2). Deskripsi v3 bergantung pada tabel txid.
- [ ] User menerima bahwa email penulis commit ikut terlihat (bagian 3).
- [ ] Buka: GitHub → `JitsuinFi/jitsuinfi-zcash` → Settings → General → Danger Zone → Change visibility → Public (atau `gh repo edit JitsuinFi/jitsuinfi-zcash --visibility public --accept-visibility-change-consequences`). Dilakukan user.
- [ ] Sesudahnya: `https://github.com/JitsuinFi/jitsuinfi-zcash` terbuka di jendela private (HTTP 200); 33 cabang remote ikut publik (sudah ikut dipindai).
- [ ] Sesudahnya: `cargo build` di `jitsuinfi-node` dari klon bersih tanpa kredensial bisa mengambil dependensi git `jitsuinfi-zcash` rev `c2ff6383…` (commit itu ada di `main`); `docker build -t jitsuin .` di zcash berjalan seperti README langkah 1.
- [ ] Sesudahnya: CI node tetap hijau (deploy key tidak lagi diperlukan untuk membaca repo publik).
- [ ] Catat keputusan pembukaan (tanggal, siapa) di [[Decision Log]] dan tandai butir ini.
