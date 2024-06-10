import asyncio
from aiohttp import ClientSession

base_url = 'http://httpbin.org'


async def count(delay):
    for i in range(delay):
        print(i)
        await asyncio.sleep(1)


async def get_delay(secs):
    endP = f'/delay/{secs}'
    print(f'Getting with {secs} delay....')

    async with ClientSession() as ses:
        try:
            async with ses.get(base_url + endP) as res:
                res = await res.read()
                print(res)
        except Exception as e:
            print(f"An error occurred: {e}")


async def main():
    d = 4
    await asyncio.gather(get_delay(d), count(d))

asyncio.run(main())
print('all done')
