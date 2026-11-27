##PROGRAM 13.1
##FUNGSI DENGAN VARIABEL GLOBAL DAN LOKAL

#akses variabel global dalam fungsi
def fungsi():
    nama_global = "Jeni" 
    print(f"fungsi menampilkan {nama_global}") # <- variabel global
fungsi()
print("\n")


##PROGRAM 13.2
##MERUBAH VARIABEL GLOBAL DI DALAM FUNGSI
angka = 0
def ubah_angka(nilai_baru):
    global angka  # fungsi ini mnedapat akses merubah angka
    angka = nilai_baru

print(f"angka sebelum dirubah: {angka}")
ubah_angka(10)
print(f"angka setelah dirubah: {angka}")
print("\n")


##PROGRAM 13.3
##PENJEBAKAN EKSEPSI
input_user = int(input("masukkan angka: "))
hasil = 0



# percobaan try & except
try:
    hasil = 10/input_user
except:
    print("input tidak boleh 0")
    
print(f"hasil = {hasil}")

