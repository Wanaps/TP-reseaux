import asyncio as aio
import aioconsole as aioc

ip = "10.1.1.13"
port = 8888

async def get_input():
    msg = await aioc.ainput(">> ")
    return msg.encode()

async def send_message(msg, writer):
    writer.write(msg)
    await writer.drain()

async def connect():
    reader, writer = await aio.open_connection(host="127.0.0.1", port=8888)
    await send_message(await get_input(), writer)


async def main():
    while True:
        await connect()
    
if __name__ == "__main__":
    aio.run(main())