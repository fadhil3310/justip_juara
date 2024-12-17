import csv
import json
import sys

def baca_csv_ke_dictionary(nama_file):
    hasil = []
    with open(nama_file, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        # Baca semua baris
        baris_csv = list(reader)
        
        # Iterasi baris
        for idx, baris in enumerate(baris_csv, start=1):
            # Abaikan baris kosong atau tidak cukup kolom
            if not baris or len(baris) < 9:
                print(f"Baris {idx} dilewati: Kosong atau tidak valid.")
                continue
            
            # Cek apakah kolom terakhir adalah "dipesan"
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
            # Jika nomor baris sesuai dengan nomor yang dipilih, ubah kolom terakhir menjadi "diterima" dan tambah nama serta username
            if idx == nomor_idx:
                print(f"Pesanan dengan No {nomor_idx} diubah statusnya menjadi 'diterima'.")
                baris[-1] = "diterima"
                # Menambahkan kolom baru untuk nama dan username
                baris.append(nama)
                baris.append(username)
            writer.writerow(baris)

# Mengambil data akun yang diterima dari main.py (misalnya, melalui argumen JSON)
if len(sys.argv) > 1:
    data_akun = json.loads(sys.argv[1])
    nama_pengguna = data_akun['name']
    username_pengguna = data_akun['username']
else:
    print("Data akun tidak ditemukan!")
    sys.exit(1)

# Contoh penggunaan
nama_file = "pesan.csv"
hasil, baris_csv = baca_csv_ke_dictionary(nama_file)

# Cetak hasil
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

try:
    tekan = int(input("Tekan angka untuk menerima pesanan: "))
    # Validasi input
    if tekan < 1 or tekan > len(baris_csv):
        print("Nomor pesanan tidak valid!")
    else:
        ubah_status_pesanan(nama_file, baris_csv, tekan, nama_pengguna, username_pengguna)
except ValueError:
    print("Input harus berupa angka!")



    