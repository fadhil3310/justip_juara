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

            if baris[8].strip().lower() == "dipesan":
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
                baris[8] = "diterima"
                baris[9] = nama
                baris[10] = username
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



def status_pesanan(data_akun):
    while True:
        print("\n" * 3)  # Bersihkan layar dengan mencetak banyak baris kosong
        print("Status Pesanan:\n")
        hasil_pesanan = {}  # Inisialisasi dictionary untuk menyimpan data pesanan
        data_csv = []  # Menyimpan semua data dari file CSV
        with open('send.csv', mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            data_csv = list(reader)  # Membaca semua data CSV
            ditemukan = False
            nomor = 1  # Inisialisasi nomor pesanan

            for i, row in enumerate(data_csv):
                if len(row) > 8 and row[10].lower() == data_akun['username'] and row[8].lower() != "selesai":
                    ditemukan = True
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
                        "Index CSV": i
                    }
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
                    nomor += 1

            if not ditemukan:
                print("Tidak ada pesanan yang ditemukan untuk akun ini.")
                input("Tekan Enter untuk kembali ke menu utama...")
                return

        # Meminta input untuk memperbarui status
        print("Alur pesanan")
        print("1. Diterima")
        print("2. Dikerjakan")  
        print("3. Dikirim")
        print("4. Pembayaran")
        print("5. Selesai")
        print("Ketik 0 untuk kembali ke menu utama.")

        try:
            nomor_pilihan = int(input("Masukkan nomor pesanan untuk memperbarui status pesanan: "))
            if nomor_pilihan in hasil_pesanan:
                index_csv = hasil_pesanan[nomor_pilihan]["Index CSV"]
                status_lama = hasil_pesanan[nomor_pilihan]["Status"].lower()

                # Tentukan status berikutnya
                status_baru = {
                    "diterima": "dikerjakan",
                    "dikerjakan": "dikirim",
                    "dikirim": "pembayaran",
                    "pembayaran": "selesai"
                }.get(status_lama)

                if status_baru:
                    data_csv[index_csv][8] = status_baru
                    with open('send.csv', mode='w', encoding='utf-8', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerows(data_csv)
                    print(f"Mengubah status pesanan No {nomor_pilihan} menjadi '{status_baru}'.")
                    time.sleep(3)
                    continue
                else:
                    print("Pesanan sudah selesai.")

                

            elif nomor_pilihan == 0:
                print("Kembali ke menu utama.")
                print("\n" * 3)  # Bersihkan layar
                return
            else:
                print("Nomor pesanan tidak ditemukan.")
        except ValueError:
            print("Input tidak valid. Harap masukkan angka.")

      
def daftar_pesanan(data_akun):
    nama_file = "send.csv"

    print(f"Selamat datang, {data_akun['name']}!")
    print(f"Anda masuk sebagai mitra dengan username: {data_akun['username']}\n")

    while True:
        baris_csv = tampilkan_data(nama_file)
        print("Tekan 'r' untuk me-refresh data atau tekan angka untuk menerima pesanan.")
        print("Tekan 0 untuk kembali ke menu utama.")
        input_user = input("Masukkan pilihan: ")

        if input_user.lower() == 'r':
            print("Data di-refresh...\n")
            continue
        try:
            tekan = int(input_user)
            if tekan == 0:
                print("Kembali ke menu utama.")
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

def history_pesanan(data_akun):
    print("Riwayat pengiriman:\n")
    with open('send.csv', mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        ditemukan = False
        nomor = 1  # Inisialisasi nomor pesanan

        for row in reader:
              # Debugging: Lihat isi setiap baris
            if len(row) > 8 and row[10].lower() == data_akun['username'] and row[8].lower() == "selesai":
                ditemukan = True
                print(f"No: {nomor}")  # Tambahkan nomor pesanan
                print(f"Jenis barang: {row[0]}")
                print(f"Nama barang: {row[1]}")
                print(f"Jumlah: {row[2]}")
                print(f"Harga total: {row[3]}")
                print(f"Tip: {row[4]}")
                print(f"Lokasi: {row[5]}")
                print(f"Status: {row[8]}")
                print("-" * 30)
                nomor += 1

        if not ditemukan:
            print("Tidak ada pesanan yang ditemukan untuk akun ini.")

    input("Tekan Enter untuk kembali ke menu utama...")
    print("\n" * 3)
    



def main(data_akun):
    while True:
        print(f"Selamat datang, mitra {data_akun['name']}!")
        print("1. Daftar pesanan")
        print("2. Status pesanan")
        print("3. Riwayat pengiriman")
        print("4. Keluar")

        try:
            dial = int(input("Masukkan angka: "))
            if dial == 1:
                print("\n" * 3)
                daftar_pesanan(data_akun)
            elif dial == 2:
                print("\n" * 3)
                status_pesanan(data_akun)
            elif dial == 3:
                print("\n" * 3)
                history_pesanan(data_akun)
            elif dial == 4:
                print("Terima kasih telah menggunakan layanan kami.")
                break
            else:
                print("Pilihan tidak valid, silakan coba lagi.")
        except ValueError:
            print("Input harus berupa angka!")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            data_akun = json.loads(sys.argv[1])
            main(data_akun)
        except json.JSONDecodeError:
            print("Error: Data akun tidak valid.")
    else:
        print("Error: Data akun tidak diberikan.")