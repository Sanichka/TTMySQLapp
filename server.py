import asyncio
from aiohttp import web
import pymysql
from pymysql.cursors import DictCursor
from contextlib import closing


async def handler(request):
    text = await request.json()
    database = db_connect()
    db_write(database, text)
    await asyncio.sleep(10)
    return web.Response(text="Data successfully sent and processed...")


async def main():
    server = web.Server(handler)
    runner = web.ServerRunner(server)
    await runner.setup()
    site = web.TCPSite(runner, "localhost", 8080)
    await site.start()
    print("======= Serving on http://127.0.0.1:8080/ ======")
    await asyncio.sleep(100*3600)


def db_connect():
    db = pymysql.connect(
        host="localhost",
        user="root",
        password="passfortest",
        db="testdb",
        cursorclass=DictCursor
    )
    return db


def db_write(db, data):
    with closing(db) as conn:
        with conn.cursor() as cursor:
            list_data = list(data.values())
            placeholders = ', '.join(['%s'] * len(data))
            columns = ', '.join(data.keys())
            query = "INSERT INTO %s ( %s ) VALUES ( %s );" % ('testdb', columns, placeholders)
            cursor.execute(query, list_data)
            conn.commit()
            with conn.cursor() as cursor:
                query = "SELECT name, age, city FROM TestDB"
                cursor.execute(query)
                for row in cursor:
                    print(row["name"], row["age"], row["city"])


loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(main())
except KeyboardInterrupt:
    pass
loop.close()