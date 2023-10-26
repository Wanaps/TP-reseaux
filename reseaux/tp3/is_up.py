from os import system
from sys import argv

command = "ping " + argv[1] + " > nul"

if (system(command) == 0):
    print("UP !")
else:
    print("DOWN !")