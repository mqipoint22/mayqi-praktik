#tugas nih ye

print("Buatlah program dengan input dan fungsi untuk menghitung:")
print("\ta. Luas persegi panjang")
print("\tb. Volume persegi panjang")
print("\tc. Luas Lingkaran")
print("\td. Volume Bola")
print(" ")

#a. Luas persegi panjang
print("a. Luas persegi panjang:")
def luas_persegi_panjang(panjang, lebar):
    hasil = (panjang * lebar)
    return hasil
print(f"Luas persegi panjang = {luas_persegi_panjang(10, 5)}")
print(" ")

#b. Volume persegi panjang
print("Volume persegi panjang:")
def volume_persegi_panjang(panjang, lebar, tinggi):
    hasil = (panjang * lebar * tinggi)
    return hasil
print(f"Volume persegi panjang = {volume_persegi_panjang(10, 5, 2)}")
print(" ")

#c. Luas lingkaran
print("Luas lingkaran:")
def luas_lingkaran(jari_jari):
    hasil = 3.14 * (jari_jari ** 2)
    return hasil
print(f"Luas lingkaran = {luas_lingkaran(24)}")
print(" ")

#d. Volume bola
print("Volume bola:")
def volume_bola(jari_jari):
    hasil = (4/3) * 3.14 * (jari_jari ** 3)
    return hasil
print(f"Volume bola = {volume_bola(20)}")