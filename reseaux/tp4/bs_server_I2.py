import socket

host = ''
port = 13337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))

s.listen(1)
conn, addr = s.accept()
print(f"Un client vient de se co et son IP c'est {addr[0]}.")

while True:

    try:
        data = conn.recv(1024)
        if not data: break
        if (data.decode() == "meo"):
            conn.sendall("Meo à toi confrère.".encode())
            break
        elif (data.decode() == "waf"):
            conn.sendall("ptdr t ki".encode())
            break
        else:
            conn.sendall("Mes respects humble humain.".encode())

    except socket.error:
        print("Erreur de connexion.")
        break

conn.close()
