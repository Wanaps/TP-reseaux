# TP1 : Maîtrise réseau du poste

Pour ce TP, on va utiliser **uniquement votre poste** (pas de VM, rien, quedal, quetchi).

Le but du TP : se remettre dans le bain tranquillement en manipulant pas mal de concepts qu'on a vu l'an dernier.

C'est un premier TP *chill*, qui vous(ré)apprend à maîtriser votre poste en ce qui concerne le réseau. Faites le seul ou avec votre mate préféré bien sûr, mais jouez le jeu, faites vos propres recherches.

La "difficulté" va crescendo au fil du TP, mais la solution tombe très vite avec une ptite recherche Google si vos connaissances de l'an dernier deviennent floues.

- [TP1 : Maîtrise réseau du poste](#tp1--maîtrise-réseau-du-poste)
- [I. Basics](#i-basics)
- [II. Go further](#ii-go-further)
- [III. Le requin](#iii-le-requin)

# I. Basics

> Tout est à faire en ligne de commande, sauf si précision contraire.

☀️ **Carte réseau WiFi**

- l'adresse MAC de votre carte WiFi

 ```
(base) C:\Windows\system32>ipconfig /all

[...]
Wireless LAN adapter Wi-Fi:
   [...]
   Physical Address. . . . . . . . . : 70-1A-B8-1A-1E-DB
   [...]
   
[...]
``` 
- l'adresse IP de votre carte WiFi
```
(base) C:\Users\ecwan>ipconfig

[...]
Wireless LAN adapter Wi-Fi:
   [...]
   IPv4 Address. . . . . . . . . . . : 172.20.10.7
   [...]
[...]
```
- le masque de sous-réseau du réseau LAN auquel vous êtes connectés en WiFi
```
(base) C:\Users\ecwan>ipconfig

[...]
Wireless LAN adapter Wi-Fi:

   [...]
   Subnet Mask . . . . . . . . . . . : 255.255.255.240
   [...]
[...]
```
  - en notation CIDR, par exemple `/16`
  ```
/28
  ```
  - ET en notation décimale, par exemple `255.255.0.0`
  ```
  255.255.255.240
  ```


---

☀️ **Déso pas déso**

Pas besoin d'un terminal là, juste une feuille, ou votre tête, ou un tool qui calcule tout hihi. Déterminer...

- l'adresse de réseau du LAN auquel vous êtes connectés en WiFi
```
172.20.10.0
```
- l'adresse de broadcast
```
172.20.10.15
```
- le nombre d'adresses IP disponibles dans ce réseau
```
14
```

---

☀️ **Hostname**

- déterminer le hostname de votre PC
```
(base) C:\Users\ecwan>hostname
DESKTOP-0BJ32GT
```

---

☀️ **Passerelle du réseau**

Déterminer...

- l'adresse IP de la passerelle du réseau
```
(base) C:\Users\ecwan>ipconfig
[...]
   Default Gateway . . . . . . . . . : [...]
                                      172.20.10.1
   [...]
[...]
```
- l'adresse MAC de la passerelle du réseau
```
(base) C:\Users\ecwan>arp -a | findstr 172.20.10.1                                                                        172.20.10.1           6a-fe-f7-5b-22-64     dynamic
```

---

☀️ **Serveur DHCP et DNS**

Déterminer...

- l'adresse IP du serveur DHCP qui vous a filé une IP
```
(base) C:\Users\ecwan>ipconfig /all
[...]
Wireless LAN adapter Wi-Fi:
   [...]
   DHCP Server . . . . . . . . . . . : 172.20.10.1
   [...]
[...]
```
- l'adresse IP du serveur DNS que vous utilisez quand vous allez sur internet
```
(base) C:\Users\ecwan>ipconfig /all
[...]
Wireless LAN adapter Wi-Fi:
   [...]
   DNS Servers . . . . . . . . . . . : [...]
                                       172.20.10.1
   [...]
[...]
```

---

☀️ **Table de routage**

Déterminer...

- dans votre table de routage, laquelle est la route par défaut
```
(base) C:\Users\ecwan>route print
[...]
IPv4 Route Table
===========================================================================
Active Routes:
Network Destination        Netmask          Gateway       Interface  Metric
[...]
         0.0.0.0          0.0.0.0      172.20.10.1      172.20.10.7     55
[...]
```
---

![Not sure](./img/notsure.png)

# II. Go further

> Toujours tout en ligne de commande.

---

☀️ **Hosts ?**

- faites en sorte que pour votre PC, le nom `b2.hello.vous` corresponde à l'IP `1.1.1.1`
```
(base) C:\Windows\system32>echo 1.1.1.1 b2.hello.vous >> C:\Windows\System32\drivers\etc\hosts


(base) C:\Windows\system32>type C:\Windows\System32\drivers\etc\hosts
[...]
1.1.1.1 b2.hello.vous
```
- prouvez avec un `ping b2.hello.vous` que ça ping bien `1.1.1.1`
```
(base) C:\Windows\system32>ping b2.hello.vous

Pinging b2.hello.vous [1.1.1.1] with 32 bytes of data:
Reply from 1.1.1.1: bytes=32 time=44ms TTL=49
Reply from 1.1.1.1: bytes=32 time=77ms TTL=49
Reply from 1.1.1.1: bytes=32 time=73ms TTL=49
Reply from 1.1.1.1: bytes=32 time=69ms TTL=49

Ping statistics for 1.1.1.1:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 44ms, Maximum = 77ms, Average = 65ms
```

> Vous pouvez éditer en GUI, et juste me montrer le contenu du fichier depuis le terminal pour le compte-rendu.

---

☀️ **Go mater une vidéo youtube et déterminer, pendant qu'elle tourne...**

- l'adresse IP du serveur auquel vous êtes connectés pour regarder la vidéo
```
77.136.192.89
```
- le port du serveur auquel vous êtes connectés
```
443
```
- le port que votre PC a ouvert en local pour se connecter au port du serveur distant
```
61623
```

---

☀️ **Requêtes DNS**

Déterminer...

- à quelle adresse IP correspond le nom de domaine `www.ynov.com`
```
(base) C:\Windows\system32>nslookup www.ynov.com
Server:  UnKnown
Address:  fe80::68fe:f7ff:fe5b:2264

Non-authoritative answer:
Name:    www.ynov.com
Addresses:  2606:4700:20::ac43:4ae2
          2606:4700:20::681a:be9
          2606:4700:20::681a:ae9
          172.67.74.226
          104.26.11.233
          104.26.10.233
```

> Ca s'appelle faire un "lookup DNS".

- à quel nom de domaine correspond l'IP `174.43.238.89`
```
(base) C:\Windows\system32>nslookup 174.43.238.89
Server:  UnKnown
Address:  fe80::68fe:f7ff:fe5b:2264

Name:    89.sub-174-43-238.myvzw.com
Address:  174.43.238.89
```

> Ca s'appelle faire un "reverse lookup DNS".

---

☀️ **Hop hop hop**

Déterminer...

- par combien de machines vos paquets passent quand vous essayez de joindre `www.ynov.com`
```
(base) C:\Windows\system32>tracert www.ynov.com

Tracing route to www.ynov.com [2606:4700:20::ac43:4ae2]
over a maximum of 30 hops:

  1     2 ms     1 ms     1 ms  2a01:cb1a:7e:bb89:eda7:26a1:b5e:6df5
  2    44 ms    50 ms    45 ms  2a01:cb1a:7e:bb89:0:59:5779:4540
  3     *        *        *     Request timed out.
  4    73 ms    49 ms    43 ms  2a01:cd00:17f:101::10
  5    42 ms    42 ms    39 ms  2a01:cd00:17f:99::49
  6    30 ms    46 ms    70 ms  2a01:cd00:17f:99::54
  7    51 ms    54 ms    42 ms  2a01:cd00:17f:12::62
  8    76 ms    43 ms    49 ms  2a01:cd00:17f:13::65
  9    54 ms    52 ms    51 ms  2a01:cfc4:1000:3000::3
 10    49 ms    25 ms    61 ms  2a01:cfc0:200:8000:193:252:102:149
 11    54 ms    35 ms    39 ms  2a01:cfc0:200:8000:193:252:102:7
 12    47 ms    39 ms    39 ms  2a01:cfc0:200:8000:193:252:102:8
 13     *        *        *     Request timed out.
 14     *        *        *     Request timed out.
 15    86 ms    87 ms    80 ms  2001:688:0:3:8::21c
 16    68 ms    48 ms    73 ms  2400:cb00:534:3::
 17   122 ms    56 ms    57 ms  2606:4700:20::ac43:4ae2

Trace complete.
```

---

☀️ **IP publique**

Déterminer...

- l'adresse IP publique de la passerelle du réseau (le routeur d'YNOV donc si vous êtes dans les locaux d'YNOV quand vous faites le TP)
```
(base) C:\Users\ecwan>ipconfig /all | Select-String Wi-Fi -Context 0,9

Carte réseau sans fil Wi-Fi :

     Passerelle par défaut. . . . . . . . . : 10.33.79.254
```

---

☀️ **Scan réseau**

Déterminer...

- combien il y a de machines dans le LAN auquel vous êtes connectés
```
(base) C:\Windows\system32>arp -a

Interface: 172.20.10.7 --- 0x4
  Internet Address      Physical Address      Type
  172.20.10.1           6a-fe-f7-5b-22-64     dynamic
  172.20.10.15          ff-ff-ff-ff-ff-ff     static
  224.0.0.22            01-00-5e-00-00-16     static
  224.0.0.251           01-00-5e-00-00-fb     static
  224.0.0.252           01-00-5e-00-00-fc     static
  239.255.255.250       01-00-5e-7f-ff-fa     static
  255.255.255.255       ff-ff-ff-ff-ff-ff     static

Interface: 10.5.1.1 --- 0x7
  Internet Address      Physical Address      Type
  10.5.1.255            ff-ff-ff-ff-ff-ff     static
  224.0.0.22            01-00-5e-00-00-16     static
  224.0.0.251           01-00-5e-00-00-fb     static
  224.0.0.252           01-00-5e-00-00-fc     static
  239.255.255.250       01-00-5e-7f-ff-fa     static

Interface: 192.168.56.1 --- 0xe
  Internet Address      Physical Address      Type
  192.168.56.255        ff-ff-ff-ff-ff-ff     static
  224.0.0.22            01-00-5e-00-00-16     static
  224.0.0.251           01-00-5e-00-00-fb     static
  224.0.0.252           01-00-5e-00-00-fc     static
  239.255.255.250       01-00-5e-7f-ff-fa     static
  255.255.255.255       ff-ff-ff-ff-ff-ff     static
   ```

> Allez-y mollo, on va vite flood le réseau sinon. :)

![Stop it](./img/stop.png)

# III. Le requin

Faites chauffer Wireshark. Pour chaque point, je veux que vous me livrez une capture Wireshark, format `.pcap` donc.

Faites *clean* 🧹, vous êtes des grands now :

- livrez moi des captures réseau avec uniquement ce que je demande et pas 40000 autres paquets autour
  - vous pouvez sélectionner seulement certains paquets quand vous enregistrez la capture dans Wireshark
- stockez les fichiers `.pcap` dans le dépôt git et côté rendu Markdown, vous me faites un lien vers le fichier, c'est cette syntaxe :

```markdown
[Lien vers capture ARP](./captures/arp.pcap)
```

---

☀️ **Capture ARP**

- 📁 fichier `arp.pcap`
- capturez un échange ARP entre votre PC et la passerelle du réseau

[Capture](./img/arp.pcapng)

> Si vous utilisez un filtre Wireshark pour mieux voir ce trafic, précisez-le moi dans le compte-rendu.

---

☀️ **Capture DNS**

- 📁 fichier `dns.pcap`
- capturez une requête DNS vers le domaine de votre choix et la réponse
- vous effectuerez la requête DNS en ligne de commande

[Capture](./img/dns.pcapng)

> Si vous utilisez un filtre Wireshark pour mieux voir ce trafic, précisez-le moi dans le compte-rendu.

---

☀️ **Capture TCP**

- 📁 fichier `tcp.pcap`
- effectuez une connexion qui sollicite le protocole TCP
- je veux voir dans la capture :
  - un 3-way handshake
  - un peu de trafic
  - la fin de la connexion TCP

[Capture](./img/tcp.pcapng)

> Si vous utilisez un filtre Wireshark pour mieux voir ce trafic, précisez-le moi dans le compte-rendu.

---

![Packet sniffer](img/wireshark.jpg)

> *Je sais que je vous l'ai déjà servi l'an dernier lui, mais j'aime trop ce meme hihi 🐈*