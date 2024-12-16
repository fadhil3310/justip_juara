import csv
import sys
import json

def save_to_csv(pilihan, barang, alamat, username, name):
    # Menyimpan data pesanan ke file CSV
    with open('pesanan.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        # Format: [pilihan, barang, alamat, username, name]
        writer.writerow([pilihan, barang, alamat, username, name])
    print(f"Pesanan {barang} telah disimpan ke file pesanan.csv.\n")

def show_catalog(data_akun):
    print("Selamat datang di katalog jasa titip!", data_akun["username"])
    print(f"Anda login sebagai: {data_akun['username']} ({data_akun['name']})")
    print("Pilih jenis jasa titip yang ingin Anda pesan:")
    print("1. Beli Barang")
    print("2. Makanan")
    print("3. Barang Tugas")
    
    pilihan = input("Masukkan pilihan (1/2/3): ").strip()

    if pilihan == "1":
        beli_barang(data_akun)
    elif pilihan == "2":
        makanan(data_akun)
    elif pilihan == "3":
        barang_tugas(data_akun)
    else:
        print("Pilihan tidak valid! Silakan pilih antara 1, 2, atau 3.")
        show_catalog(data_akun)

def beli_barang(data_akun):
    print("\nAnda memilih jasa titip 'Beli Barang'.")
    barang = input("Masukkan nama barang yang ingin dibeli: ").strip()
    alamat = input("Masukkan alamat pengiriman: ").strip()
    
    print(f"\nPesanan Anda: {barang} akan dikirim ke {alamat}.")
    
    # Simpan pesanan ke CSV
    save_to_csv("Beli Barang", barang, alamat, data_akun["username"], data_akun["name"])

def makanan(data_akun):
    print("\nAnda memilih jasa titip 'Makanan'.")
    makanan = input("Masukkan nama makanan yang ingin dibeli: ").strip()
    alamat = input("Masukkan alamat pengiriman: ").strip()
    
    print(f"\nPesanan Anda: {makanan} akan dikirim ke {alamat}.")
    
    # Simpan pesanan ke CSV
    save_to_csv("Makanan", makanan, alamat, data_akun["username"], data_akun["name"])

def barang_tugas(data_akun):
    print("\nAnda memilih jasa titip 'Barang Tugas'.")
    tugas = input("Masukkan jenis barang tugas yang ingin dibeli: ").strip()
    alamat = input("Masukkan alamat pengiriman: ").strip()
    
    print(f"\nPesanan Anda: {tugas} untuk tugas akan dikirim ke {alamat}.")
    
    # Simpan pesanan ke CSV
    save_to_csv("Barang Tugas", tugas, alamat, data_akun["username"], data_akun["name"])

if __name__ == "__main__":
    # Menerima data akun dari argumen command line
    if len(sys.argv) > 1:
        try:
            data_akun = json.loads(sys.argv[1])
            show_catalog(data_akun)
        except (json.JSONDecodeError, IndexError):
            print("Data akun tidak valid. Pastikan data akun dikirim dengan benar.")
    else:
        print("Data akun tidak ditemukan. Harap jalankan melalui main.py.")
