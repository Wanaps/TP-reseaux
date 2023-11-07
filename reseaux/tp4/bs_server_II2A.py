import argparse
import socket
import logging
import logging

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--port", action="store", type=int, default="13337", help="specify the port to connect to")
args = parser.parse_args()

logging.basicConfig(filename='/var/log/bs_server/bs_server.log', encoding='utf-8', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')


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
logging.info(f"Le serveur tourne sur {port}.")
s.listen(1)

conn, addr = s.accept()

print(f"Un client vient de se co et son IP c'est {addr[0]}.")
logging.info(f"Un client {addr[0]} s'est connecté.")

response = ""

while True:
    try:
        data = conn.recv(1024)
        if not data: break
        logging.info(f"Le client {addr[0]} a envoyé {data.decode()}.")
        if (data.decode() == "meo"):
            response = "Meo à toi confrère.".encode()
        elif (data.decode() == "waf"):
            response = "ptdr t ki".encode()
        else:
            response = "Mes respects humble humain.".encode()
    except socket.error:
        print("Erreur de connexion.")
        
conn.send(response)
logging.info(f"Réponse envoyée au client {addr[0]} : {response.decode()}.")

conn.close()