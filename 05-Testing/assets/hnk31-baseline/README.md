# Patokan visual HNK-31

Diambil 2026-10-22 dari jitsuinfi-frontend main `155eaf7` (build production, `vite preview`), Chrome headless (WebGL lewat SwiftShader), tanpa sesi login, dengan `scripts/fe-shots.sh`.

Per route: `<nama>-1440x900.jpg` (layar desktop), `<nama>-390x844.jpg` (ponsel), `<nama>-1440x4000.jpg` (halaman panjang), `<nama>.dom.html` (DOM setelah render, untuk paritas teks).

| Nama | Alamat lama | Alamat baru |
|---|---|---|
| landing | `/` | `/` |
| lobby | `/app.html` | `/app` |
| try | `/app.html#/try` | `/try` |
| verify | `/app.html#/verify` | `/verify` |
| outsider | `/app.html#/outsider` | `/outsider` |
| index | `/app.html#/index` | `/index` |
| account | `/app.html#/account` | `/account` |
| supplier | `/app.html#/supplier` (tanpa sesi: halaman masuk) | `/supplier` |
| buyer | `/app.html#/buyer` (tanpa sesi: halaman masuk) | `/buyer` |
| member | `/app.html#/member` (tanpa sesi: halaman masuk) | `/member` |
| apply | `/app.html#/apply` | `/apply` |
| console | `/console.html` (node lokal belum dipasangkan) | `/console` |
| console-pair | `/console.html?view=pair` | `/console/pair` |

Layar setelah login (meja supplier, buyer, anggota, konsol) tidak bisa diambil headless karena butuh passkey: patokannya ditangkap saat E2E lokal di Chrome sebelum task halaman itu dimulai.
