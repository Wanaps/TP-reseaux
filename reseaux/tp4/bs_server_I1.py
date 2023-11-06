import socket

host = ''
port = 13337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))

s.listen(1)
conn, addr = s.accept()
print('Connected by', addr)

while True:

    try:
        data = conn.recv(1024)
        if not data: break
        print(f"Données reçues: {data}")
        conn.sendall("Salut mec.")

    except socket.error:
        print("Erreur de connexion.")
        break

conn.close()

# dans la vm :
#
# [user@localhost tp4]$ sudo firewall-cmd --add-port=13337/tcp --permanent
# [sudo] password for user:
# success