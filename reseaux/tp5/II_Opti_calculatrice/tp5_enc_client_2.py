import socket
import re

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 9999))
msg = input("Calcul à envoyer: ")

# if not "+" in msg or not "-" in msg or not "*" in msg:
#     print("Votre opération doit être une addition, soustraction ou multiplication")
#     exit(-1)

separators = r'[+\-*]'

checker = msg.replace(" ", "")
checker = re.split(separators, checker)
first = int(checker[0])
second = int(checker[1])
print(f"{type(first)} : {first}")

print(f"{type(second)} : {second}")

if int(checker[0]) > 4294967295 or int(checker[1]) > 4294967295:
    print("Erreur, l'opération n'est apparement pas valide.")

length = first.bit_length()

header = length.to_bytes(4, byteorder='big')

first = first.to_bytes(1, byteorder="little")

final = header + first

print(f"sending {final}")

s.send(final)
s.close()
