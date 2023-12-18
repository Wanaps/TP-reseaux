import socket
import re

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 9999))


msg = input("Calcul à envoyer: ")

if not "+" in msg and not "-" in msg and "*" not in msg:
    print("nope")
    exit(-1)

separators = r'[+\-* ]'

checker = msg.replace(" ", "")
msg = checker
checker = re.split(separators, checker)

if int(checker[0]) > 4294967295 or int(checker[1]) > 4294967295:
    print("Erreur, un des deux nombres est supérieur à 4294967295.")

msg = msg.encode()

length = len(msg)

header = length.to_bytes(4, byteorder='big')

final = header + msg

print(final)

s.send(final)
s.close()
