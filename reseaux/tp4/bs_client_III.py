import socket
import sys
import re
import logging

host = '10.1.1.11'
port = 13337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

logging.basicConfig(filename='/var/log/bs_server/bs_server.log', encoding='utf-8', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

s.connect((host, port))

print(f"Connecté avec succès au serveur {host} sur le port {port}")
logging.info(f"Connecté avec succès au serveur {host} sur le port {port}")

txt = input("Saisissez une opération arithmétique : ")

x = re.search('[0-9]+[+*-][0-9]+', txt)
# verify if the number is between -100000 and 100000


def check_op(operation):
    if not re.match(r'^-?\d+(?:\s*[+\-*]\s*-?\d+)+$', operation):
        logging.error("L'opération n'est pas une opération correcte.")
        raise TypeError("L'opération doit être une addition, une soustraction ou une multiplication.")

    nombres = re.findall(r'-?\d+', operation)

    for nombre in nombres:
        if not -100000 <= int(nombre) <= 100000:
            logging.error(f"Le nombre {nombre} n'est pas entre -100000 et 100000.")
            raise TypeError(f"Le nombre {nombre} n'est pas entre -100000 et 100000.")

check_op(txt)

if type(txt) != str:
    logging.error("L'opération n'est pas une string.")
    raise TypeError("Frère t'as pas mis une string")
elif x:
    pass
else:
    logging.error("L'opération n'est pas une opération correcte.")
    raise ValueError("Frère t'as pas mis une opération correcte")

try:
    s.sendall(txt.encode())
    logging.info(f"Envoi de l'opération {txt} au serveur.")
    data = s.recv(1024)
except socket.error:
    print("pas de bol anatole, ça a foiré")
    logging.error("Echec de l'envoi du message")
    sys.exit(1)


print(f"réponse : {repr(data.decode())}")

sys.exit(0)