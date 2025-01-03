import csv
import os

from semua.file.lokasi_file import lokasi_file

# Baca semua pesanan yang masih berstatus "dipesan"
def baca_data_progress(lokasi_file_progress):
    hasil = []
    with open(lokasi_file_progress, mode='r') as file:
        baris_csv = list(csv.reader(file))
        for _, baris in enumerate(baris_csv):
            data = {
                "Tipe": baris[0],
                "Isi": baris[1],
                "Isi tambahan": baris[2]
            }
            hasil.append(data)
    return hasil

def mulai_bayar(lokasi_file_progress, username_mitra, harga):
    # Hapus isi terminal biar rapih
    os.system('cls' if os.name == 'nt' else 'clear')

    print("============= PEMBAYARAN =============")
    print("Hore! pesanan kamu sudah sampai! WAKTUNYA BAYAR!!")
    print(f"Harga barang (semua): Rp. {harga} (sudah termasuk tip)\n")
    print("Untuk pembayaran, silahkan bayar ke kurir\n")

    while True:
        input("Tekan apa saja apabila sudah selesai membayar ")
        data = baca_data_progress(lokasi_file_progress)
        if data[len(data) - 1]["Tipe"] == "BAYAR":
            mulai_rating(username_mitra)
            break
        else:
            print("Pembayaran belum selesai!")


def mulai_rating(username_mitra):
    # Hapus isi terminal biar rapih
    os.system('cls' if os.name == 'nt' else 'clear')

    print("============= BERI RATING =============")

    while True:
        try:
            rating = int(input("Masukkan rating untuk kurir (1-5):"))
            if rating < 1 or rating > 5:
                print("Masukkan rating yang valid")
            else:
                # Tambahkan rating ke file rating.csv
                with open(lokasi_file["rating"], mode='a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(["mitra", username_mitra, rating])
                
                # Hapus isi terminal biar rapih     
                os.system('cls' if os.name == 'nt' else 'clear') 
                break

        except ValueError:
            print("Masukkan rating yang valid")


