import asyncio

ip = '127.0.0.1'
port = 8888

global CLIENTS
CLIENTS = {}

def add_client(reader, writer):
    if not CLIENTS.get(writer.get_extra_info('peername')):
        CLIENTS[writer.get_extra_info('peername')] = {}
        CLIENTS[writer.get_extra_info('peername')]["r"] = reader
        CLIENTS[writer.get_extra_info('peername')]["w"] = writer
        print(f"Client {writer.get_extra_info('peername')} added.")
    
async def send_to_all(message, addr):
    encoded = message.encode()
    for client in CLIENTS:
        if client != addr:
            print(f"Sending {message} to {client}")
            send = f"{addr[0]}:{addr[1]} a dit : {encoded!r}"
            CLIENTS[client]["w"].write(send.encode())
            await CLIENTS[client]["w"].drain()
            print(f"Message sent to {client} : {message}")

async def handle_client_msg(reader, writer):
    add_client(reader, writer)
    while True:

        data = await reader.read(1024)
        addr = writer.get_extra_info('peername')

        if data == b'':
            break

        message = data.decode()
        print(f"Message received {addr[0]}:{addr[1]} : {message}")
        
        await send_to_all(message, addr)

async def main():
    server = await asyncio.start_server(handle_client_msg, ip, port)

    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
    print(f'Serving on {addrs}')

    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())