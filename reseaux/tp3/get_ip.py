import psutil
from socket import *
from sys import argv

myHostName = gethostname()
myIP = gethostbyname(myHostName)
print(myIP)