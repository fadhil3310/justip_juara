import csv
import json
import sys
import os
import time

from semua.file.lokasi_file import lokasi_file


def tampilkan_riwayat_pesanan(data_akun):
    print("Riwayat pengiriman:\n")
    with open(lokasi_file["pesanan"], mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        ditemukan = False
        nomor = 1  # Inisialisasi nomor pesanan

        for row in reader:
            if row[9].lower() == data_akun['username'] and row[8].lower() == "beres":
                ditemukan = True
                print(f"No: {nomor}")  # Tambahkan nomor pesanan
                print(f"Jenis barang: {row[1]}")
                print(f"Nama barang: {row[2]}")
                print(f"Jumlah: {row[3]}")
                print(f"Tip: {row[4]}")
                print(f"Lokasi: {row[5]}")
                print(f"Status: {row[8]}")
                print("-" * 30)
                nomor += 1

        if not ditemukan:
            print("Tidak ada pesanan yang ditemukan untuk akun ini.")

    input("Tekan Enter untuk kembali ke menu utama...")