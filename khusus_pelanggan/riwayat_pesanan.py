import csv


def tampilkan_riwayat(data_akun):
    try:
        with open('send.csv', mode='r') as file:
            reader = csv.reader(file)
            found = False
            for row in reader:
                if len(row) > 8 and row[6].lower() == data_akun['username'] and row[8] == "selesai":    
                    found = True
                    print("-" * 30)
                    print(f"Nama mitra: {row[9]}")
                    print(f"Username mitra: {row[10]}")
                    print(f"Jenis Barang: {row[0]}")
                    print(f"Nama Barang: {row[1]}")
                    print(f"Jumlah: {row[2]}")
                    print(f"Harga Total: {row[3]}")
                    print(f"Tip: {row[4]}")
                    print(f"Alamat: {row[5]}")
                    print(f"Status: {row[8]}")
                    print("-" * 30)
            if not found:
                print("Tidak ada pesanan ditemukan.")
    except FileNotFoundError:
        print("File pesanan tidak ditemukan!")