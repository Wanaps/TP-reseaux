import asyncio
import websockets

async def hello():
    uri = "ws://10.1.2.1:8888"
    async with websockets.connect(uri) as websocket:
        while True:
            msg = input("message to send : ")

            await websocket.send(msg)
            print(f">>> {msg}")

            greeting = await websocket.recv()
            print(f"<<< {greeting}")

if __name__ == "__main__":
    asyncio.run(hello())
