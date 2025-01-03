import csv
import json
import sys
import os
import time

from . import daftar_pesanan as daftar
from . import status_pesanan as status
from . import riwayat_pesanan as riwayat


def menu_mitra(data_akun):
    while True:
        print(f"Selamat datang, mitra {data_akun['name']}!")
        print("1. Daftar pesanan")
        print("2. Riwayat pengiriman")
        print("3. Keluar")

        dial = input("Masukkan angka: ")
        if dial == "1":
            daftar.tampilkan_daftar_pesanan(data_akun)
        elif dial == "2":
            riwayat.tampilkan_riwayat_pesanan(data_akun)
        elif dial == "3":
            print("Terima kasih telah menggunakan layanan kami.")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")