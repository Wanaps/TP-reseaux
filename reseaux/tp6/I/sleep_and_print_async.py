import asyncio as asy

async def main():
    for i in range(11):
        print(i)
        await asy.sleep(1)

loop = asy.get_event_loop()

tasks = [
    loop.create_task(main()),
    loop.create_task(main()),
]

if __name__ == "__main__":
    loop.run_until_complete(asy.wait(tasks))
    loop.close()