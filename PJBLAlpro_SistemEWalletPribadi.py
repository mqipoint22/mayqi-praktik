#1. INISIALISASI STRUKTUR DATA (DICTIONARY)
# Dictionary utama untuk menyimpan seluruh state keuangan

data_keuangan = {
    "saldo": 0.0,
    "daftar_transaksi": [],  # List dictionary untuk riwayat transaksi
    "anggaran": {}           # Dictionary untuk mapping: {kategori: batas_nominal}
}

# 2. FUNGSI-FUNGSI SISTEM (FUNCTIONS)

def catat_pemasukan(data, kategori, nominal, catatan):
    """Mencatat pemasukan uang dan menambah saldo."""
    # percabangan if-elif-else untuk validasi input
    if nominal <= 0:
        print("[GAGAL] Nominal pemasukan harus lebih besar dari Rp 0!")
        return False
    elif not kategori.strip():
        print("[GAGAL] Kategori tidak boleh kosong!")
        return False
    else:
        data["saldo"] += nominal # update saldo pada dictionary

        # buat dictionary transaksi baru
        transaksi_baru = {
            "id": len(data["daftar_transaksi"]) + 1,
            "jenis": "PEMASUKAN",
            "kategori": kategori.strip(),
            "nominal": nominal,
            "catatan": catatan
        }

        data["daftar_transaksi"].append(transaksi_baru) # simpan ke dalam list transaksi
        print(f"[SUKSES] Pemasukan sebesar Rp {nominal:,.2f} berhasil dicatat.")
        return True


def catat_pengeluaran(data, kategori, nominal, catatan):
    """Mencatat pengeluaran, mengurangi saldo, dan memicu evaluasi anggaran."""
    # percabangan if-elif-else untuk aturan saldo dan validasi nominal
    if nominal <= 0:
        print("[GAGAL] Nominal pengeluaran harus lebih besar dari Rp 0!")
        return False
    elif nominal > data["saldo"]:
        print(f"[GAGAL] Saldo tidak mencukupi! Saldo saat ini: Rp {data['saldo']:,.2f}")
        return False
    else:
        data["saldo"] -= nominal # kurangi saldo

        # buat dictionary transaksi baru
        transaksi_baru = {
            "id": len(data["daftar_transaksi"]) + 1,
            "jenis": "PENGELUARAN",
            "kategori": kategori.strip(),
            "nominal": nominal,
            "catatan": catatan
        }

        # Simpan ke list
        data["daftar_transaksi"].append(transaksi_baru)
        print(f"[SUKSES] Pengeluaran dicatat. Sisa saldo saat ini: Rp {data['saldo']:,.2f}")

        evaluasi_anggaran(data, kategori.strip()) # panggil fungsi evaluasi batas anggaran
        return True

def atur_anggaran(data, kategori, batas_nominal):
    """Menetapkan batas pengeluaran untuk kategori tertentu."""
    if batas_nominal <= 0:
        print("[GAGAL] Batas nominal anggaran harus lebih dari Rp 0!")
    elif not kategori.strip():
        print("[GAGAL] Nama kategori tidak boleh kosong!")
    else:
        data["anggaran"][kategori.strip()] = batas_nominal # Simpan batas anggaran ke dalam dictionary
        print(f"[SUKSES] Anggaran kategori '{kategori.strip()}' ditetapkan: Rp {batas_nominal:,.2f}")

def evaluasi_anggaran(data, kategori):
    """Mengevaluasi pemakaian anggaran kategori dengan aturan if-elif-else."""
    # Cek apakah kategori ada di dictionary anggaran
    if kategori not in data["anggaran"]:
        return
    batas = data["anggaran"][kategori]
    total_terpakai = 0.0

    # perulangan for untuk menjumlahkan pengeluaran pada kategori ini
    for trx in data["daftar_transaksi"]:
        if trx["jenis"] == "PENGELUARAN" and trx["kategori"].lower() == kategori.lower():
            total_terpakai += trx["nominal"]

    persentase = (total_terpakai / batas) * 100

    # percabangan if-elif-else untuk aturan batas peringatan anggaran
    if persentase > 100:
        print(f"\n>> [PERINGATAN BAHAYA] Pengeluaran '{kategori}' MELEBIHI ANGGARAN!")
        print(f">> Terpakai: Rp {total_terpakai:,.2f} dari Rp {batas:,.2f} ({persentase:.1f}%)\n")
    elif persentase >= 80:
        print(f"\n>> [PERINGATAN WASPADA] Pengeluaran '{kategori}' mendekati batas!")
        print(f">> Terpakai: Rp {total_terpakai:,.2f} dari Rp {batas:,.2f} ({persentase:.1f}%)\n")
    else:
        print(f">> [INFO] Anggaran '{kategori}' aman. Terpakai: {persentase:.1f}%\n")


def tampilkan_ringkasan(data):
    """Menghitung dan menampilkan total pemasukan, pengeluaran, dan net cash flow."""
    total_masuk = 0.0
    total_keluar = 0.0

    # Perulangan for untuk data dari list transaksi
    for trx in data["daftar_transaksi"]:
        if trx["jenis"] == "PEMASUKAN":
            total_masuk += trx["nominal"]
        elif trx["jenis"] == "PENGELUARAN":
            total_keluar += trx["nominal"]

    cash_flow = total_masuk - total_keluar

    print("\n" + "=" * 45)
    print("             RINGKASAN KEUANGAN              ")
    print("=" * 45)
    print(f" Saldo Saat Ini          : Rp {data['saldo']:>15,.2f}")
    print(f" Total Seluruh Pemasukan : Rp {total_masuk:>15,.2f}")
    print(f" Total Pengeluaran       : Rp {total_keluar:>15,.2f}")
    print("-" * 45)
    print(f" Cash Flow Bersih        : Rp {cash_flow:>15,.2f}")
    print("=" * 45)


def tampilkan_riwayat(data):
    """Menampilkan seluruh isi list transaksi."""
    print("\n" + "=" * 60)
    print("                    RIWAYAT TRANSAKSI                       ")
    print("=" * 60)

    if not data["daftar_transaksi"]:
        print(" [Belum ada transaksi yang tercatat]")
    else:
        for trx in data["daftar_transaksi"]:
            print(f" ID: {trx['id']:<3} | {trx['jenis']:<11} | "
                  f"Kat: {trx['kategori']:<12} | "
                  f"Rp {trx['nominal']:>12,.2f} | Ket: {trx['catatan']}")
    print("=" * 60)



# 3. MENU UTAMA MENGGUNAKAN WHILE LOOP & PERCABANGAN

def main():
    program_berjalan = True

    # Perulangan WHILE agar program terus berjalan sampai pengguna keluar
    while program_berjalan:
        print("\n=== SISTEM MANAJEMEN KEUANGAN PRIBADI ===")
        print("1. Catat Pemasukan")
        print("2. Catat Pengeluaran")
        print("3. Atur Batas Anggaran")
        print("4. Tampilkan Ringkasan Finansial")
        print("5. Tampilkan Riwayat Transaksi")
        print("6. Keluar Program")
        
        pilihan = input("Pilih menu (1-6): ").strip()

        # Percabangan IF-ELIF-ELSE untuk navigasi menu
        if pilihan == "1":
            try:
                kategori = input("Masukkan Kategori (misal: Gaji, Bonus): ")
                nominal = float(input("Masukkan Nominal (Rp): "))
                catatan = input("Catatan tambahan: ")
                catat_pemasukan(data_keuangan, kategori, nominal, catatan)
            except ValueError:
                print("[ERROR] Masukkan angka yang valid untuk nominal!")

        elif pilihan == "2":
            try:
                kategori = input("Masukkan Kategori (misal: Makan, Transport): ")
                nominal = float(input("Masukkan Nominal (Rp): "))
                catatan = input("Catatan tambahan: ")
                catat_pengeluaran(data_keuangan, kategori, nominal, catatan)
            except ValueError:
                print("[ERROR] Masukkan angka yang valid untuk nominal!")

        elif pilihan == "3":
            try:
                kategori = input("Masukkan Kategori yang ingin dibatasi: ")
                batas = float(input("Masukkan Batas Nominal Anggaran (Rp): "))
                atur_anggaran(data_keuangan, kategori, batas)
            except ValueError:
                print("[ERROR] Masukkan angka yang valid untuk nominal!")

        elif pilihan == "4":
            tampilkan_ringkasan(data_keuangan)

        elif pilihan == "5":
            tampilkan_riwayat(data_keuangan)

        elif pilihan == "6":
            print("\nTerima kasih telah menggunakan sistem manajemen keuangan. Sampai jumpa!")
            program_berjalan = False  # Menghentikan perulangan while

        else:
            print("[ERROR] Pilihan menu tidak valid! Silakan masukkan opsi 1 hingga 6.")
