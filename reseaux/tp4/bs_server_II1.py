import argparse
import socket
import sys
import re

parser = argparse.ArgumentParser()

parser.add_argument("-p", "--port", action="store", type=int, default="13337", help="specify the port to connect to")

args = parser.parse_args()

if (args.port < 0 or args.port > 65535):
    print("ERROR Le port spécifié n'est pas un port possible (de 0 à 65535).")
    exit(1)
elif (args.port >= 0 and args.port <= 1024):
    print("ERROR Le port spécifié est un port privilégié. Spécifiez un port au dessus de 1024.")
    exit(2)

host = '10.1.1.11'
port = args.port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))

txt = input("Que veux-tu envoyer au serveur : ")

x = re.search('meo|waf', txt)

if (type(txt) != str):
    raise TypeError("Frère t'as pas mis une string")
elif (x):
    pass
else:
    raise ValueError("Frère t'as pas mis un mot correct")

try:
    s.sendall(txt.encode())
    data = s.recv(1024)
    print(f"Connecté avec succès au serveur {host} sur le port {port}")
except socket.error:
    print("pas de bol anatole, ça a foiré")
    sys.exit(1)


print(f"réponse : {repr(data.decode())}")

sys.exit(0)