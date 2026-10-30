# 1.manipulasi list
kendaraan = ["motor", "mobil", "sepeda", "bus"]

kendaraan.append("truk")
print(f"kendaraan ditambahkan {kendaraan}")      # untuk menambahkan data

kendaraan.insert(1, "becak")
print(f"kendaraan ditambahkan lagi {kendaraan}") # untuk mwnyisipkan data

kendaraan.remove("bus")
print(f"kendaraan dihapus {kendaraan}")          # untuk menghapus data

kendaraan[2] = "skuter"
print(f"kendaraan diubah {kendaraan}")           # untuk mengubah data

panjang_data = len(kendaraan)
print(f"panjang data kendaraan {panjang_data}\n")# untuk menampilkan panjang data   