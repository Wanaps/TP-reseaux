import argparse
import socket

parser = argparse.ArgumentParser()

parser.add_argument("-p", "--port", action="store", type=int, default="13337", help="specify the port to connect to")

args = parser.parse_args()

if (args.port < 0 or args.port > 65535):
    print("ERROR Le port spécifié n'est pas un port possible (de 0 à 65535).")
    exit(1)
elif (args.port >= 0 and args.port <= 1024):
    print("ERROR Le port spécifié est un port privilégié. Spécifiez un port au dessus de 1024.")
    exit(2)

host = ''
port = args.port
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
        elif (data.decode() == "waf"):
            conn.sendall("ptdr t ki".encode())
        else:
            conn.sendall("Mes respects humble humain.".encode())

    except socket.error:
        print("Erreur de connexion.")
        
conn.close()