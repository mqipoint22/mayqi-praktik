# {Program 4.1 Logical}
# Operasi logika atau boolean: not, or, and, xor

# === NOT ===
print('===NOT===')
a = True
c = not a
print('data a =', a)
print('------------ NOT')
print('data c =', c)

print() # Baris kosong untuk pemisah

# program OR dimana hanya dibutuhkan salah satu benar/True saja untuk True
# (jika salah satu true, maka hasilnya adalah true)
print('===OR===')
a = False
b = False
c = a or b
print(a)

a = False
b = True
c = a or b
print(a)

# program and, akan bernilai benar ketika semua terpenuhi atau True 
# (jika dua buah nilai true, maka hasil true)
print('===AND===')
a = True
b = True
c = a and b
print(c)

a = False
b = True
c = a and b
print(c)

# program Xor, hanya akan bernilai benar ketika salah satu benar 
# (akan true jika salah satu true, sisanya false)
print('===XOR===')
a = False
b = True
c = a ^ b
print(c)

a = False
b = True
c = a ^ b
print(a)


#{Program 4.2 logika dan komparasi}
#Latihan logika dan komperasi
#program untuk mengecek bilangan < 3 / >10
#++++++++++ 3 ---------- 10 +++++++++++

angka = int(input("masukkan angka: "))
iskurangdari = angka < 3
islebihdari = angka > 10
hasil = iskurangdari or islebihdari
print(hasil)
angka = int(input("masukkan angka: "))
iskurangdari = angka < 10
islebihdari = angka > 3
hasil = iskurangdari and islebihdari
print(hasil) 


#{Program 4.3  IF and ELSE }
#if dan else statement
#1. if nya
#2. kondisinya(syarat)
#3. aksi
#program Riski BISA
#program if inline
nama = input("masukkan nama: ")
if nama == "mayqi" : print("bisa")
#program if indentation
if nama == "mayqi":
    print("HEBAT!!")
    print("BISA!!")
print("akhir dari program")
#else statement
if nama == "mayqi":
    print("HEBAT!!")
else:
    print("BISA!!!")

#ELIF = else if statement
nama = input("masukkan nama: ")
# if kondisi: 
        #aksi true 
# elif kondisi: 
        # aksi true 
# elif kondisi: 
        # aksi true 
# else: 
        #aksi
if nama == "mayqi":
    print("ini dia yang gw cari!")
elif nama == "messi":
    print("Overrated")
elif nama == "kian":
    print("proplayer")
else:
    print("user not found")
print("end")

#{Program 4.4  ELIF Statement}
 # OR (jika salah satu true, maka hasilnya adalah true) 
print("===OR===")
a = True
b = True
c = a or b
print(c) 
nama = input("Siapa nama anda?")
if   nama == "mayqi": 
    print("hai raden paling bagus dewe!!!") #aksi true 1
elif nama == "ronaldo": 
    print("lu GOAT sepak bola!!!") #aksi true 2
elif nama == "leo": 
    print("sok asik!!!") #aksi true 3
else: 
    print("apasih iuh!!!") #aksi false
print("akhir dari program") 
