# j'ai fait le tp sur windows et j'avais la flemme de trouver les fichiers tmp et tout
# mais en gros faut juste modifier 'path' pour le chemin tmp, je montre juste que j'ai compris le tp :')

import sys
import requests as req

path = "./sync_index.html"

def get_content(url):
    content = req.get(url)
    return content

def write_content(content, file):
    with open(file, "wb") as f:
        f.write(content.text.encode())
        f.close()
    
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 web_sync.py <url>")
        sys.exit(1)
    url = sys.argv[1]
    write_content(get_content(url), path)