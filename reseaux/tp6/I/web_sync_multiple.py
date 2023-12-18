import sys
import requests as req
import time

path_to_write = "./demo/web_"

def read_content(file):
    with open(file, "r") as f:
        content = f.readlines()
        f.close()
    return content

def get_content(path_to_read):
    content = read_content(path_to_read)
    for url in content:
        url = url.strip()
        file = url.split("/")[-2]
        content = req.get(url)
        write_content(content, path_to_write + file)

def write_content(content, path_to_write):
    with open(path_to_write, "wb") as f:
        f.write(content.text.encode())
        f.close()
    
if __name__ == "__main__":
    time_start = time.time()
    if len(sys.argv) != 2:
        print("Usage: python3 web_sync.py <file_w/_urls>")
        sys.exit(1)
    path_to_read = sys.argv[1]
    get_content(path_to_read)
    print("Time taken: ", time.time() - time_start)