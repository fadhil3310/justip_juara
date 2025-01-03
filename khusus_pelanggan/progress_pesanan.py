import os
import csv
import uuid

from semua.file.lokasi_file import lokasi_file
from . import beres_pesanan as beres_pesanan


def mulai(lokasi_file_progress):

    while True:
        # Hapus isi terminal biar rapih
        os.system('cls' if os.name == 'nt' else 'clear')

        print("============= PROGRESS PESANAN =============")
        print("Pesan progress pesanan yang dikirim kurir akan ditampilkan disini\n")

        # Baca data progress tugas mitra
        data = baca_data_progress(lokasi_file_progress)

        # Kalau tugas sudah selesai, lanjut ke pembayaran
        if len(data) > 0 and data[len(data) - 1]["Tipe"] == "BERES":
            beres_pesanan.mulai_bayar(lokasi_file_progress, data[0]["Isi"], data[len(data) - 1]["Isi"])
            break
        # Kalau tugas sudah selesai dan sudah bayar, lanjut ke rating
        elif len(data) > 0 and data[len(data) - 1]["Tipe"] == "BAYAR":
            beres_pesanan.mulai_rating(data[0]["Isi"])
            break
        # Kalau pesanan pelanggan baru dipilih oleh mitra,
        # tampilkan pesan ke user kalau pesanan sudah dipilih mitra
        elif len(data) > 0:
            print(f"Hore! Pesananmu sudah diterima oleh: {data[0]["Isi tambahan"]}.")
            print("Doain ya kurir-mu biar ga kecebur ke got karena terkesima mengantar paket untuk orang se-spesial kamu! 💗🫵\n")
        
        # Print semua pesan progress baris-per-baris
        for baris in data:
            if baris["Tipe"] == "PROGRESS":
                print(f"Progress: {baris['Isi']}")

        input("Tekan apa saja untuk refresh ")

    
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