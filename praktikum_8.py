#Program 10.1 Tuples dan sets
#List
#menggunakan kurung siku
data_list = [10, 2, 4, 3, 2]        # sifatnya berurutan, namun dapat dirubah
print("Data List:", data_list) 

#Tuples
data_tuples = (7, 8, 10, 11)
print("Data Tuples:", data_tuples)
print("Elemen indeks ke-1 pada Tuples:", data_tuples[1])

#Sets
data_sets = {10, 4, 3, 2, 7, 6, 5}
print("Data Sets:", data_sets)

# Program 10.2: Dictionary 
# 1. List
data_list = ['ucup', 'rendi', 'salsa']
print("Akses List indeks ke-0:", data_list[0])
# 2. Dictionary
data_dict = {
    'key': 'value',
    'cp': 'ucup',
    'rd': 'rendi',
    'sl': 'salsa',
    'nmbr': 100,
    'list': data_list
}
print("Akses dictionary key 'cp':", data_dict['cp'])
print("Akses dictionary key 'nmbr':", data_dict['nmbr'])
print("Akses dictionary key 'list':", data_dict['list'])

#Pada List, kita menggunakan elemen menggunakan indeks angka, contohnya: ( 0, 1, 2).
#Sedangkan pada Dictionary, kita menggunakan elemen menggunakan key atau kata kunci
#yang berupa teks atau string contohnya: ('cp', 'nmbr').


#Program 10.3 Operasi Dictionary 
#OPERASI DICTIONARY
data_dict = {
    "cup":"ucup surucup",
    "pet":"opet saripet",
    "ndo":"nando surando"
}

#Panjang Dictionary
LENDICT = len(data_dict)
print(f"PANJANG DICTIONARY: {LENDICT}")

#Mengecek key exist atau tidak
KEY = "cup"
CHECKKEY = KEY in data_dict
print(f"apakah {KEY} ada di data_dict: {CHECKKEY}")

#Mengakses value (read) dengan get
print(data_dict["cup"])
print(data_dict.get("cup"))
print(data_dict.get("kis","key tidak ditemukan")) #check key dengan massage

#Mengupdate data
data_dict["cup"] = "ucup si ganteng"
print(data_dict)
data_dict["de"] = "ade si adik"
print(data_dict)

data_dict.update({"cup":"ucup surucup"})
print(data_dict)
data_dict.update({"iwn":"iwan mang keren"}) #akan di tambah jika belum ada key
print(data_dict)

#Menghapus data
del data_dict["iwn"]
print(data_dict)

#Program 10.4 Looping Dictionary 
# Program Looping Dictionary

ijazah_ijazah = {
    "owi": "jokokowi",
    "roy": "roy suryo",  # Menambahkan koma yang kurang
    "lur": "lur sedulur",
    "wel": "bung towel"
}

# 1. Looping pertama 
# for inisialisasi in dict
#   print (inisialisasi)
print("--- 1. Looping Key secara Langsung ---")
for ijazah in ijazah_ijazah:
    print(ijazah)

for key, value in ijazah_ijazah.items():
    print(f"key : {key} => value : {value}")

#
# 
# 
# 
# # Looping Dictionary - Data Mahasiswa Universitas Tidar

# Membuat dictionary dengan data Universitas Tidar
data_mahasiswa = {
    "nama": "Seto tembak",
    "prodi": "Teknologi Informasi",
    "fakultas": "Teknik",
    "semester": 3,
    "biaya_ukt": 100000
}

# 1. Looping biasa (hanya mengambil key)
print("=== 1. Looping Key ===")
for key in data_mahasiswa:
    print(key)

print("\n=== 2. Looping Keys menggunakan .keys() ===")
keys = data_mahasiswa.keys()
print(keys)
for key in data_mahasiswa.keys():
    print(data_mahasiswa.get(key))

print("\n=== 3. Looping Values menggunakan .values() ===")
values = data_mahasiswa.values()
print(values)
for value in data_mahasiswa.values():
    print(value)

print("\n=== 4. Looping Items (Key dan Value) menggunakan .items() ===")
items = data_mahasiswa.items()
print(items)

# Menampilkan tuple (key, value)
for item in data_mahasiswa.items():
    print(item)

# Menampilkan key dan value dengan format f-string yang rapi
print("\n--- Format Output Data Universitas Tidar ---")
for key, value in data_mahasiswa.items():
    print(f"Key: {key:<12} | Value: {value}")

