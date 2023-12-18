# j'ai fait le tp sur windows et j'avais la flemme de trouver les fichiers tmp et tout
# mais en gros faut juste modifier 'path' pour le chemin tmp, je montre juste que j'ai compris le tp :')

import asyncio as aio
import aiohttp as ahttp
import aiofiles as afiles
import sys

path = "./async_index.html"

async def get_content(url):
    async with ahttp.ClientSession() as session:
        async with session.get(url) as resp:
            content = await resp.read()
    return content

async def write_content(content, file):
    async with afiles.open(file, "wb") as f:
        await f.write(content)
        await f.close()
    
loop = aio.new_event_loop()

    
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 web_sync.py <url>")
        sys.exit(1)
    url = sys.argv[1]
    try:
        loop.run_until_complete(write_content(loop.run_until_complete(get_content(url)), path))
    except Exception as e:
        print(f"An error occurred: {e}")
