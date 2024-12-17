import csv
import json
import sys
import os
import time

def baca_csv_ke_dictionary(nama_file):
    hasil = []
    with open(nama_file, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        baris_csv = list(reader)

        for idx, baris in enumerate(baris_csv, start=1):
            if not baris or len(baris) < 9:
                print(f"Baris {idx} dilewati: Kosong atau tidak valid.")
                continue

            if baris[-1].strip().lower() == "dipesan":
                data = {
                    "No": idx,
                    "Nama": baris[7],
                    "Username": baris[6],
                    "Jenis barang": baris[0],
                    "Nama barang": baris[1],
                    "Jumlah": int(baris[2]),
                    "Harga total": int(baris[3]),
                    "Tip": int(baris[4]),
                    "Lokasi": baris[5]
                }
                hasil.append(data)
    return hasil, baris_csv

def ubah_status_pesanan(nama_file, baris_csv, nomor_idx, nama, username):
    with open(nama_file, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        for idx, baris in enumerate(baris_csv, start=1):
            if idx == nomor_idx:
                print(f"Pesanan dengan No {nomor_idx} diubah statusnya menjadi 'diterima'.")
                baris[-1] = "diterima"
                baris.append(nama)
                baris.append(username)
            writer.writerow(baris)

def tampilkan_data(nama_file):
    hasil, baris_csv = baca_csv_ke_dictionary(nama_file)

    os.system('cls' if os.name == 'nt' else 'clear')

    for pesanan in hasil:
        print(f"Nomor Pesanan: {pesanan['No']}")
        print(f"Nama: {pesanan['Nama']}")
        print(f"Username: {pesanan['Username']}")
        print(f"Jenis barang: {pesanan['Jenis barang']}")
        print(f"Nama barang: {pesanan['Nama barang']}")
        print(f"Jumlah: {pesanan['Jumlah']}")
        print(f"Harga total: {pesanan['Harga total']}")
        print(f"Tip: {pesanan['Tip']}")
        print(f"Lokasi: {pesanan['Lokasi']}")
        print("-" * 30)

    return baris_csv

def main(data_akun):
    nama_file = "buy.csv"

    print(f"Selamat datang, {data_akun['name']}!")
    print(f"Anda masuk sebagai mitra dengan username: {data_akun['username']}.\n")

    while True:
        baris_csv = tampilkan_data(nama_file)
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
            if tekan < 1 or tekan > len(baris_csv):
                print("Nomor pesanan tidak valid!")
            else:
                nama_pengguna = data_akun['name']
                username_pengguna = data_akun['username']
                ubah_status_pesanan(nama_file, baris_csv, tekan, nama_pengguna, username_pengguna)

        except ValueError:
            print("Input harus berupa angka!")

        time.sleep(2)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            data_akun = json.loads(sys.argv[1])
            main(data_akun)
        except json.JSONDecodeError:
            print("Error: Data akun tidak valid.")
    else:
        print("Error: Data akun tidak diberikan.")
