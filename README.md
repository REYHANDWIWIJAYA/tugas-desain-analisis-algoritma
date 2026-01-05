# 0/1 Knapsack Problem dengan Dynamic Programming  
## Optimasi Muatan Carrier Pendakian

Repository ini berisi implementasi **algoritma 0/1 Knapsack Problem** menggunakan metode **Dynamic Programming** untuk menyelesaikan permasalahan optimasi pemilihan barang pada carrier pendakian dengan kapasitas terbatas.

---

## 📌 Deskripsi Masalah
Dalam kegiatan pendakian, kapasitas carrier sangat terbatas sehingga tidak semua barang dapat dibawa. Setiap barang memiliki:
- Berat (weight)
- Nilai kepentingan (value)

Tujuan dari permasalahan ini adalah **memilih kombinasi barang dengan nilai kepentingan maksimum tanpa melebihi kapasitas carrier**.

Pada kasus ini:
- **Kapasitas carrier**: 8 kg  
- **Jumlah item**: 10 barang  
- **Metode**: 0/1 Knapsack dengan Dynamic Programming  

---

## 📦 Data Barang

| No | Nama Item | Berat (kg) | Nilai |
|----|----------|------------|-------|
| 1 | Tenda | 4.0 | 10 |
| 2 | Sleeping Bag | 1.5 | 9 |
| 3 | Jaket Gunung | 1.0 | 8 |
| 4 | Matras | 1.0 | 7 |
| 5 | Kompor Portable | 1.0 | 7 |
| 6 | Headlamp | 0.3 | 6 |
| 7 | Kotak P3K | 0.7 | 8 |
| 8 | Jas Hujan | 0.8 | 6 |
| 9 | Peralatan Makan | 0.7 | 5 |
| 10 | Makanan Instan | 3.0 | 9 |

---

## ⚙️ Metode Penyelesaian
Algoritma **Dynamic Programming** digunakan karena:
- Menjamin solusi optimal
- Menghindari perhitungan berulang (overlapping subproblems)
- Lebih efisien dibandingkan brute force

Kompleksitas waktu:
- **Dynamic Programming**: O(n × W)
- **Brute Force**: O(2ⁿ)

---

## 🧠 State Space Tree
State Space Tree digunakan untuk memvisualisasikan seluruh kemungkinan keputusan pengambilan item (include/exclude).  
Pruning dilakukan jika total berat melebihi kapasitas carrier, sehingga cabang tersebut tidak dilanjutkan.

---

## 🧪 Hasil Implementasi

**Output Program:**
- Nilai maksimum: **56**
- Total berat: **7.0 kg**
- Sisa kapasitas: **1.0 kg**

**Item Terpilih:**
- Sleeping Bag  
- Jaket Gunung  
- Matras  
- Kompor Portable  
- Headlamp  
- Kotak P3K  
- Jas Hujan  
- Peralatan Makan  

---

## ▶️ Cara Menjalankan Program

1. Pastikan Python sudah terinstal
2. Clone repository ini:
   ```bash
   git clone https://github.com/username/knapsack-dynamic-programming.git
