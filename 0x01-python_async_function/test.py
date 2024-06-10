import asyncio
from aiohttp import ClientSession
import requests


base_url = 'http://httpbin.org'


async def count(delay):
    for i in range(delay):
        print(i)
        await asyncio.sleep(1)


async def get_delay(secs):
    endP = f'/delay/{secs}'

    print(f'Getting with {secs} delay....')

    async with ClientSession() as ses:
        async with ses.get(base_url + endP) as res:
            res = await res.read()
            print(res)

    resp = requests.get(base_url + endP).json()
    print(resp)


async def main():
    d = 8
    await asyncio.gather(get_delay(d), count(d))

asyncio.run(main())

print('all done')
