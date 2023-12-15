import asyncio

ip = "127.0.0.1"
port = 8888

# do a server with asyncronous functions. every message the server receive should be printed in the terminal like this "Message received from {IP}:{Port} : {msg}"

async def handle_packet(reader, writer):
    while True:

        data = await reader.read(1024)
        addr = writer.get_extra_info('peername')

        if data == b'':
            break

        message = data.decode()
        print(f"Message received from {addr[0]}:{addr[1]} : {message!r}")
        
        
async def main():
    server = await asyncio.start_server(handle_packet, ip, port)

    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
    print(f'Serving on {addrs}')

    async with server:
        await server.serve_forever()
        
if __name__ == "__main__":
    asyncio.run(main())