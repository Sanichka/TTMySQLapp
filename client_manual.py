import aiohttp
import asyncio
import json


async def fetch(session, url):
    data = await client_input()
    print("Wait for server response...")
    async with session.request(method="POST", url=url, data=json.dumps(data)) as response:
        return await response.text()


async def main():
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
        html = await fetch(session, 'http://127.0.0.1:8080/')
        print(html)


async def client_input():
    result = dict()
    result["name"] = input("Enter name: ")
    result["age"] = (int(input("Enter age: ")))
    result["city"] = (input("Enter city: "))
    return result

loop = asyncio.get_event_loop()
loop.run_until_complete(main())