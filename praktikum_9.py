
#Program 11.1 Multi keys & Nesting Dictionary 
import datetime

# Data mahasiswa 1
mahasiswa1 = {
    'nama': 'Cristiano Ronaldo',
    'nim': '19022001',
    'sks lulus': 130,
    'beasiswa': False,
    'lahir': datetime.datetime(2001, 4, 10)  # tahun, tanggal, bulan
}

# Data mahasiswa 2
mahasiswa2 = {
    'nama': 'Federico Falverde',
    'nim': '19022002',
    'sks lulus': 140,
    'beasiswa': True,
    'lahir': datetime.datetime(2002, 10, 10)
}

# Data mahasiswa 3
mahasiswa3 = {
    'nama': 'Harry Kane',
    'nim': '19022003',
    'sks lulus': 100,
    'beasiswa': True,
    'lahir': datetime.datetime(1977, 5, 10)
}

# Nesting Dictionary (Dictionary di dalam Dictionary)
data_mahasiswa = {
    'MAH001': mahasiswa1,
    'MAH002': mahasiswa2,
    'MAH003': mahasiswa3,
}

# Menampilkan Header Tabel
print(f"{'KEY':<6} {'Nama':<20} {'SKS':<5} {'Beasiswa':<9} {'Lahir':<10}")
print("-"*55)

# Looping untuk menampilkan data dari nested dictionary
for KEY in data_mahasiswa:
    NAMA = data_mahasiswa[KEY]['nama']
    SKS = data_mahasiswa[KEY]['sks lulus']
    BEASISWA = str(data_mahasiswa[KEY]['beasiswa'])
    LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%d-%m-%Y")
    
    print(f"{KEY:<6} {NAMA:<20} {SKS:<5} {BEASISWA:<9} {LAHIR:<10}")




### **Program 11.2: Input Data Mahasiswa Menggunakan Template**

import datetime

# Template dictionary dasar
mahasiswa_template = {
    'nama': 'nama',
    'nim': '00000000',
    'sks_lulus': 0,
    'lahir': datetime.datetime(1111, 1, 11)
}

print(f"{'SELAMAT DATANG':^20}")
print(f"{'DATA MAHASISWA':^20}")
print("-" * 20)

# Membuat dictionary mahasiswa baru berdasarkan template
mahasiswa = dict.fromkeys(mahasiswa_template.keys())
print("Template awal:", mahasiswa)

# Memasukkan data dari input pengguna
mahasiswa['nama'] = input("Nama Mahasiswa: ")
mahasiswa['nim'] = input("NIM Mahasiswa: ")
mahasiswa['sks_lulus'] = int(input("SKS Lulus: "))

TAHUN_LAHIR = int(input("Tahun lahir (YYYY): "))
BULAN_LAHIR = int(input("Bulan lahir (1-12): "))
TANGGAL_LAHIR = int(input("Tanggal lahir (1-31): "))

mahasiswa['lahir'] = datetime.datetime(TAHUN_LAHIR, BULAN_LAHIR, TANGGAL_LAHIR)

print("\nHasil Input Data Mahasiswa:")
print(mahasiswa)




# Program 11.3: Program Interaktif Dynamic Nesting Dictionary

import datetime
import os
import string
import random

# Template dict mahasiswa
mahasiswa_template = {
    'nama': 'nama',
    'nim': '00000000',
    'sks lulus': 0,
    'lahir': datetime.datetime(1111, 1, 11)
}

data_mahasiswa = {}

while True:
    # Membersihkan layar terminal (gunakan 'cls' untuk Windows, 'clear' untuk Mac/Linux)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print(f"{'SELAMAT DATANG':^20}")
    print(f"{'DATA MAHASISWA':^20}")
    print("-" * 20)
    
    mahasiswa = dict.fromkeys(mahasiswa_template.keys())
    
    mahasiswa['nama'] = input("Nama Mahasiswa: ")
    mahasiswa['nim'] = input("NIM Mahasiswa: ")
    mahasiswa['sks lulus'] = int(input("SKS Lulus: "))
    
    TAHUN_LAHIR = int(input("Tahun lahir (YYYY): "))
    BULAN_LAHIR = int(input("Bulan lahir (1-12): "))
    TANGGAL_LAHIR = int(input("Tanggal lahir (1-31): "))
    
    mahasiswa['lahir'] = datetime.datetime(TAHUN_LAHIR, BULAN_LAHIR, TANGGAL_LAHIR)
    
    # Generate Key acak sepanjang 6 karakter huruf kapital
    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
    data_mahasiswa.update({KEY: mahasiswa})
    
    # Menampilkan tabel data mahasiswa
    print(f"\n{'KEY':<6} {'Nama':<17} {'NIM':<8} {'SKS Lulus':<10} {'Tanggal Lahir':<13}")
    print('-' * 60)
    
    for KEY in data_mahasiswa:
        NAMA = data_mahasiswa[KEY]['nama']
        NIM = data_mahasiswa[KEY]['nim']
        SKS = str(data_mahasiswa[KEY]['sks lulus'])
        LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%d/%m/%Y")
        
        print(f"{KEY:<6} {NAMA:<17} {NIM:<8} {SKS:^10} {LAHIR:^13}")
        
    print("\n")
    is_done = input("Mau tambah lagi bro (y/n)? ")
    if is_done.lower() == "n":
        break

print("\nAkhir dari program, terima kasih")
