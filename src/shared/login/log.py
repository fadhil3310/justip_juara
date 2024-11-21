
import json
import os
import asyncio

from websockets.asyncio.client import connect
from shared.communicator.socket import SocketCommunicator


class DataAkun:
    def __init__(self, username, name, account_type):
        self.username: username
        self.name: name
        self.account_type: account_type


async def register(username, password, name, account_type):
    communicator = SocketCommunicator()

    pesan = {
        "type": "register",
        "username": username,
        "password": password,
        "name": name,
        "account_type": account_type
    }
    await communicator.websocket.send(json.dumps(pesan))

    raw_hasil = await communicator.websocket.recv()
    hasil = json.loads(raw_hasil)
    if (hasil == None or (hasil["type"] == "reply_register" and hasil["result"] == "failed")):
        return False
    else:
        return True

async def login(username, password) -> DataAkun | None:
    communicator = SocketCommunicator()

    pesan = {
        "type": "login",
        "username": username,
        "password": password
    }
    await communicator.websocket.send(json.dumps(pesan))

    raw_hasil = await communicator.websocket.recv()
    hasil = json.loads(raw_hasil)
    if (hasil == None or (hasil["type"] == "reply_login" and hasil["result"] == "failed")):
        return None
    else:
        return DataAkun(hasil["username"], hasil["password"], hasil["account_type"])


# Program utama
async def authenticate() -> DataAkun | None:
    communicator = SocketCommunicator()

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
                hasil = register(username, password, nama, akun)
                if hasil == True:
                    print("Register berhasil")
                else:
                    print("Register gagal")
        elif pilihan == "login":
            username = input("Masukkan username: ")
            password = input("Masukkan password: ")
            hasil = await login(username, password)  # Menyimpan hasil login di variabel nama
            if hasil != None:
                # Menampilkan pesan selamat datang setelah login berhasil
                print(f"Selamat datang di JusTip, {nama}\n")
                return hasil
            else:
                print(f"Username atau password salah\n")
                # Reconnect ke server
                # await communicator.start("ws://localhost:8222")
        else:
            print("Pilihan tidak valid.")

    