import semua.login.log as login

data_akun = login.authenticate()
print(f"Nama: {data_akun["name"]}")
print(f"Tipe akun: {data_akun["account_type"]}")

