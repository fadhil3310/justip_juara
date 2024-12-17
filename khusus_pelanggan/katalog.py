import csv
import sys
import json

def save_to_csv(pilihan, barang, kuantitas, total, tip, alamat, username, name, status):
    # Menyimpan data pesanan ke file CSV
    with open('buy.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        # Format: [pilihan, barang, alamat, username, name]
        writer.writerow([pilihan, barang, kuantitas, total, tip, alamat, username, name, status])
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
    kuantitas = int(input("Masukkan jumlah barang: "))
    harga = int(input("Harga barang satuan (Rupiah): "))
    tip = int(input("Upah untuk mitra (Rupiah): ")) 
    total = kuantitas * harga 
    print(f"\nPesanan Anda: {barang} akan dikirim ke {alamat}.")
    
    # Simpan pesanan ke CSV
    save_to_csv("Beli Barang", barang, kuantitas, total, tip, alamat, data_akun["username"], data_akun["name"], "dipesan")

def makanan(data_akun):
    print("\nAnda memilih jasa titip 'Makanan'.")
    makanan = input("Masukkan nama makanan yang ingin dibeli: ").strip()
    alamat = input("Masukkan alamat pengiriman: ").strip()
    kuantitas = int(input("Masukkan jumlah makanan: "))
    harga = int(input("Harga makanan satuan (Rupiah): "))
    tip = int(input("Upah untuk mitra (Rupiah): ")) 
    total = kuantitas * harga 
    print(f"\nPesanan Anda: {makanan} akan dikirim ke {alamat}.")
    
    # Simpan pesanan ke CSV
    save_to_csv("Makanan", makanan, kuantitas, total, tip, alamat, data_akun["username"], data_akun["name"], "dipesan")

def barang_tugas(data_akun):
    print("\nAnda memilih jasa titip 'Barang Tugas'.")
    tugas = input("Masukkan jenis barang tugas yang ingin dibeli: ").strip()
    alamat = input("Masukkan alamat pengiriman: ").strip()
    kuantitas = int(input("Masukkan jumlah barang: "))
    harga = int(input("Harga barang satuan (Rupiah): "))
    tip = int(input("Upah untuk mitra (Rupiah): ")) 
    total = kuantitas * harga 
    print(f"\nPesanan Anda: {tugas} untuk tugas akan dikirim ke {alamat}.")
    
    # Simpan pesanan ke CSV
    save_to_csv("Barang Tugas", tugas, kuantitas, total, tip, alamat, data_akun["username"], data_akun["name"], "dipesan")

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
