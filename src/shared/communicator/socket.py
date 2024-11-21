from websockets.asyncio.client import connect, ClientConnection

class SocketCommunicatorMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
    
class SocketCommunicator(metaclass=SocketCommunicatorMeta):
    async def start(self, url):
        self.websocket = await connect(url)
        # self.pingPong()

    # async def pingPong(self):
    #     self.websocket.ping()
