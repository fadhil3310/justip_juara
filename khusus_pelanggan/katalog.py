import csv

def save_to_csv(pilihan, barang, alamat):
    # Menyimpan data pesanan ke file CSV
    with open('pesanan.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([pilihan, barang, alamat])
    print(f"Pesanan {barang} telah disimpan ke file pesanan.csv.\n")

def show_catalog():
    print("Selamat datang di katalog jasa titip!")
    print("Pilih jenis jasa titip yang ingin Anda pesan:")
    print("1. Beli Barang")
    print("2. Makanan")
    print("3. Barang Tugas")
    
    pilihan = input("Masukkan pilihan (1/2/3): ").strip()

    if pilihan == "1":
        beli_barang()
    elif pilihan == "2":
        makanan()
    elif pilihan == "3":
        barang_tugas()
    else:
        print("Pilihan tidak valid! Silakan pilih antara 1, 2, atau 3.")
        show_catalog()

def beli_barang():
    print("\nAnda memilih jasa titip 'Beli Barang'.")
    barang = input("Masukkan nama barang yang ingin dibeli: ").strip()
    alamat = input("Masukkan alamat pengiriman: ").strip()
    
    print(f"\nPesanan Anda: {barang} akan dikirim ke {alamat}.")
    
    # Simpan pesanan ke CSV
    save_to_csv("Beli Barang", barang, alamat)

def makanan():
    print("\nAnda memilih jasa titip 'Makanan'.")
    makanan = input("Masukkan nama makanan yang ingin dibeli: ").strip()
    alamat = input("Masukkan alamat pengiriman: ").strip()
    
    print(f"\nPesanan Anda: {makanan} akan dikirim ke {alamat}.")
    
    # Simpan pesanan ke CSV
    save_to_csv("Makanan", makanan, alamat)

def barang_tugas():
    print("\nAnda memilih jasa titip 'Barang Tugas'.")
    tugas = input("Masukkan jenis barang tugas yang ingin dibeli: ").strip()
    alamat = input("Masukkan alamat pengiriman: ").strip()
    
    print(f"\nPesanan Anda: {tugas} untuk tugas akan dikirim ke {alamat}.")
    
    # Simpan pesanan ke CSV
    save_to_csv("Barang Tugas", tugas, alamat)

if __name__ == "__main__":
    show_catalog()
