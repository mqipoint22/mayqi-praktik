print("1.a Buatlah sebuah tuple bernama mahasiswa yang berisi 3 data diri Anda:(Nama, NIM, Prodi)!")
Mahasiswa = ("Muhammad Mayqi Irfansyah", "2605060043", "Teknologi Informasi")
print(f"Nama\t:\t {Mahasiswa[0]}")
print(f"NIM\t\t:\t {Mahasiswa[1]}")
print(f"Prodi\t:\t {Mahasiswa[2]}")
print(" ")

print("1.b Tampilkan data NIM dan Prodi ke layar dengan cara mengakses indeksnya!")
print(f"Data Mahasiswa :\t {Mahasiswa}")
print(f"NIM\t\t:\t {Mahasiswa[1]}")
print(f"Prodi\t:\t {Mahasiswa[2]}")
print(" ")

print("1.c Coba jalankan kode mahasiswa[2] = Teknologi Informasi. Amati pesan error yang muncul, lalu jelaskan mengapa hal tersebut terjadi!")
# Mahasiswa[2] = "Teknologi Informasi"
# File "c:\Users\user\Desktop\mfjr_VSC_smstr.1\mfjr_tugas_10.py", line 16, in <module>
#     Mahasiswa[2] = "Teknologi Informasi"
#     ~~~^^^
# TypeError: 'tuple' object does not support item assignment

#Eror tersebut terjadi dikarenakan data Mahasiswa berjenis tuple yang bersifat(imuttable) atau tidak dapat diubah
print(" ")

print("1.d Buatlah sebuah Set bernama nilai_angka dari barisan angka berikut: 10, 4, 3, 2, 4, 10, 7, 5. Cetak nilai_angka ke layar dan jelaskan apa yang terjadi pada angka 10 dan 4 yang ditulis dua kali!")
data_sets = {10,4,3,2,4,10}
print(f"angka:\n {data_sets}")
# {2, 10, 3, 4}
# bisa dilihat pada output nya bahwa angka 4 dan 10 hanya muncul sekali karena pada data sets output yang ditampilkan akan diurutkan dan hanya ditampilkan satu kali per elemen