## Compte-rendu

☀️ Sur **`node1.lan1.tp2`**

- afficher ses cartes réseau
```bash
[user@node1 ~]$ ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: enp0s8: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 08:00:27:86:e6:b1 brd ff:ff:ff:ff:ff:ff
    inet 10.1.1.11/24 brd 10.1.1.255 scope global noprefixroute enp0s8
       valid_lft forever preferred_lft forever
    inet6 fe80::a00:27ff:fe86:e6b1/64 scope link
       valid_lft forever preferred_lft forever
```
- afficher sa table de routage
```bash
[user@node1 ~]$ ip r s
10.1.1.0/24 dev enp0s8 proto kernel scope link src 10.1.1.11 metric 100
```
- prouvez qu'il peut joindre `node2.lan2.tp2`
```bash
[user@node1 ~]$ ip r s
10.1.1.0/24 dev enp0s8 proto kernel scope link src 10.1.1.11 metric 100
10.1.2.0/24 via 10.1.1.254 dev enp0s8 proto static metric 100
```
- prouvez avec un `traceroute` que le paquet passe bien par `router.tp2`
```bash
[user@node1 ~]$ traceroute 10.1.2.12
traceroute to 10.1.2.12 (10.1.2.12), 30 hops max, 60 byte packets
 1  10.1.1.254 (10.1.1.254)  0.530 ms  0.526 ms  0.545 ms
 2  10.1.2.12 (10.1.2.12)  0.535 ms !X  0.458 ms !X  0.447 ms !X
```

# II. Interlude accès internet

![No internet](./img/no%20internet.jpg)

**On va donner accès internet à tout le monde.** Le routeur aura un accès internet, et permettra à tout le monde d'y accéder : il sera la passerelle par défaut des membres du LAN1 et des membres du LAN2.

**Ajoutez une carte NAT au routeur pour qu'il ait un accès internet.**

☀️ **Sur `router.tp2`**

- prouvez que vous avez un accès internet (ping d'une IP publique)
```bash
[user@router ~]$ ping 1.1.1.1
PING 1.1.1.1 (1.1.1.1) 56(84) bytes of data.
64 bytes from 1.1.1.1: icmp_seq=1 ttl=56 time=15.4 ms
64 bytes from 1.1.1.1: icmp_seq=2 ttl=56 time=12.7 ms
^C
--- 1.1.1.1 ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1002ms
rtt min/avg/max/mdev = 12.685/14.029/15.373/1.344 ms
```
- prouvez que vous pouvez résoudre des noms publics (ping d'un nom de domaine public)
```bash
[user@router ~]$ ping google.com
PING google.com (216.58.214.174) 56(84) bytes of data.
64 bytes from mad01s26-in-f14.1e100.net (216.58.214.174): icmp_seq=1 ttl=118 time=12.7 ms
64 bytes from mad01s26-in-f14.1e100.net (216.58.214.174): icmp_seq=2 ttl=118 time=15.4 ms
^C
--- google.com ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1003ms
rtt min/avg/max/mdev = 12.702/14.072/15.443/1.370 ms
```

☀️ **Accès internet LAN1 et LAN2**

- ajoutez une route par défaut sur les deux machines du LAN1
```bash
[user@node1 ~]$ ip r s
default via 10.1.1.254 dev enp0s8 proto static metric 100
[...]
```
- ajoutez une route par défaut sur les deux machines du LAN2
```bash
[user@node1 ~]$ ip r s
default via 10.1.2.254 dev enp0s8 proto static metric 100
[...]
```
- configurez l'adresse d'un serveur DNS que vos machines peuvent utiliser pour résoudre des noms 
```bash

[user@node1 ~]$ cat /etc/sysconfig/network-scripts/ifcfg-enp0s8
NAME=enp0s8
DEVICE=enp0s8

BOOTPROTO=static
ONBOOT=yes

IPADDR=10.1.2.11
NETMASK=255.255.255.0

GATEWAY=10.1.2.254
DNS1=1.1.1.1
```
- dans le compte-rendu, mettez-moi que la conf des points précédents sur `node2.lan1.tp2`
- prouvez que `node2.lan1.tp2` a un accès internet :
  - il peut ping une IP publique
```bash
[user@node2 ~]$ ping 1.1.1.1
PING 1.1.1.1 (1.1.1.1) 56(84) bytes of data.
64 bytes from 1.1.1.1: icmp_seq=1 ttl=54 time=13.2 ms
64 bytes from 1.1.1.1: icmp_seq=2 ttl=54 time=16.2 ms
^C
--- 1.1.1.1 ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1002ms
rtt min/avg/max/mdev = 13.229/14.690/16.152/1.461 ms
```
  - il peut ping un nom de domaine public
```bash
[user@node2 ~]$ ping google.com
PING google.com (216.58.215.46) 56(84) bytes of data.
64 bytes from par21s17-in-f14.1e100.net (216.58.215.46): icmp_seq=1 ttl=118 time=14.2 ms
64 bytes from par21s17-in-f14.1e100.net (216.58.215.46): icmp_seq=2 ttl=118 time=12.1 ms
^C
--- google.com ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1002ms
rtt min/avg/max/mdev = 12.144/13.195/14.247/1.051 ms
```

## 1. DHCP

Pour ce qui est de la configuration du serveur DHCP, quelques précisions :

- vous ferez en sorte qu'il propose des adresses IPs entre `10.1.1.100` et `10.1.1.200`
- vous utiliserez aussi une option DHCP pour indiquer aux clients que la passerelle du réseau est `10.1.1.254` : le routeur
- vous utiliserez aussi une option DHCP pour indiquer aux clients qu'un serveur DNS joignable depuis le réseau c'est `1.1.1.1`

---

☀️ **Sur `dhcp.lan1.tp2`**

- n'oubliez pas de renommer la machine (`node2.lan1.tp2` devient `dhcp.lan1.tp2`)
```bash
[user@node2 ~]$ cat /etc/hostname
dhcp.lan1.tp2
```
- changez son adresse IP en `10.1.1.253`
```bash
[user@dhcp ~]$ cat /etc/sysconfig/network-scripts/ifcfg-enp0s8
NAME=enp0s8
DEVICE=enp0s8

BOOTPROTO=static
ONBOOT=yes

IPADDR=10.1.1.253
NETMASK=255.255.255.0

GATEWAY=10.1.2.254
DNS1=1.1.1.1
```
- setup du serveur DHCP
  - commande d'installation du paquet
```bash
  [user@dhcp ~]$ sudo dnf -y install dhcp-server
```
  - fichier de conf
```bash
[user@dhcp ~]$ sudo /etc/dhcp/dhcpd.conf
sudo cat /etc/dhcp/dhcpd.conf
# create new
# specify domain name
option domain-name     "lan1.tp2";
# specify DNS server's hostname or IP address
option domain-name-servers     dhcp.lan1.tp2;
# default lease time
default-lease-time 600;
# max lease time
max-lease-time 7200;
# this DHCP server to be declared valid
authoritative;
# specify network address and subnetmask
subnet 10.1.1.0 netmask 255.255.255.0 {
    # specify the range of lease IP address
    range dynamic-bootp 10.1.1.100 10.1.1.200;
    # specify broadcast address
    option broadcast-address 10.1.1.255;
    # specify gateway
    option routers 10.1.1.254;
```
  - service actif
```bash
  [user@dhcp ~]$ systemctl status dhcpd
● dhcpd.service - DHCPv4 Server Daemon
     Loaded: loaded (/usr/lib/systemd/system/dhcpd.service; enabled; preset: di>
     Active: active (running) since Tue 2023-10-24 22:25:24 CEST; 1min 23s ago
       Docs: man:dhcpd(8)
             man:dhcpd.conf(5)
   Main PID: 1785 (dhcpd)
     Status: "Dispatching packets..."
      Tasks: 1 (limit: 4611)
     Memory: 5.2M
        CPU: 8ms
     CGroup: /system.slice/dhcpd.service
             └─1785 /usr/sbin/dhcpd -f -cf /etc/dhcp/dhcpd.conf -user dhcpd -gr>
Oct 24 22:25:24 node2.lan1.tp2 dhcpd[1785]: Config file: /etc/dhcp/dhcpd.conf
Oct 24 22:25:24 node2.lan1.tp2 dhcpd[1785]: Database file: /var/lib/dhcpd/dhcpd>
Oct 24 22:25:24 node2.lan1.tp2 dhcpd[1785]: PID file: /var/run/dhcpd.pid
Oct 24 22:25:24 node2.lan1.tp2 dhcpd[1785]: Source compiled to use binary-leases
Oct 24 22:25:24 node2.lan1.tp2 dhcpd[1785]: Wrote 0 leases to leases file.
```

☀️ **Sur `node1.lan1.tp2`**

- demandez une IP au serveur DHCP
```bash
[user@node1 ~]$ cat /etc/sysconfig/network-scripts/ifcfg-enp0s8
NAME=enp0s8
DEVICE=enp0s8

BOOTPROTO=dhcp
ONBOOT=yes
```
- prouvez que vous avez bien récupéré une IP *via* le DHCP
```bash
[user@node1 ~]$ ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: enp0s8: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 08:00:27:86:e6:b1 brd ff:ff:ff:ff:ff:ff
    inet 10.1.1.100/24 brd 10.1.1.255 scope global dynamic noprefixroute enp0s8
       valid_lft 542sec preferred_lft 542sec
    inet6 fe80::a00:27ff:fe86:e6b1/64 scope link
       valid_lft forever preferred_lft forever
```
- prouvez que vous avez bien récupéré l'IP de la passerelle
```bash
[user@node1 ~]$ ip r s
default via 10.1.1.254 dev enp0s8 proto dhcp src 10.1.1.100 metric 100
10.1.1.0/24 dev enp0s8 proto kernel scope link src 10.1.1.100 metric 100
10.1.2.0/24 via 10.1.1.254 dev enp0s8 proto static metric 100
```
- prouvez que vous pouvez `ping node1.lan2.tp2`
```bash
[user@node1 ~]$ ping 10.1.2.11
PING 10.1.2.11 (10.1.2.11) 56(84) bytes of data.
64 bytes from 10.1.2.11: icmp_seq=1 ttl=63 time=0.774 ms
64 bytes from 10.1.2.11: icmp_seq=2 ttl=63 time=0.703 ms
^C
--- 10.1.2.11 ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1050ms
rtt min/avg/max/mdev = 0.703/0.738/0.774/0.035 ms
```

## 2. Web web web

Un petit serveur web ? Pour la route ?

On recycle ici, toujours dans un soucis d'économie de ressources, la machine `node2.lan2.tp2` qui devient `web.lan2.tp2`. On va y monter un serveur Web qui mettra à disposition un site web tout nul.

---

☀️ **Sur `web.lan2.tp2`**

- n'oubliez pas de renommer la machine (`node2.lan2.tp2` devient `web.lan2.tp2`)
```bash
[user@web ~]$ hostname
web.lan2.tp2
```
- setup du service Web
  - installation de NGINX
```bash
[user@web ~]$ sudo dnf install nginx
[...]
Complete!
[user@web ~]$ sudo systemctl enable --now nginx
Created symlink /etc/systemd/system/multi-user.target.wants/nginx.service → /usr/lib/systemd/system/nginx.service.
```
  - gestion de la racine web `/var/www/site_nul/`
```bash
[user@web ~]$ cat /var/www/site_nul/index.html
<html>
  <head>
    <title>My Website</title>
  </head>
  <body>
    <h1>Welcome To My Website!</h1>
  </body>
</html>
```
  - configuration NGINX
```bash
[user@web ~]$ cat /etc/nginx/nginx.conf
# For more information on configuration, see:
#   * Official English Documentation: http://nginx.org/en/docs/
#   * Official Russian Documentation: http://nginx.org/ru/docs/

user nginx;
worker_processes auto;
error_log /var/log/nginx/error.log;
pid /run/nginx.pid;

# Load dynamic modules. See /usr/share/doc/nginx/README.dynamic.
include /usr/share/nginx/modules/*.conf;

events {
    worker_connections 1024;
}

http {
    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    access_log  /var/log/nginx/access.log  main;

    sendfile            on;
    tcp_nopush          on;
    tcp_nodelay         on;
    keepalive_timeout   65;
    types_hash_max_size 4096;

    include             /etc/nginx/mime.types;
    default_type        application/octet-stream;

    # Load modular configuration files from the /etc/nginx/conf.d directory.
    # See http://nginx.org/en/docs/ngx_core_module.html#include
    # for more information.
    include /etc/nginx/conf.d/*.conf;

    server {
        listen       80;
        listen       [::]:80;
        server_name  site_nul.tp2;
        location / {
                root /var/www/site_nul;
                index index.html
        root         /usr/share/nginx/html;
        }

        # Load configuration files for the default server block.
        include /etc/nginx/default.d/*.conf;

        error_page 404 /404.html;
        location = /404.html {
        }

        error_page 500 502 503 504 /50x.html;
        location = /50x.html {
        }
    }

# Settings for a TLS enabled server.
#
#    server {
#        listen       443 ssl http2;
#        listen       [::]:443 ssl http2;
#        server_name  _;
#        root         /usr/share/nginx/html;
#
#        ssl_certificate "/etc/pki/nginx/server.crt";
#        ssl_certificate_key "/etc/pki/nginx/private/server.key";
#        ssl_session_cache shared:SSL:1m;
#        ssl_session_timeout  10m;
#        ssl_ciphers PROFILE=SYSTEM;
#        ssl_prefer_server_ciphers on;
#
#        # Load configuration files for the default server block.
#        include /etc/nginx/default.d/*.conf;
#
#        error_page 404 /404.html;
#            location = /40x.html {
#        }
#
#        error_page 500 502 503 504 /50x.html;
#            location = /50x.html {
#        }
#    }

}
```

  - service actif
```bash
  [user@web ~]$ sudo systemctl status nginx
● nginx.service - The nginx HTTP and reverse proxy server
     Loaded: loaded (/usr/lib/systemd/system/nginx.service; enabled; preset: disabled)
     Active: active (running) since Wed 2023-10-25 19:27:09 CEST; 38min ago
   Main PID: 1475 (nginx)
      Tasks: 2 (limit: 4611)
     Memory: 2.0M
        CPU: 15ms
     CGroup: /system.slice/nginx.service
             ├─1475 "nginx: master process /usr/sbin/nginx"
             └─1476 "nginx: worker process"

Oct 25 19:27:09 web.lan2.tp2 systemd[1]: Starting The nginx HTTP and reverse proxy server...
Oct 25 19:27:09 web.lan2.tp2 nginx[1473]: nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
Oct 25 19:27:09 web.lan2.tp2 nginx[1473]: nginx: configuration file /etc/nginx/nginx.conf test is successful
Oct 25 19:27:09 web.lan2.tp2 systemd[1]: Started The nginx HTTP and reverse proxy server.
```
  - ouverture du port firewall
```bash
[user@web ~]$ sudo firewall-cmd --add-port=80/tcp --permanent
success
```
- prouvez qu'il y a un programme NGINX qui tourne derrière le port 80 de la machine (commande `ss`)
```bash
[user@web ~]$ sudo ss -nplat | grep nginx
LISTEN 0      511          0.0.0.0:80        0.0.0.0:*     users:(("nginx",pid=1476,fd=6),("nginx",pid=1475,fd=6))
LISTEN 0      511             [::]:80           [::]:*     users:(("nginx",pid=1476,fd=7),("nginx",pid=1475,fd=7))
```
- prouvez que le firewall est bien configuré
```bash
[user@web ~]$ sudo firewall-cmd --list-all
public (active)
  target: default
  icmp-block-inversion: no
  interfaces: enp0s8
  sources:
  services: cockpit dhcpv6-client http ssh
  ports: 80/tcp
  protocols:
  forward: yes
  masquerade: no
  forward-ports:
  source-ports:
  icmp-blocks:
  rich rules:
```

☀️ **Sur `node1.lan1.tp2`**

- éditez le fichier `hosts` pour que `site_nul.tp2` pointe vers l'IP de `web.lan2.tp2`
```bash
[user@node1 ~]$ cat /etc/hosts
127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4
::1         localhost localhost.localdomain localhost6 localhost6.localdomain6
10.1.2.12 web.lan2.tp2 site_nul.tp2
```
- visitez le site nul avec une commande `curl` et en utilisant le nom `site_nul.tp2`
```bash
[user@node1 ~]$ curl site_nul.tp2
<html>
  <head>
    <title>My Website</title>
  </head>
  <body>
    <h1>Welcome To My Website!</h1>
  </body>
</html>
```

![That's all folks](./img/thatsall.jpg)