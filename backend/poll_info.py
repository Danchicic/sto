import asyncio

import aiohttp

async def poll_microservices():
    async with aiohttp.ClientSession() as session:
        while True:
            async with session.get("http://localhost:8120/items") as response:
                if response.status == 200:
                    print(response.status, await response.json())

            async with session.get("http://localhost:8121/") as response:
                if response.status == 200:
                    print(response.status, await response.json())

            await asyncio.sleep(10)


asyncio.run(poll_microservices())



