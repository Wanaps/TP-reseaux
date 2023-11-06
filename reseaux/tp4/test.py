import re


string = "cat dadad waf cat"

x = re.search('meo|waf', string)

# check if x is null

if (x):
    print("frère t'as mis un mot interdit")
else:
    print("frère t'as mis un mot autorisé")