# Lucky Kit

Repository ini mengembangkan dan mendistribusikan skill `lucky-kit`, dengan nama tampilan **Lucky Kit**. Pembuat dan pemegang hak cipta: **Ihza Luckyan Passya**.

Skill membantu pengguna mengubah ide, artefak yang sudah tersedia, atau codebase menjadi dokumentasi selaras dan handoff implementasi. Nama folder sumber adalah `Lucky-Kit`. Hasil aplikasi pengguna berada di workspace aplikasinya masing-masing.

## Batas workspace

- Edit skill pada [sumber utama](skills/lucky-kit/SKILL.md). Salinan terpasang adalah hasil instalasi.
- Untuk ide aplikasi, lanjutkan diskusi sesuai scope. Sebelum menulis dokumen produk atau kode, pastikan workspace tujuan berada di luar repository ini.
- Jangan membuat chat baru tanpa diminta atau memakai keputusan aplikasi lain sebagai default.
- Simpan artefak pengujian, transkrip, dan hasil aplikasi di luar repository.

## Struktur dan penulisan

- Instruksi umum serta routing berada di `SKILL.md`, detail workflow di `references/`, dan template di `assets/templates/`.
- Seluruh kebutuhan runtime skill harus berada dalam `skills/lucky-kit/`. Jangan menggandakan template atau membuat referensi skill bergantung pada root repository.
- Gunakan nama deskriptif lowercase kebab-case, dengan nama konvensional seperti `SKILL.md`, `README.md`, dan `LICENSE` tetap dipertahankan.
- Dokumentasi publik utama berbahasa Inggris, dengan README Indonesia yang setara. Seluruh instruksi workflow dan template berbahasa Inggris. Instruksi pengguna yang dominan Indonesia menghasilkan diskusi dan dokumen Indonesia; selain itu hasilnya Inggris.
- Dokumentasi produk memakai Markdown secara default. Ikuti format yang diminta pengguna dan konvensi workspace aplikasi.
- Tulis instruksi yang membantu keputusan nyata. Hindari pengulangan, klaim tanpa bukti, dan prosedur yang tidak relevan dengan scope.

## Validasi dan instalasi

- Jalankan `python scripts/validate.py` untuk integritas paket dan referensi lokal.
- Perubahan skill memerlukan `quick_validate.py` dari skill-creator.
- Jika script berubah, jalankan skenario yang terdampak. Installer memiliki `scripts/test-install.ps1` dan `scripts/test-install.py`.
- Perubahan workflow diperiksa melalui skenario representatif; self-review diberi label sesuai metodenya.
- Setelah sumber selesai divalidasi, instal ulang melalui `scripts/install-skill.ps1`. Pertahankan lokasi instalasi yang dipakai, kecuali migrasi diminta.
- Pemeriksaan dokumen tidak membuktikan perilaku agent, keberhasilan CI hosted, atau kesiapan produksi aplikasi.

## Lisensi dan distribusi

Pertahankan GPLv3 dan izin hasil generasi dalam paket. `LICENSE` adalah teks kanonis; `skills/lucky-kit/LICENSE.txt` harus identik. Jangan menambahkan kewajiban branding ke aplikasi pengguna.

Ikuti [panduan kontribusi](CONTRIBUTING.md) dan [kredit](CREDITS.md) saat membawa materi pihak ketiga. Panduan komunitas di root, `.github/`, dan `docs/` tidak dimuat sebagai instruksi skill. Persiapan lokal tidak berarti publikasi atau rilis sudah dilakukan.
