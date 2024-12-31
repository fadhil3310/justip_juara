import katalog as katalog
import pesanan_sekarang as pesanan_sekarang
import riwayat_pesanan as riwayat_pesanan

# Fungsi untuk menampilkan menu pelanggan
def main(data_akun):
    print(f"Selamat datang di menu pelanggan, {data_akun['name']}.")
    print("1. Katalog")
    print("2. Pesanan Anda")
    print("3. Riwayat Pemesanan")
    dial = int(input("Masukkan angka: "))

    if dial == 1:
        print("Menjalankan katalog...")
        katalog.tampilkan_katalog(data_akun)
    elif dial == 2:
        print("Pesanan Anda:")
        pesanan_sekarang.tampilkan_pesanan(data_akun)
    elif dial == 3:
        riwayat_pesanan.tampilkan_riwayat(data_akun)
    else:
        print("Pilihan tidak valid! Silakan coba lagi.")
        main(data_akun)