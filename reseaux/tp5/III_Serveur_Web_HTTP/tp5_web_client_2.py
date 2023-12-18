import http.client as hc

page = input("Page à demander : ")

conn = hc.HTTPConnection("localhost", 8080)
conn.request("GET", page)
r1 = conn.getresponse()
print(r1.status, r1.reason)
data1 = r1.read()
print(data1)
conn.close()
