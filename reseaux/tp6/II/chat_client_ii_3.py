import asyncio as aio
import aioconsole as aioc

ip = "127.0.0.1"
port = 8888


async def get_input():
    msg = await aioc.ainput(">> ")
    return msg.encode()

async def send_message(msg, writer):
    writer.write(msg)
    await writer.drain()

async def connect():
    print(f"Trying to connect to {ip}:{port}")
    reader, writer = await aio.open_connection(host=ip, port=port)
    print("Connected.")
    while True:
        await send_message(await get_input(), writer)

async def main():
    await connect()
    
if __name__ == "__main__":
    aio.run(main())