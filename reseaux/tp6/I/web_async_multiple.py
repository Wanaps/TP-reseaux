import sys
import aiohttp
import aiofiles
import asyncio
import time

path_to_write = "./demo/web_"

async def read_content(file):
    async with aiofiles.open(file, "r") as f:
        content = await f.readlines()
    return content

async def get_content(path_to_read):
    content = await read_content(path_to_read)
    async with aiohttp.ClientSession() as session:
        tasks = [process_url(session, url.strip()) for url in content]
        await asyncio.gather(*tasks)

async def process_url(session, url):
    async with session.get(url) as response:
        if response.status == 200:
            file = url.split("/")[-2]
            content = await response.text()
            await write_content(content, path_to_write + file)

async def write_content(content, path_to_write):
    async with aiofiles.open(path_to_write, "wb") as f:
        await f.write(content.encode())

async def main():
    if len(sys.argv) != 2:
        print("Usage: python3 web_sync.py <file_w/_urls>")
        return
    path_to_read = sys.argv[1]
    await get_content(path_to_read)

if __name__ == "__main__":
    time_start = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
    print("Time taken: ", time.time() - time_start)
