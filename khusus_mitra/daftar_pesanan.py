import csv
import json
import sys
import os
import time

from semua.file.lokasi_file import lokasi_file
from . import progress_pesanan as progress_pesanan

# Baca semua pesanan yang masih berstatus "dipesan"
def baca_data_pesanan():
    hasil = []
    with open(lokasi_file["pesanan"], mode='r') as file:
        baris_csv = list(csv.reader(file))
        # print(baris_csv)

        nomor = 1
        for _, baris in enumerate(baris_csv):
            # if not baris or len(baris) < 9:
            #     continue

            if baris[8].strip().lower() == "dipesan":
                data = {
                    "No": nomor,
                    "Id": baris[0],
                    "Jenis barang": baris[1],
                    "Nama barang": baris[2],
                    "Jumlah": int(baris[3]),
                    "Tip": int(baris[4]),
                    "Lokasi": baris[5],
                    "Username": baris[6],
                    "Nama": baris[7],
                }
                hasil.append(data)
                nomor += 1
                
    return hasil

def print_data_pesanan(data_pesanan):
    # Hapus isi terminal biar rapih
    os.system('cls' if os.name == 'nt' else 'clear')

    # Print semua data pesanan baris-per-baris
    for pesanan in data_pesanan:
        print(f"Nomor Pesanan: {pesanan['No']}")
        print(f"Nama: {pesanan['Nama']}")
        print(f"Username: {pesanan['Username']}")
        print(f"Jenis barang: {pesanan['Jenis barang']}")
        print(f"Nama barang: {pesanan['Nama barang']}")
        print(f"Jumlah: {pesanan['Jumlah']}")
        print(f"Tip: Rp. {pesanan['Tip']}")
        print(f"Lokasi: {pesanan['Lokasi']}")
        print("-" * 30)


def tampilkan_daftar_pesanan(data_akun):
    while True:
        print("============= DAFTAR PESANAN =============")

        # Baca data pesanan, lalu tampilkan ke terminal
        data_pesanan = baca_data_pesanan()
        print_data_pesanan(data_pesanan)

        print("Tekan 'r' untuk me-refresh data atau tekan angka untuk menerima pesanan.")
        input_user = input("Masukkan pilihan (tekan 'r' untuk refresh atau nomor pesanan untuk menerima pesanan): ")

        if input_user.lower() == 'r':
            print("Data di-refresh...\n")
            continue
        try:
            tekan = int(input_user)
            if tekan == 0:
                print("Program selesai.")
                break
            if tekan < 1 or tekan > len(data_pesanan):
                print("Nomor pesanan tidak valid!")
                time.sleep(1)
            else:
                progress_pesanan.mulai(data_pesanan[tekan - 1], data_akun)
                break
        except ValueError:
            print("Input harus berupa angka!")
            time.sleep(1)
