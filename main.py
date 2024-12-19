
import semua.login.log as login

import khusus_pelanggan.katalog as katalog
import khusus_mitra.job as job

# Autentikasi dan login
data_akun = login.authenticate()

# Menampilkan data akun setelah login
print(f"Nama: {data_akun['name']}")
print(f"Tipe akun: {data_akun['account_type']}")

# Mengecek tipe akun, jika "pelanggan", jalankan katalog.py
if data_akun['account_type'] == 'pelanggan':
    print("Akun 'pelanggan' terdeteksi. Menjalankan katalog...")
    
    # Menjalankan katalog.py dengan mengirimkan data akun sebagai argumen
    katalog.start(data_akun)
elif data_akun['account_type'] == 'mitra':
    print("Akun 'mitra' terdeteksi. Menjalankan job...")
    job.main(data_akun)


else:
    print("Akun bukan pelanggan. Akses ke katalog tidak diberikan.")

