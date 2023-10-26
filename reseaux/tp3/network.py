from os import system
from sys import argv
from socket import *

def find_command(arg) -> int:
    if (arg == 'ping'):
        return 1
    elif (arg == 'lookup'):
        return 2
    elif (arg == 'ip'):
        return 3
    else:
        return None

command = find_command(argv[1])
result = ""

def ping(arg) -> str:
    cmd = "ping " + arg + " > nul"

    if (system(cmd) == 0):
        return("UP !")
    else:
        return("DOWN !")

def ip() -> None:
    myHostName = gethostname()
    myIP = gethostbyname(myHostName)
    return(myIP)

def lookup(arg) -> str:
    return gethostbyname(arg)

match command:
    case 1:
        result = ping(argv[2])
    case 2:
        result = lookup(argv[2])
    case 3:
        result = ip()
    case None:
        result = "Déso frérot c'est non"

print(result)