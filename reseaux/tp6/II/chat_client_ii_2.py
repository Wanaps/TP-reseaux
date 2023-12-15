import socket
import sys

host = '127.0.0.1'
port = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))

s.sendall(b"Hello")

data = s.recv(1024)

s.close()

if not data:
    print("Pas de réponse.")
    sys.exit(-1)

print(f"réponse : {repr(data)}")

sys.exit(0)