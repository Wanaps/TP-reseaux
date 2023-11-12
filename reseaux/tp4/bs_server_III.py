import argparse
import socket
import logging
import time
# from colorama import Fore, Style
import colorlog

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--port", action="store", type=int, default="13337", help="specify the port to connect to")
args = parser.parse_args()

logging.basicConfig(filename='/var/log/bs_server/bs_server.log', encoding='utf-8', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

logger = colorlog.getLogger()

if (args.port < 0 or args.port > 65535):
    print("ERROR Le port spécifié n'est pas un port possible (de 0 à 65535).")
    exit(1)
elif (args.port >= 0 and args.port <= 1024):
    print("ERROR Le port spécifié est un port privilégié. Spécifiez un port au-dessus de 1024.")
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
last_activity_time = time.time()

try:
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break

            last_activity_time = time.time()

            logging.info(f"Le client {addr[0]} a envoyé {data.decode()}.")
            if data.decode() == "meo":
                response = "Meo à toi confrère."
            elif data.decode() == "waf":
                response = "ptdr t ki"
            else:
                response = "Mes respects humble humain."
            conn.sendall(response.encode())
            logging.info(f"Réponse envoyée au client {addr[0]} : {response}.")
    except socket.error:
        print("Erreur de connexion.")
finally:
    conn.close()
    s.close()


while True:
    current_time = time.time()
    elapsed_time = current_time - last_activity_time
    if elapsed_time >= 60:
        logging.info("Aucun client depuis plus d'une minute.")
        last_activity_time = current_time
    time.sleep(60)
