# 📦 Sistem Navigasi Logistik Drone Otomatis (CLI App)

Aplikasi terminal Python sederhana untuk mengelola data pengiriman menggunakan konsep struktural seperti array, pencarian (binary & linear search), dan update status secara berurutan.

---

## 🔧 Fitur Utama

- ✅ Tambah data pengiriman dengan ID otomatis
- 🔍 Cari ID pengiriman menggunakan **Binary Search**
- 🔎 (Disiapkan) Pencarian ID menggunakan **Linear Search** (opsional)
- 🗂️ Filter data berdasarkan prioritas
- 🔁 Perbarui status pengiriman secara siklik (Belum → Dalam Perjalanan → Selesai → ...)
- 📋 Tampilkan seluruh data pengiriman
- ❌ Keluar dari aplikasi

---

## 🧠 Format Data

Setiap pengiriman disimpan dalam bentuk list 4 elemen:

```python
[id_pengiriman, prioritas, waktu_estimasi, status]

#contoh
[1023, 2, 30, "Belum"]
```

---

## 🚀 Cara Menjalankan
```bash
git clone https://github.com/PrayaaDikk/sistem-navigasi-logistik-drone-otomatis.git
cd sistem-navigasi-logistik-drone-otomatis
```

### Lalu jalankan
```bash
python main.py
```

## 📚 Contoh Output CLI
```bash
=== Menu Pengiriman ===
1. Tambah data pengiriman
2. Cari ID pengiriman
3. Tampilkan data pengiriman berdasarkan prioritas
4. Perbarui status pengiriman
5. Tampilkan semua data pengiriman
6. Keluar
Masukkan pilihan:
```

---
