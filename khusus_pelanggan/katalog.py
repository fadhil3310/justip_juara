import csv
import json
import sys
import semua.login.log as login

# Fungsi untuk menyimpan pesanan ke file CSV
def save_to_csv(pilihan, barang, kuantitas, total, tip, alamat, username, name, status, nama_mitra, username_mitra):
    with open('send.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([pilihan, barang, kuantitas, total, tip, alamat, username, name, status, nama_mitra, username_mitra])
    print(f"Pesanan {barang} telah disimpan ke file pesanan.csv.\n")

# Fungsi untuk menampilkan katalog
def show_catalog(data_akun):
    print("Selamat datang di katalog jasa titip!", data_akun["username"])
    print(f"Anda login sebagai: {data_akun['username']} ({data_akun['name']})")
    print("Pilih jenis jasa titip yang ingin Anda pesan:")
    print("1. Beli Barang")
    print("2. Makanan")
    print("3. Barang Tugas")
    
    pilihan = input("Masukkan pilihan (1/2/3): ").strip()

    if pilihan == "1":
        beli_barang(data_akun)
    elif pilihan == "2":
        makanan(data_akun)
    elif pilihan == "3":
        barang_tugas(data_akun)
    else:
        print("Pilihan tidak valid! Silakan pilih antara 1, 2, atau 3.")
        show_catalog(data_akun)

# Fungsi untuk kategori "Beli Barang"
def beli_barang(data_akun):
    print("\nAnda memilih jasa titip 'Beli Barang'.")
    barang = input("Masukkan nama barang yang ingin dibeli: ").strip()
    alamat = input("Masukkan alamat pengiriman: ").strip()
    kuantitas = int(input("Masukkan jumlah barang: "))
    harga = int(input("Harga barang satuan (Rupiah): "))
    tip = int(input("Upah untuk mitra (Rupiah): ")) 
    total = kuantitas * harga 
    print(f"\nPesanan Anda: {barang} akan dikirim ke {alamat}.")
    save_to_csv("Beli Barang", barang, kuantitas, total, tip, alamat, data_akun["username"], data_akun["name"], "dipesan", "Tidak ada" , "tidak ada")

# Fungsi untuk kategori "Makanan"
def makanan(data_akun):
    print("\nAnda memilih jasa titip 'Makanan'.")
    makanan = input("Masukkan nama makanan yang ingin dibeli: ").strip()
    alamat = input("Masukkan alamat pengiriman: ").strip()
    kuantitas = int(input("Masukkan jumlah makanan: "))
    harga = int(input("Harga makanan satuan (Rupiah): "))
    tip = int(input("Upah untuk mitra (Rupiah): ")) 
    total = kuantitas * harga 
    print(f"\nPesanan Anda: {makanan} akan dikirim ke {alamat}.")
    save_to_csv("Makanan", makanan, kuantitas, total, tip, alamat, data_akun["username"], data_akun["name"], "dipesan", "Tidak ada" , "tidak ada")

# Fungsi untuk kategori "Barang Tugas"
def barang_tugas(data_akun):
    print("\nAnda memilih jasa titip 'Barang Tugas'.")
    tugas = input("Masukkan jenis barang tugas yang ingin dibeli: ").strip()
    alamat = input("Masukkan alamat pengiriman: ").strip()
    kuantitas = int(input("Masukkan jumlah barang: "))
    harga = int(input("Harga barang satuan (Rupiah): "))
    tip = int(input("Upah untuk mitra (Rupiah): ")) 
    total = kuantitas * harga 
    print(f"\nPesanan Anda: {tugas} untuk tugas akan dikirim ke {alamat}.")
    save_to_csv("Barang Tugas", tugas, kuantitas, total, tip, alamat, data_akun["username"], data_akun["name"], "dipesan", "Tidak ada" , "tidak ada")

# Fungsi untuk menampilkan menu pelanggan
def menu_pelanggan(data_akun):
    print(f"Selamat datang di menu pelanggan, {data_akun['name']}.")
    print("1. Katalog")
    print("2. Pesanan Anda")
    print("3. Riwayat Pemesanan")
    dial = int(input("Masukkan angka: "))

    if dial == 1:
        print("Menjalankan katalog...")
        show_catalog(data_akun)
    elif dial == 2:
        print("Pesanan Anda:")
        tampilkan_pesanan(data_akun)
    elif dial == 3:
        history_pesanan(data_akun)
    else:
        print("Pilihan tidak valid! Silakan coba lagi.")
        menu_pelanggan(data_akun)

# Fungsi untuk menampilkan pesanan pelanggan
def tampilkan_pesanan(data_akun):
    try:
        with open('send.csv', mode='r') as file:
            reader = csv.reader(file)
            found = False
            for row in reader:
                if len(row) > 8 and row[6].lower() == data_akun['username']:
                    found = True
                    print("-" * 30)
                    print(f"Nama mitra: {row[9]}")
                    print(f"Username mitra: {row[10]}")
                    print(f"Jenis Barang: {row[0]}")
                    print(f"Nama Barang: {row[1]}")
                    print(f"Jumlah: {row[2]}")
                    print(f"Harga Total: {row[3]}")
                    print(f"Tip: {row[4]}")
                    print(f"Alamat: {row[5]}")
                    print(f"Status: {row[8]}")
                    print("-" * 30)
            if not found:
                print("Tidak ada pesanan ditemukan.")
    except FileNotFoundError:
        print("File pesanan tidak ditemukan!")

def history_pesanan(data_akun):
    try:
        with open('send.csv', mode='r') as file:
            reader = csv.reader(file)
            found = False
            for row in reader:
                if len(row) > 8 and row[6].lower() == data_akun['username'] and row[8] == "selesai":    
                    found = True
                    print("-" * 30)
                    print(f"Nama mitra: {row[9]}")
                    print(f"Username mitra: {row[10]}")
                    print(f"Jenis Barang: {row[0]}")
                    print(f"Nama Barang: {row[1]}")
                    print(f"Jumlah: {row[2]}")
                    print(f"Harga Total: {row[3]}")
                    print(f"Tip: {row[4]}")
                    print(f"Alamat: {row[5]}")
                    print(f"Status: {row[8]}")
                    print("-" * 30)
            if not found:
                print("Tidak ada pesanan ditemukan.")
    except FileNotFoundError:
        print("File pesanan tidak ditemukan!")

# Main program
if __name__ == "__main__":
    data_akun = login.authenticate()
    menu_pelanggan(data_akun)

    