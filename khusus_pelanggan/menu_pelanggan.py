import csv
import semua.login.log as login
import khusus_pelanggan.katalog as katalog


data_akun = login.authenticate()


filename = 'buy.csv'


print(f"Selamat datang di menu, {data_akun['name']}.")
print("1. Katalog")
print("2. Pesanan anda")
print("3. Riwayat pemesanan")
dial = int(input("Masukkan angka: "))

if dial == 1:
    print("Akun 'pelanggan' terdeteksi. Menjalankan katalog...")
    # Menjalankan katalog.py dengan mengirimkan data akun sebagai argumen
    katalog.start(data_akun)

if dial == 2:
    with open('buy.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
    # Periksa apakah indeks ke-8 adalah "dipesan"
            if len(row) > 8 and row[6].lower() == data_akun['username']:
                print("-" * 30)
                print(f"Nama mitra: {row[9]}")
                print(f"Username mitra: {row[10]}")
                print(f"Jenis barang: {row[0]}")
                print(f"Nama barang: {row[1]}")
                print(f"Jumlah: {row[2]}")
                print(f"Harga total: {row[3]}")
                print(f"Tip: {row[4]}")
                print(f"Lokasi: {row[5]}")
                print(f"Status: {row[8]}")                    
                print("-" * 30)

