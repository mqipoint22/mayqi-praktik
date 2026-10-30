# 4.mengambil data dari list
# Tampilan harga item denganmemanggil indeks baris dan kolom yang spesifik dari list tersebut
data_barang = [["buku", 5000], ["pensil", 2000], ["pulpen", 3000]]

harga_pensil = data_barang[1][1]
print(f"harga pensil adalah {harga_pensil}")

for barang in data_barang:                      # untuk tampilan output data satu per satu
    print(f"nama\t : {barang[0]}")
    print(f"harga\t : {barang[1]}\n")