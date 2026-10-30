# 2.operasi list
angka = [75,80,90,75,85,100,65]

index_100 = angka.index(100)
print(f"index angka 100 adalah {index_100}")    # untuk menampilkan index

jumlah_angka_75 = angka.count(75)
print(f"jumlah angka 75 adalah {jumlah_angka_75}")  # untuk menampilkan jumlah

angka.sort()
print(f"angka diurutkan {angka}")                # untuk pengurutan dari terkecil ke terbesar

angka.sort(reverse=True)
print(f"angka diurutkan {angka}\n")               # untuk pengrutan dari besar ke kecil                         

