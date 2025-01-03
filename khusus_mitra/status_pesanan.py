import csv
import json
import sys
import os
import time

def tampilkan_status_pesanan(data_akun):
    print("Status Pesanan:\n")
    hasil_pesanan = {}  # Inisialisasi dictionary untuk menyimpan data pesanan
    data_csv = []  # Menyimpan semua data dari file CSV
    with open('send.csv', mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        data_csv = list(reader)  # Membaca semua data CSV
        ditemukan = False
        nomor = 1  # Inisialisasi nomor pesanan

        for i, row in enumerate(data_csv):
            if len(row) > 8 and row[9].lower() == data_akun['username'] and row[7].lower() != "selesai":
                ditemukan = True
                # Simpan data ke dictionary
                hasil_pesanan[nomor] = {
                    "Nama pelanggan": row[7],
                    "Username pelanggan": row[6],
                    "Jenis barang": row[0],
                    "Nama barang": row[1],
                    "Jumlah": row[2],
                    "Harga total": row[3],
                    "Tip": row[4],
                    "Lokasi": row[5],
                    "Status": row[8],
                    "Index CSV": i  # Menyimpan indeks untuk pengeditan nanti
                }
                # Cetak data pesanan
                print(f"No: {nomor}")
                print(f"Nama pelanggan: {row[7]}")
                print(f"Username pelanggan: {row[6]}")
                print(f"Jenis barang: {row[0]}")
                print(f"Nama barang: {row[1]}")
                print(f"Jumlah: {row[2]}")
                print(f"Harga total: {row[3]}")
                print(f"Tip: {row[4]}")
                print(f"Lokasi: {row[5]}")
                print(f"Status: {row[8]}")
                print("-" * 30)
                nomor += 1  # Tambahkan 1 ke nomor untuk setiap pesanan

        if not ditemukan:
            print("Tidak ada pesanan yang ditemukan untuk akun ini.")
            return hasil_pesanan

    # Meminta input nomor pesanan untuk memperbarui status
    try:
        print("Alur pesanan")
        print("1. Diterima")
        print("2. Dikerjakan")  
        print("3. Dikirim")
        print("4. pembayaran")
        print("5. Selesai")
        nomor_pilihan = int(input("Masukkan nomor pesanan untuk memperbarui status pesanan: "))
        if nomor_pilihan in hasil_pesanan:
           
            if hasil_pesanan[nomor_pilihan]["Status"].lower() == "diterima":
                index_csv = hasil_pesanan[nomor_pilihan]["Index CSV"]                   
                data_csv[index_csv][8] = "dikerjakan"
                with open('send.csv', mode='w', encoding='utf-8', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(data_csv)
                print(f"Status pesanan No {nomor_pilihan} berhasil diperbarui.")
                
            elif hasil_pesanan[nomor_pilihan]["Status"].lower() == "dikerjakan":
                index_csv = hasil_pesanan[nomor_pilihan]["Index CSV"]                   
                data_csv[index_csv][8] = "dikirim"
                with open('send.csv', mode='w', encoding='utf-8', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(data_csv)
                    print(f"Status pesanan No {nomor_pilihan} berhasil diperbarui.")
                    
            elif hasil_pesanan[nomor_pilihan]["Status"].lower() == "dikirim":
                index_csv = hasil_pesanan[nomor_pilihan]["Index CSV"]                   
                data_csv[index_csv][8] = "pembayaran"
                with open('send.csv', mode='w', encoding='utf-8', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(data_csv)
                    print(f"Status pesanan No {nomor_pilihan} berhasil diperbarui.")
            
            elif hasil_pesanan[nomor_pilihan]["Status"].lower() == "pembayaran":
                index_csv = hasil_pesanan[nomor_pilihan]["Index CSV"]                   
                data_csv[index_csv][8] = "selesai"
                with open('send.csv', mode='w', encoding='utf-8', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(data_csv)
                    print(f"Status pesanan No {nomor_pilihan} berhasil diperbarui.")            
        else:
            print("Nomor pesanan tidak ditemukan.")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")

    return hasil_pesanan  # Kembalikan dictionary hasil pesanan