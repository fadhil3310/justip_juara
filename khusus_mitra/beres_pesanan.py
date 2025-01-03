


import csv
import os

from semua.file.lokasi_file import lokasi_file


def mulai_pembayaran(lokasi_file_progress, id_pesanan, total_harga, username_pelanggan):
    # Hapus isi terminal biar rapih
    os.system('cls' if os.name == 'nt' else 'clear')

    print("============= PEMBAYARAN =============")
    print("Tunggu pelanggan membayar")
    print(f"Total harga: Rp. {total_harga}")
    
    while True:
        input_user = input("Apabila sudah selesai, ketik SELESAI: ")
        if input_user == "SELESAI":
            lapor_pembayaran(lokasi_file_progress, id_pesanan)
            mulai_rating(username_pelanggan)
            break

def lapor_pembayaran(lokasi_file_progress, id_pesanan):
    with open(lokasi_file_progress, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["BAYAR", "-", "-"])

    data_progress = None
    with open(lokasi_file["pesanan"], mode='r') as file:
        data_progress = list(csv.reader(file))
    with open(lokasi_file["pesanan"], mode='w',  newline='') as file:
        writer = csv.writer(file)
        for _, baris in enumerate(data_progress, start=1):
            if baris[0] == id_pesanan:
                baris[8] = "beres"
            writer.writerow(baris)

def mulai_rating(username_pelanggan):
     # Hapus isi terminal biar rapih
    os.system('cls' if os.name == 'nt' else 'clear')

    print("============= BERI RATING =============")

    while True:
        try:
            rating = int(input("Masukkan rating untuk pelanggan (1-5):"))
            if rating < 1 or rating > 5:
                print("Masukkan rating yang valid")
            else:
                # Tambahkan rating ke file rating.csv
                with open(lokasi_file["rating"], mode='a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(["pelanggan", username_pelanggan, rating])
                
                # Hapus isi terminal biar rapih     
                os.system('cls' if os.name == 'nt' else 'clear') 
                break

        except ValueError:
            print("Masukkan rating yang valid")