import aiohttp
import asyncio
import json

datasend = {"name": "Bob", "age": 27, "city": "Oakland"}


async def fetch(session, url):
    print("Wait for server response...")
    async with session.request(method="POST", url=url, data=json.dumps(datasend)) as response:
        return await response.text()


async def main():
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
        html = await fetch(session, 'http://127.0.0.1:8080/')
        print(html)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())