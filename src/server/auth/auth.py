import os

def register(username, password, nama, akun):
    # Membuat folder 'login' jika belum ada
    # os.makedirs("login", exist_ok=True)
    # Menyimpan file akun.txt di dalam folder 'login'
    with open("./akun.csv", "a") as file:
        file.write(f"{username},{password},{nama},{akun}\n")
    print("Registrasi berhasil.")
    return True

def login(username, password):
    # Membaca file akun.txt dari folder 'login'
    try:
        with open("./akun.csv", "r") as file:
            for line in file:
                stored_username, stored_password, stored_nama, stored_akun = line.strip().split(",")
                if stored_username == username and stored_password == password:
                    print("Login berhasil.")
                    return { 
                        "username": stored_username, 
                        "name": stored_nama, 
                        "account_type": stored_akun
                    }  # Mengembalikan nama pengguna yang berhasil login
    except FileNotFoundError:
        print("File akun.csv tidak ditemukan.")
    print("Username atau password salah.")
    return None