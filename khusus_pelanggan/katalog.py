import csv
import json
import os
import sys
import uuid
import semua.login.log as login

from semua.file.lokasi_file import lokasi_file
from . import progress_pesanan as progress_pesanan


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


def kirim_pesanan(pilihan, barang, kuantitas, tip, alamat, username, name):
    id_pesanan = uuid.uuid4()

    # Tambahkan ke file pesanan.csv
    with open(lokasi_file["pesanan"], mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([id_pesanan, pilihan, barang, kuantitas, tip, alamat, username, name, "dipesan", "-", "-"])
    
    # Buat file progress pesanan
    if not os.path.exists(lokasi_file["progress_pesanan"]):
        os.mkdir(lokasi_file["progress_pesanan"])
    with open(lokasi_file["progress_pesanan"] + str(id_pesanan) + ".csv", mode='w'):
        pass

    progress_pesanan.mulai(lokasi_file["progress_pesanan"] + str(id_pesanan) + ".csv")


# Fungsi untuk kategori "Beli Barang"
def beli_barang(data_akun):
    print("\nAnda memilih jasa titip 'Beli Barang'.")
    barang = input("Masukkan nama barang yang ingin dibeli: ").strip()
    alamat = input("Masukkan alamat pengiriman: ").strip()
    kuantitas = int(input("Masukkan jumlah barang: "))
    tip = int(input("Upah untuk mitra (Rupiah): ")) 
    print(f"\nPesanan Anda: {barang} akan dikirim ke {alamat}.")
    kirim_pesanan("Beli Barang", barang, kuantitas, tip, alamat, data_akun["username"], data_akun["name"])

# Fungsi untuk kategori "Makanan"
def makanan(data_akun):
    print("\nAnda memilih jasa titip 'Makanan'.")
    makanan = input("Masukkan nama makanan yang ingin dibeli: ").strip()
    alamat = input("Masukkan alamat pengiriman: ").strip()
    kuantitas = int(input("Masukkan jumlah makanan: "))
    tip = int(input("Upah untuk mitra (Rupiah): ")) 
    print(f"\nPesanan Anda: {makanan} akan dikirim ke {alamat}.")
    kirim_pesanan("Makanan", makanan, kuantitas, tip, alamat, data_akun["username"], data_akun["name"])

# Fungsi untuk kategori "Barang Tugas"
def barang_tugas(data_akun):
    print("\nAnda memilih jasa titip 'Barang Tugas'.")
    tugas = input("Masukkan jenis barang tugas yang ingin dibeli: ").strip()
    alamat = input("Masukkan alamat pengiriman: ").strip()
    kuantitas = int(input("Masukkan jumlah barang: "))
    tip = int(input("Upah untuk mitra (Rupiah): ")) 
    print(f"\nPesanan Anda: {tugas} untuk tugas akan dikirim ke {alamat}.")
    kirim_pesanan("Barang Tugas", tugas, kuantitas, tip, alamat, data_akun["username"], data_akun["name"])


    