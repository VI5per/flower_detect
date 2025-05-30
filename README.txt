# 🌸 Flower Detection using YOLOv8

**flower_detect** adalah program pendeteksi objek bunga berbasis model deep learning **YOLOv8**. Program ini berjalan melalui skrip Python dan menggunakan model hasil pelatihan dalam format `.pt`. Tanpa perlu antarmuka grafis atau library tambahan, cukup jalankan melalui terminal/command prompt.

---

## 📂 Struktur Proyek

flower_detect/
├── flower_detect.py # Script utama untuk menjalankan deteksi
├── flower_detect.pt # Model YOLOv8 terlatih untuk bunga
├── image.jpg # Gambar yang akan dideteksi (contoh)
└── README.md # 

###  Catatan Penting (NOTE)
🔹 Pastikan gambar yang ingin dideteksi sudah diunduh dan disimpan di direktori yang sama dengan file flower_detect.py.
🔹 Ganti atau sesuaikan nama file gambar (misalnya image.jpg) di dalam kode flower_detect.py agar sesuai dengan nama file gambar yang ingin kamu deteksi.
 
image_path = r'(ganti sesuai tempat directori file)(nama_gambar_yg_dideteksi.jpg)']

####
🛠️ Program ini masih dalam tahap pengembangan.

Untuk saat ini, fungsinya hanya terbatas pada mendeteksi objek bunga di dalam gambar. Program belum mendukung penyimpanan data deteksi ke database, pengolahan lanjutan, atau integrasi sistem lain.

Fitur-fitur tambahan sedang dalam proses pengembangan dan akan ditambahkan di versi selanjutnya.