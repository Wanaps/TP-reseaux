from os import system
from sys import argv

ping = "ping "
ip = argv[1]

command = ping + ip

system(command)