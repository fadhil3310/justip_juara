

import os

def register(username, password, nama, akun):
    # Membuat folder 'login' jika belum ada
    os.makedirs("login", exist_ok=True)
    # Menyimpan file akun.txt di dalam folder 'login'
    with open("login/akun.csv", "a") as file:
        file.write(f"{username},{password},{nama},{akun}\n")
    print("Registrasi berhasil.")

def login(username, password):
    # Membaca file akun.txt dari folder 'login'
    try:
        with open("login/akun.csv", "r") as file:
            for line in file:
                stored_username, stored_password, stored_nama, stored_akun = line.strip().split(",")
                if stored_username == username and stored_password == password:
                    print("Login berhasil.")
                    return stored_nama  # Mengembalikan nama pengguna yang berhasil login
    except FileNotFoundError:
        print("File akun.csv tidak ditemukan.")
    print("Username atau password salah.")
    return None

# Program utama
nama = None  # Mendefinisikan variabel nama di luar loop
while True:
    pilihan = input("Pilih 'register' atau 'login': ").strip().lower()
    if pilihan == "register":
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        nama = input("Masukkan nama lengkap: ")
        akun = input("Tipe akun? 'mitra' atau 'pelanggan':").strip().lower()        
        if akun != "mitra" and akun != "pelanggan":
            print("Tipe akun hanya bisa 'mitra' atau 'pelanggan'")
        else: 
            register(username, password, nama, akun)
    elif pilihan == "login":
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        nama = login(username, password)  # Menyimpan hasil login di variabel nama
        if nama:
            break
    else:
        print("Pilihan tidak valid.")

# Menampilkan pesan selamat datang setelah login berhasil
print(f"Selamat datang di JusTip, {nama}\n")
