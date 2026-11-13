import datetime
import os
import random
import string

# Template dict buku
buku_template = {
    "judul buku": "judul",
    "penulis": "penulis",
    "tahun terbit": 0000,
    "tanggal pinjam": datetime.datetime(1111, 1, 11),
    "status": "TERSEDIA",
}

data_buku = {}

while True:
  # os.system("cls")  # Gunakan "cls" untuk Windows
  os.system("clear")  # Gunakan "clear" untuk Linux/Mac

  print(f"{'SELAMAT DATANG':^25}")
  print(f"{'MANAJEMEN PERPUSTAKAAN':^25}")
  print("-" * 30)

  buku = dict.fromkeys(buku_template.keys())
  buku["judul buku"] = input("Judul Buku        : ")
  buku["penulis"] = input("Penulis Buku      : ")
  buku["tahun terbit"] = int(input("Tahun Terbit      : "))

  print("--- Tanggal Terakhir Pinjam ---")
  T_PINJAM = int(input("Tanggal (1-31)    : "))
  B_PINJAM = int(input("Bulan (1-12)      : "))
  TH_PINJAM = int(input("Tahun (YYYY)      : "))
  buku["tanggal pinjam"] = datetime.datetime(TH_PINJAM, B_PINJAM, T_PINJAM)

  status_pilihan = input("Status Buku (1: Tersedia, 2: Tidak): ")
  if status_pilihan == "1":
    buku["status"] = "TERSEDIA"
  else:
    buku["status"] = "TIDAK"

  # Generate Key Unik untuk Buku (Multi-keys/Nesting key)
  KEY = "".join((random.choice(string.ascii_uppercase) for i in range(5)))
  data_buku.update({KEY: buku})

  # Menampilkan tabel data buku
  print(
      f"\n{'KEYS':<6} {'JUDUL BUKU':<15} {'PENULIS':<12} {'TAHUN':<6}"
      f" {'TGL PINJAM':<12} {'STATUS':<10}"
  )
  print("-" * 70)

  for KEY in data_buku:
    JUDUL = data_buku[KEY]["judul buku"]
    PENULIS = data_buku[KEY]["penulis"]
    TAHUN = data_buku[KEY]["tahun terbit"]
    TGL = data_buku[KEY]["tanggal pinjam"].strftime("%x")
    STATUS = data_buku[KEY]["status"]
    print(f"{KEY:<6} {JUDUL:<15} {PENULIS:<12} {TAHUN:<6} {TGL:<12} {STATUS:<10}")

  print("\n")
  is_done = input("Tambah buku lagi? (y/n): ")
  if is_done.lower() == "n":
    break

print("\nProgram Selesai. Terima kasih!")