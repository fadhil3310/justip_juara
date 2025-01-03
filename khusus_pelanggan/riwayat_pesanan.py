import csv

from semua.file.lokasi_file import lokasi_file


def tampilkan_riwayat(data_akun):
    try:
        with open(lokasi_file["pesanan"], mode='r') as file:
            reader = csv.reader(file)
            found = False
            
            print("-" * 30)
            for row in reader:
                if row[6].lower() == data_akun['username'] and row[8] == "beres":    
                    found = True
                    print(f"Nama mitra: {row[9]}")
                    print(f"Username mitra: {row[10]}")
                    print(f"Jenis Barang: {row[1]}")
                    print(f"Nama Barang: {row[2]}")
                    print(f"Jumlah: {row[3]}")
                    print(f"Tip: {row[4]}")
                    print(f"Alamat: {row[5]}")
                    print(f"Status: {row[8]}")
                    print("-" * 30)
            if not found:
                print("Tidak ada pesanan ditemukan.")
    except FileNotFoundError:
        print("File pesanan tidak ditemukan!")