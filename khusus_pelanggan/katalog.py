import csv
import json
import sys
import uuid
import semua.login.log as login

# Fungsi untuk menampilkan katalog
def tampilkan_katalog(data_akun):
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
        tampilkan_katalog(data_akun)


# Fungsi untuk menyimpan pesanan ke file CSV
def save_to_csv(pilihan, barang, kuantitas, tip, alamat, username, name, status, nama_mitra, username_mitra):
    with open('send.csv', mode='a', newline='') as file:
        id = uuid.uuid4()
        writer = csv.writer(file)
        writer.writerow([id, pilihan, barang, kuantitas, tip, alamat, username, name, status, nama_mitra, username_mitra])
    print(f"Pesanan {barang} telah disimpan ke file pesanan.csv.\n")

# Fungsi untuk kategori "Beli Barang"
def beli_barang(data_akun):
    print("\nAnda memilih jasa titip 'Beli Barang'.")
    barang = input("Masukkan nama barang yang ingin dibeli: ").strip()
    alamat = input("Masukkan alamat pengiriman: ").strip()
    kuantitas = int(input("Masukkan jumlah barang: "))
    tip = int(input("Upah untuk mitra (Rupiah): ")) 
    print(f"\nPesanan Anda: {barang} akan dikirim ke {alamat}.")
    save_to_csv("Beli Barang", barang, kuantitas, tip, alamat, data_akun["username"], data_akun["name"], "dipesan", "Tidak ada" , "tidak ada")

# Fungsi untuk kategori "Makanan"
def makanan(data_akun):
    print("\nAnda memilih jasa titip 'Makanan'.")
    makanan = input("Masukkan nama makanan yang ingin dibeli: ").strip()
    alamat = input("Masukkan alamat pengiriman: ").strip()
    kuantitas = int(input("Masukkan jumlah makanan: "))
    tip = int(input("Upah untuk mitra (Rupiah): ")) 
    print(f"\nPesanan Anda: {makanan} akan dikirim ke {alamat}.")
    save_to_csv("Makanan", makanan, kuantitas, tip, alamat, data_akun["username"], data_akun["name"], "dipesan", "Tidak ada" , "tidak ada")

# Fungsi untuk kategori "Barang Tugas"
def barang_tugas(data_akun):
    print("\nAnda memilih jasa titip 'Barang Tugas'.")
    tugas = input("Masukkan jenis barang tugas yang ingin dibeli: ").strip()
    alamat = input("Masukkan alamat pengiriman: ").strip()
    kuantitas = int(input("Masukkan jumlah barang: "))
    tip = int(input("Upah untuk mitra (Rupiah): ")) 
    print(f"\nPesanan Anda: {tugas} untuk tugas akan dikirim ke {alamat}.")
    save_to_csv("Barang Tugas", tugas, kuantitas, tip, alamat, data_akun["username"], data_akun["name"], "dipesan", "Tidak ada" , "tidak ada")


    