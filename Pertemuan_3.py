#operasi aritmatika

a = 10
b = 5

# operasi penjumlahan +
hasil = a + b
print(a, "+", b, "=", hasil)

# operasi pengurangan -
hasil = a - b
print(a, "-", b, "=", hasil)

# operasi perkalian *
hasil = a * b
print(a, "*", b, "=", hasil)

# operasi pembagian /
hasil = a / b
print(a, "/", b, "=", hasil)

# operasi modulus %
hasil = a % b
print(a, "%", b, "=", hasil)        #modulus (%)adalah sisa hasil bagi 

# operasi eksponen (pangkat) **
hasil = a ** b
print(a, "**", b, "=", hasil)       #untuk memangkaatkan angka

# operasi floor division //
hasil = a // b
print(a, "//", b, "=", hasil)       #untuk membagi angka




# latihan konversi satuan temperature  
# # program konversi celcius ke satuan lain 

print("\nPROGRAM KONVERSI TEMPERATUR\n")                                            #memperjelas sebuah program yang sedang dibuat 

celcius = float(input("Masukan suhu dalam celcius : "))                             #memasukkan suhu dalam celcius, sebagai penentu suhu dari awal (celcius - kelvin)     
print("suhu adalah", celcius, "Celcius")                                            #Sebagai penerang (penjelas) / kalimat bawaan 

# reamur
reamur = (4/5) * celcius                                                            #(4/5)* adalah tanda untuk mengalikan dengan hasil celcius yang telah kita masukkan 
print("Suhu dalam reamur adalah ", reamur, "Reamur")                                

# fahrenheit
fahrenheit = ((9/5) * celcius) + 32                                                 #tanda + 32 adalah hasil dari perkalian per( mengubah fahrenheit) lalu ditambah 32 sebagai hasil
print("Suhu dalam fahrenheit adalah ", fahrenheit, "Fahrenheit")

# kelvin
kelvin = celcius + 273                                                              #tanda + 273 adalah hasil dari perkalian per( mengubah kelvin) lalu ditambah 273 sebagai hasil   
print("Suhu dalam kelvin adalah ", kelvin, "Kelvin")



a = 10
b = 5

hasil = a > b
print(a, ">", b, "=", hasil)           #apakah nilai tersebut lebih besar

hasil = a < b
print(a, "<", b, "=", hasil)           #apakah nilai tersebut lebih kecil

hasil = a >= b
print(a, ">=", b, "=", hasil)          #apakaah nilai tersebut lebih besar sama dengan  

hasil = a <= b
print(a, "<=", b, "=", hasil)          #apakah nilai tersebut lebih kecil sama dengan 

hasil = a == b
print(a, "==", b, "=", hasil)          #apakah nilai tersebut sebanding atau tidak

hasil = a != b
print(a, "!=", b, "=", hasil)          #apakah nilai tersebuat sama


# latihan konversi

panjang = 12
lebar = 5
tinggi = 8

# a
luas = panjang * lebar
volume = luas * tinggi
keliling = 2 * (panjang + lebar + tinggi)

print("luas = ", luas)
print("volume = ", volume)
print("keliling = ", keliling)

# b
hasil = luas > 50
print(luas, ">", 50, "=", hasil)

# c
hasil = volume == 480
print(volume, "==", 480, "=", hasil)