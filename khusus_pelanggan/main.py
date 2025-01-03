from . import katalog as katalog
from . import pesanan_sekarang as pesanan_sekarang
from . import riwayat_pesanan as riwayat_pesanan

# Fungsi untuk menampilkan menu pelanggan
def menu_pelanggan(data_akun):
    while True:
        print(f"Selamat datang di menu pelanggan, {data_akun['name']}.")
        print("1. Katalog")
        print("2. Riwayat Pemesanan")
        dial = int(input("Masukkan angka: "))

        if dial == 1:
            print("Menjalankan katalog...")
            katalog.tampilkan_katalog(data_akun)
        elif dial == 2:
            riwayat_pesanan.tampilkan_riwayat(data_akun)
        else:
            print("Pilihan tidak valid! Silakan coba lagi.")