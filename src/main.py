import asyncio
import sys
import shared.geolocation as geo
import shared.panic as pa
import server.server as server
import shared.login.log as auth
from shared.communicator.socket import SocketCommunicator

async def main():
    if (len(sys.argv) > 1 and sys.argv[1] == "--server"):
        await server.start()
    else:
        communicator = SocketCommunicator()
        await communicator.start("ws://localhost:8222")

        data_akun = await auth.authenticate()
        print(f"Nama: {data_akun.name}")
        print(f"Tipe akun: {data_akun.account_type}")

if __name__ == "__main__":
    # Bypass exception handling dahulu karena masih dalam tahap pengembangan
    pa.bypass_handling = True
    sys.excepthook = pa.except_hook
    asyncio.run(main())
