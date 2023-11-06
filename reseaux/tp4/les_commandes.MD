# les commandes réalisées ✨

## sur le serveur

- on clone une nouvelle vm et on met à jour :
```bash
[user@localhost ~]$ sudo dnf update -y
Last metadata expiration check: 0:35:43 ago on Mon Nov  6 10:37:04 2023.
Dependencies resolved.
Nothing to do.
Complete!
```
déjà à jour, quel bg!

- on installe python, git et tout:
```bash
[user@localhost ~]$ sudo dnf install python git
Last metadata expiration check: 0:36:28 ago on Mon Nov  6 10:37:04 2023.
Package python-unversioned-command-3.9.16-1.el9_2.2.noarch is already installed.
Package git-2.39.3-1.el9_2.x86_64 is already installed.
Dependencies resolved.
Nothing to do.
Complete!
```
bon ok je l'avais déjà fait mais c'est juste pour ajouter du contenu au compte rendu

- on lui ordonne son ip:

```bash
[user@localhost ~]$ cat /etc/sysconfig/network-scripts/ifcfg-enp0s8
NAME=enp0s8
DEVICE=enp0s8

BOOTPROTO=static
ONBOOT=yes

IPADDR=10.1.1.11
NETMASK=255.255.255.0
```

- on lui rafraîchit la tronche :
```bash
[user@localhost ~]$ sudo systemctl restart NetworkManager
[sudo] password for user:
[user@localhost ]$
```

- on vient chopper son ip:
```bash
[user@localhost tp4]$ ip a

[...]
3: enp0s8: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 08:00:27:e0:8c:11 brd ff:ff:ff:ff:ff:ff
    inet 10.1.1.11/24 brd 10.1.1.255 scope global noprefixroute enp0s8
       valid_lft forever preferred_lft forever
    inet6 fe80::a00:27ff:fee0:8c11/64 scope link
       valid_lft forever preferred_lft forever
```

- on ajoute le port t'as capté
```bash
[user@localhost ~]$ sudo firewall-cmd --add-port=13337/tcp --permanent
success
[user@localhost ~]$ sudo firewall-cmd --reload
success
```

- on check si c'est ok :
```bash
[user@localhost tp4]$ sudo firewall-cmd --list-all
public (active)
[...]
  ports: 13337/tcp 80/tcp
[...]
```
c'est good

- on choppe le répo, le code et on éxecute le code du serveur (je passe les détails)
```bash
[user@localhost tp4]$ python bs_server_I1.py

```
ça boucle !

- et voilà le grep de raisin 🍇 :
```bash
[user@localhost ~]$ ss -tlp | grep -i 13337
LISTEN 0      1            0.0.0.0:13337      0.0.0.0:*    users:(("python",pid=1509,fd=3))
```

## sur le client

- le même bordel que sur le serveur, on met à jour, on installe...

- on lui ordonne son ip :

```bash
[user@localhost ~]$ cat /etc/sysconfig/network-scripts/ifcfg-enp0s8
NAME=enp0s8
DEVICE=enp0s8

BOOTPROTO=static
ONBOOT=yes

IPADDR=10.1.1.13
NETMASK=255.255.255.0
```

