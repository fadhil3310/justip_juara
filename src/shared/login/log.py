

def register(username, password, nama):
    # Membuka file akun.txt dalam mode append (menambahkan data di akhir file)
    with open("akun.txt", "a") as file:
        # Menulis username, password, dan nama ke dalam file
        file.write(f"{username},{password},{nama}\n")
    print("Registrasi berhasil.")

def login(username, password):
    # Membuka file akun.txt dalam mode baca
    try:
        with open("akun.txt", "r") as file:
            # Membaca setiap baris dalam file
            for line in file:
                # Memisahkan baris berdasarkan koma
                stored_username, stored_password, stored_nama = line.strip().split(",")
                # Memeriksa kecocokan username dan password
                if stored_username == username and stored_password == password:
                    print("Login berhasil.")
                    return stored_nama  # Mengembalikan nama pengguna yang berhasil login
    except FileNotFoundError:
        print("File akun.txt tidak ditemukan.")
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
        register(username, password, nama)
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
