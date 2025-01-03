import csv

from semua.file.lokasi_file import lokasi_file


def register(username, password, name, account_type):
    # Membuat folder 'login' jika belum ada
    # os.makedirs("login", exist_ok=True)
    # Menyimpan file akun.txt di dalam folder 'login'

    # Cek apabila sudah ada akun dengan username yang sama
    with open(lokasi_file["akun"], "r") as file:
        data_akun = list(csv.reader(file))
        for _, baris in enumerate(data_akun):
            if baris[0] == username:
                print("Sudah ada akun dengan username yang sama")
                return False

    with open(lokasi_file["akun"], "a") as file:
        file.write(f"{username},{password},{name},{account_type}\n")
    print("Registrasi berhasil.")
    return True

def login(username, password):
    # Membaca file akun.txt dari folder 'login'
    try:
        with open(lokasi_file["akun"], "r") as file:
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


# Program utama
def authenticate():
    while True:
        pilihan = input("Pilih 'register' atau 'login': ").strip().lower()
        if pilihan == "register":
            username = input("Masukkan username: ").strip()
            if username == "":
                print("Username tidak boleh kosong!")
                continue

            password = input("Masukkan password: ").strip()
            if password == "" or len(password) < 8:
                print("Password tidak boleh kosong dan harus lebih dari 8!")
                continue

            nama = input("Masukkan nama lengkap: ")
            if nama == "":
                print("Nama tidak boleh kosong!")
                continue

            akun = input("Tipe akun? 'mitra' atau 'pelanggan':").strip().lower() 

            if akun != "mitra" and akun != "pelanggan":
                print("Tipe akun hanya bisa 'mitra' atau 'pelanggan'")
            else: 
                hasil = register(username, password, nama, akun)
                if hasil == True:
                    print("Register berhasil")
                else:
                    print("Register gagal")
        elif pilihan == "login":
            username = input("Masukkan username: ")
            password = input("Masukkan password: ")
            hasil = login(username, password)  # Menyimpan hasil login di variabel nama
            if hasil != None:
                # Menampilkan pesan selamat datang setelah login berhasil
                print(f"Selamat datang di JusTip, {hasil["name"]}\n")
                return hasil
            else:
                print(f"Username atau password salah\n")
        else:
            print("Pilihan tidak valid.")