from websockets.asyncio.server import serve
import server.auth.auth as auth
import json

async def handleMessage(websocket):
    raw_message = await websocket.recv()
    message = json.loads(raw_message)

    if (message["type"] == "login"):
        print("Dapat request login")
        hasil = auth.login(message["username"], message["password"])
        if (hasil == None):
            pesan_balas = {
                "type": "reply_login",
                "result": "failed"
            }
            await websocket.send(json.dumps(pesan_balas))
        else:
            pesan_balas = {
                "type": "reply_login",
                "result": "success",
                **hasil
            }
            await websocket.send(json.dumps(pesan_balas))
    elif (message["type"] == "register"):
        print("Dapat request register")
        hasil = auth.register(message["username"], message["password"], message["name"], message["account_type"])
        if (hasil == False):
            pesan_balas = {
                "type": "reply_register",
                "result": "failed"
            }
            await websocket.send(json.dumps(pesan_balas))
        else:
            pesan_balas = {
                "type": "reply_register",
                "result": "success"
            }
            await websocket.send(json.dumps(pesan_balas))

async def start():
     async with serve(handleMessage, "localhost", 8222) as server:
        await server.serve_forever()