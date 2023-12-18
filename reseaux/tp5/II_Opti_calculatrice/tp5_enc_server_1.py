import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('127.0.0.1', 9999))

s.listen()
conn, addr = s.accept()
print("Connecté")

while True:

    try:
        header = conn.recv(4)
        if not header: break
        length = int.from_bytes(header[0:4])
        print(f"Lecture des {length} prochains octets")

        chunks = []

        b_received = 0

        while b_received < length:
            chunk = conn.recv(min(length - b_received, 1024))

            if not chunk:
                raise RuntimeError("nope frérot ça marche pas")
            
            chunks.append(chunk)

            b_received += len(chunk)

    except socket.error:
        print("Error Occured.")
        break

    m_received = b"".join(chunks).decode('utf-8')
    print(f"Received from client {m_received}")

conn.close()
s.close()
    