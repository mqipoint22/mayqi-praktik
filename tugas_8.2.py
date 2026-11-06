print("2. Manipulasi Dictionary")
print("2.a Buatlah sebuah dictionary bernama data_mahasiswa dengan pasangan key-value berikut:")
print("    - nim: 240101 ")
print("    - nama: Budi Santoso")
print("    - prodi: Teknologi Informasi")

data_mahasiswa = {
    "NIM":"240101",
    "Nama":"Budi Santoso",
    "Prodi":"Teknologi Informasi"
}
print(data_mahasiswa)
print(" ")

print("2.b Ubah nilai prodi menjadi Sastra Mesin sekaligus menambahkan key baru")
print("    angkatan dengan nilai 2026!")

print(f"\tdata sebelum di ganti\t\t: {data_mahasiswa}")
data_mahasiswa.update({"Prodi":"Sastra Mesin"})
print(f"\tdata setelah penggantian\t: {data_mahasiswa}")
print(" ")
print(f"data sebelum di tambah: {data_mahasiswa}")
data_mahasiswa.update({"Angkatan":2026})
print(f"data setelah di tambah: {data_mahasiswa}")
print(" ")

print("2.c Hapus data nim, lalu tampilkan hasil akhir dictionary ke layar!")
print(f"data sebe;um dihapus: {data_mahasiswa}")
del data_mahasiswa["NIM"]
print(f"Hasil akhir dictionary: {data_mahasiswa}")