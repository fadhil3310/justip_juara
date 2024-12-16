import csv

def baca_csv_ke_dictionary(nama_file):
    hasil = []
    with open(nama_file, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        
        # Iterasi baris
        for idx, baris in enumerate(reader, start=1):
            # Abaikan baris kosong atau tidak cukup kolom
            if not baris or len(baris) < 9:
                print(f"Baris {idx} dilewati: Kosong atau tidak valid.")
                continue
            
            # Cek apakah kolom terakhir adalah "dipesan"
            if baris[-1].strip().lower() == "dipesan":
                data = {
                    "No": idx,
                    "Nama": baris[7],
                    "Username": baris[6],
                    "Jenis barang": baris[0],
                    "Nama barang": baris[1],
                    "Jumlah": int(baris[2]),
                    "Harga total": int(baris[3]),
                    "Tip": int(baris[4]),
                    "Lokasi": baris[5]
                }
                hasil.append(data)
    return hasil

# Contoh penggunaan
nama_file = "pesan.csv"
hasil = baca_csv_ke_dictionary(nama_file)

# Cetak hasil
for pesanan in hasil:
    print(f"Nomor Pesanan: {pesanan['No']}")
    print(f"Nama: {pesanan['Nama']}")
    print(f"Username: {pesanan['Username']}")
    print(f"Jenis barang: {pesanan['Jenis barang']}")
    print(f"Nama barang: {pesanan['Nama barang']}")
    print(f"Jumlah: {pesanan['Jumlah']}")
    print(f"Harga total: {pesanan['Harga total']}")
    print(f"Tip: {pesanan['Tip']}")
    print(f"Lokasi: {pesanan['Lokasi']}")
    print("-" * 30)
