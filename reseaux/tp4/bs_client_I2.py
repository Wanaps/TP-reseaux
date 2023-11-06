import socket
import sys
import re

host = '10.1.1.11'
port = 13337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))

txt = input("Que veux-tu envoyer au serveur : ")

x = re.search('meo|waf', txt)

if (txt.type() != str):
    print("frère c'est pas une string")
    sys.exit(1)
elif (x):
    pass
else:
    print("il faut que tu mettes soit 'meo' soit 'waf' poto")
    sys.exit(1)


try:
    s.sendall(txt.encode())
    data = s.recv(1024)
    print(f"Connecté avec succès au serveur {host} sur le port {port}")
except socket.error:
    print("pas de bol anatole, ça a foiré")
    sys.exit(1)


print(f"réponse : {repr(data.decode())}")

sys.exit(0)