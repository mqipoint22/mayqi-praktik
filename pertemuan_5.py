print("Program 5.1")   # Perulangan (loop) 
# 1. Tanpa Perulangan (Manual)
angka = 1
print(angka)
angka = angka + 1
print(angka)
angka = angka + 1
print(angka)

# 2. Perulangan dengan List
angka2 = [0, 1, 2, 3, 4]  
print(angka2)

for i in angka2:
    print(i)

# 4. Perulangan dengan Range (Awal, Akhir)
angka4 = range(1, 11)

for i in angka4:
    print(i)
# 5. Perulangan dengan String
data_str = "saya ganteng abiies"
for huruf in data_str:
    print(huruf)



print("Program 5.2 While Loop")
angka = 1
print(f"angka sekarang -> {angka}")

while angka < 5:
    angka += 1  # Sama artinya dengan: angka = angka + 1
    print(f"angka sekarang -> {angka}")
    angka = angka + 1

# Contoh Pass percobaan
print("Program 5.3  Continue and Pass")
angka = 0
while angka < 5:
    angka = angka + 1
    if angka == 3:
        pass  # tidak melakukan apa-apa
    print(angka)

# Contoh Continue
angka = 0
print(f"angka sekarang -> {angka}")
while angka < 5:
    angka = angka + 1
    print(f"angka sekarang -> {angka}")
    if angka == 3:
        print("nice")
        continue  # lompat langsung ke perulangan berikutnya
    print("whasssup")
print("Pinish\n")


print("Program 5.4  break ")
# break  
angka = 0
print(f"aku beri kesempatan ke {angka}")
while angka < 5:
    angka = angka + 1
    print(f"aku beri kesempatan ke {angka}")# aksi 1
    if(angka == 3):
        print("nice")   
        break 
    print("roar") 

print("kita putus") 


print("Program 5.5  Latihan perulangan ")
# 1. Menggunakan For Loop
print("=== 1. Segitiga dengan For Loop ===")
sisi = 4
count = 1

for i in range(sisi):
    print("*" * count)
    count += 1

print("\n")

# 2. Menggunakan While Loop
print("=== 2. Segitiga dengan While Loop ===")
sisi = 10
count = 1

while True:
    print("*" * count)
    count += 1
    if count > sisi:
        break  # Menghentikan perulangan saat count melebihi nilai sisi

print("\nProgram Selesai")




#TUGAS

