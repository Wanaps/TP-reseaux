import asyncio
import websockets

ip = "127.0.0.1"
port = 8888

async def hello(websocket):
    msg = await websocket.recv()
    print(f"<<< {msg}")
    greeting = f"Hello client ! Received {msg}"
    await websocket.send(greeting)
    print(f">>> {greeting}")


async def main():
    async with websockets.serve(hello, ip, port):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
