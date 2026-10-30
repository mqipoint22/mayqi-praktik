# Program 9.1: Pengenalan dan Pembuatan List

# praktikum setelah uts
# Kumpulan data numbers
data_angka = [1, 5, 2, 3]
print("data_angka:", data_angka)

# Kumpulan data_string
data_string = ["ucup", "adit", "siti"]
print("data_string:", data_string)

# Kumpulan data boolean
data_boolean = [True, False, True, True]
print("data_boolean:", data_boolean)

# Cara alternatif membuat list
data_campuran = [1, "bakwan", 2, "cireng", "ucup", True, "adit", False]
print("data_campuran:", data_campuran)

data_range = range(0, 10, 2)  
print("data_range:", data_range)

data_list = list(data_range)
print("data_list:", data_list)

# Membuat list dengan for loop (List Comprehension)
list_for = [i ** 2 for i in range(0, 10)]
print("list_for:", list_for)

# Membuat list dengan for dan if (mengecualikan angka 5)
list_for_if = [i for i in range(0, 10) if i != 5]
print("list_for_if (i != 5):", list_for_if)

# Membuat list khusus angka genap
list_genap = [i for i in range(0, 10) if i % 2 == 0]
print("list_genap:", list_genap)

# Membuat list khusus angka ganjil
list_ganjil = [i for i in range(0, 10) if i % 2 != 0]
print("list_ganjil:", list_ganjil)





# Program 9.2: Manipulasi List
data = ["Ucup", "Adit", "Dudung"]

# Mengambil data dari list
data_0 = data[0]
print(f"data pertama (index 0) = {data_0}")

data_terakhir = data[-1]
print(f"data terakhir adalah = {data_terakhir}")

# Mengambil info jumlah data dalam list
panjang_data = len(data)
print(f"panjang data = {panjang_data}")

# Menambahkan item pada list sesuai posisi
print(f"data sebelum ditambah = \n{data}")
data.insert(1, "Yanto")
print(f"data sesudah ditambah = \n{data}")

data.append("Ririn")
print(f"data ditambah lagi = \n{data}")

# Menambahkan list dengan list 
data_baru = ["Luffy", "Zoro", "Nami"]
data.extend(data_baru)
print(f"data gabungan = \n{data}")

# Merubah data 
data[2] = "jarwo"
print(f"data rubah = \n{data}")

# Menghapus data tertentu
data.remove("Ucup")
print(f"data hapus = \n{data}")

# Menghapus data paling belakang menggunakan pop
data.pop()
print(f"data akhir = \n{data}")





# Program 9.3: Operasi List 
data_angka_ops = [1, 5, 1, 4, 3, 2, 4, 3, 2, 3, 7, 8, 9, 0]
print(f"data angka = \n{data_angka_ops}")

# Menghitung kemunculan data 
jumlah_data_4 = data_angka_ops.count(4)
jumlah_data_3 = data_angka_ops.count(3)
print(f"jumlah angka 4 = {jumlah_data_4}")
print(f"jumlah angka 3 = {jumlah_data_3}")

# Mengambil posisi data 
data_nama = ["Rendi", "Iqbal", "Gana", "Khairil"]
print(f"data = {data_nama}")
index_Iqbal = data_nama.index("Iqbal")
index_Gana = data_nama.index("Gana")
print(f"index si Iqbal = {index_Iqbal}")
print(f"index si Gana = {index_Gana}")

# Mengurutkan list
print(f"data angka sebelum sort = \n{data_angka_ops}")
data_angka_ops.sort()
print(f"data angka sort = \n{data_angka_ops}")

print(f"data nama sebelum sort = {data_nama}")
data_nama.sort()
print(f"data nama sort = {data_nama}")

# Membalik urutan list 
data_angka_ops.reverse()
data_nama.reverse()
print(f"data angka di reverse: \n{data_angka_ops}")
print(f"data nama di reverse: \n{data_nama}")





# Program 9.4: Nested List
data_0 = [1, 2]
data_1 = [3, 4]
data_list_biasa = [1, 2, 3, 4]
print(f"list biasa = {data_list_biasa}")

list_2D = [data_0, data_1, 6, 7]
print(f"list 2D = {list_2D}")

# Contoh penggunaan nested list untuk data peserta
peserta_0 = ["Wowok", 25, "Laki-laki"]
peserta_1 = ["Rusdi", 23, "Laki-laki"]
peserta_2 = ["Sri", 50, "Wanita"]

list_peserta = [peserta_0, peserta_1, peserta_2]
print(f"peserta = {list_peserta}")

for peserta in list_peserta:
    print(f"nama\t : {peserta[0]}")
    print(f"umur\t : {peserta[1]}")
    print(f"Gender\t : {peserta[2]}\n")