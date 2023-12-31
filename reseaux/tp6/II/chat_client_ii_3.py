import asyncio
import aioconsole

ip = "127.0.0.1"
port = 8888

async def receive_messages(reader):
    while True:
        data = await reader.read(1024)
        if not data:
            break
        print(f"\n{data.decode()}\n>> ", end="")

async def send_message(writer):
    while True:
        message = await aioconsole.ainput(">> ")
        writer.write(message.encode())
        await writer.drain()

async def main():
    reader, writer = await asyncio.open_connection(ip, port)
    
    receive_task = asyncio.create_task(receive_messages(reader))
    send_task = asyncio.create_task(send_message(writer))
    
    await asyncio.gather(receive_task, send_task)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
    finally:
        print("\nClosing connection...")