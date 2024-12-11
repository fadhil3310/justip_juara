import subprocess
import semua.login.log as login
import json

# Autentikasi dan login
data_akun = login.authenticate()

# Menampilkan data akun setelah login
print(f"Nama: {data_akun['name']}")
print(f"Tipe akun: {data_akun['account_type']}")

# Mengecek tipe akun, jika "pelanggan", jalankan katalog.py
if data_akun['account_type'] == 'pelanggan':
    print("Akun 'pelanggan' terdeteksi. Menjalankan katalog...")
    
    # Menjalankan katalog.py dengan mengirimkan data akun sebagai argumen
    subprocess.run(['python', 'khusus_pelanggan/katalog.py', json.dumps(data_akun)])
else:
    print("Akun bukan pelanggan. Akses ke katalog tidak diberikan.")

