import os
import csv
import uuid

from khusus_mitra.beres_pesanan import mulai_pembayaran
from semua.file.lokasi_file import lokasi_file


def mulai(data_pesanan, data_akun):
    # Hapus isi terminal biar rapih
    os.system('cls' if os.name == 'nt' else 'clear')

    # Cek apakah file progress tugas dari pesanan ini ada
    # Apabila tidak, maka langsung keluarkan error karena terdapat kesalahan dalam sistem
    lokasi_file_progress = lokasi_file["progress_pesanan"] + data_pesanan["Id"] + ".csv"
    if os.path.isfile(lokasi_file_progress) is False:
        # Langsung lempar user ke menu utama
        print("Mohon maaf, terjadi kesalahan dari sistem. Pesanan tidak dapat dilanjutkan")
        return
    
    # Ubah status pesanan dari "dipesan" menjadi "diterima"
    ubah_status_pesanan(data_pesanan["Id"], data_akun)
    # Lapor progress bahwa pesanan sudah dipilih oleh mitra
    lapor_terima_pesanan(lokasi_file_progress, data_akun)

    print("============= ANTAR PESANAN =============")
    print("Pesanan berhasil diambil. Selamat bekerja ganteng/cantik!")
    print("Utamakan keselamatan, bukan kecepatan...")
    print("...tapi ga lama banget juga, nanti dikasih rating jelek sama pelanggan 👎💢\n")

    print(f"Nama pelanggan: {data_pesanan['Nama']}")
    print(f"Alamat pelanggan: {data_pesanan['Lokasi']}\n")

    print("Input progress tugas kamu disini. Kalau sudah beres, ketik 'BERES' untuk lanjut ke pembayaran")
    while True:
        input_user = input("Masukkan progress: ")
        if input_user != "BERES":
            lapor_progress_pesanan(lokasi_file_progress, input_user)
            print("Pesan berhasil dikirim ke pelanggan")
        else:
            # Cek apabila harga yang dimasukkan valid
            try:
                harga = format_uang(input("Berapa harga pesanan tersebut? (Rp): "))
            except ValueError:
                print("Masukkan uang yang valid!")
                continue

            total_harga = harga + data_pesanan["Tip"]
            lapor_beres_pesanan(lokasi_file_progress, total_harga)
            mulai_pembayaran(lokasi_file_progress, data_pesanan["Id"], total_harga, data_pesanan["Username"])
            break

# Hapus titik sama koma biar bisa diconvert jadi int
def format_uang(teks: str):
    return int(teks.replace(".", "").replace(",", ""))

def kirim_progress(lokasi_file_progress, tipe, isi, isi_tambahan):
     with open(lokasi_file_progress, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([tipe, isi, isi_tambahan])

def lapor_terima_pesanan(lokasi_file_progress, data_akun):
    kirim_progress(lokasi_file_progress, "TERIMA", data_akun['username'], data_akun['name'])

def lapor_progress_pesanan(lokasi_file_progress, teks):
    kirim_progress(lokasi_file_progress, "PROGRESS", teks, "-")

def lapor_beres_pesanan(lokasi_file_progress, harga_barang):
    kirim_progress(lokasi_file_progress, "BERES", harga_barang, "-")
            
def ubah_status_pesanan(id_pesanan, data_akun):
    # Baca file pesanan
    data_pesanan = None
    with open(lokasi_file["pesanan"], mode='r') as file:
        data_pesanan = list(csv.reader(file))

    # Tulis file pesanan
    with open(lokasi_file["pesanan"], mode='w',  newline='') as file:
        writer = csv.writer(file)
        for _, baris in enumerate(data_pesanan, start=1):
            if baris[0] == id_pesanan:
                baris[8] = "diterima"
                baris[9] = data_akun["username"]
                baris[10] = data_akun["name"]
            writer.writerow(baris)

    
