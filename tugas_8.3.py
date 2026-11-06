# a. Membuat dictionary 'keranjang'
keranjang = {"apel": 5000, "pisang": 3000, "jeruk": 7000, "anggur": 15000}

# Menyiapkan variabel untuk menghitung total belanja
total_belanja = 0

# b. Perulangan untuk menampilkan setiap barang dan harganya
for buah, harga in keranjang.items():
    print(f"Harga {buah}: Rp {harga}")
    total_belanja += harga  # Menjumlahkan total belanja

# c. Menampilkan total belanja
print(f"Total belanja: Rp {total_belanja}")