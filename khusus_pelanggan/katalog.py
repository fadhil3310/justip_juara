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
    jumlah = input("Masukkan jumlah barang: ").strip()
    
    print(f"\nPesanan Anda: {jumlah} {barang} akan dikirim ke {alamat}.")
    print("Jasa titip 'Beli Barang' berhasil dipesan.\n")

def makanan():
    print("\nAnda memilih jasa titip 'Makanan'.")
    makanan = input("Masukkan nama makanan yang ingin dibeli: ").strip()
    alamat = input("Masukkan alamat pengiriman: ").strip()
    
    print(f"\nPesanan Anda: {makanan} akan dikirim ke {alamat}.")
    print("Jasa titip 'Makanan' berhasil dipesan.\n")

def barang_tugas():
    print("\nAnda memilih jasa titip 'Barang Tugas'.")
    tugas = input("Masukkan jenis barang tugas yang ingin dibeli: ").strip()
    alamat = input("Masukkan alamat pengiriman: ").strip()
    
    print(f"\nPesanan Anda: {tugas} untuk tugas akan dikirim ke {alamat}.")
    print("Jasa titip 'Barang Tugas' berhasil dipesan.\n")

if __name__ == "__main__":
    show_catalog()