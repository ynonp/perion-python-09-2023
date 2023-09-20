import asyncio, aiofiles
import cProfile

async def create_file(name):
    async with aiofiles.open(name, mode='w') as f:
        for i in range(1_000):
            await f.write('hello async\n')
        print(f"File {name} is ready")

async def main():
    t1 = asyncio.create_task(create_file('one.txt'))
    t2 = asyncio.create_task(create_file('two.txt'))
    t3 = asyncio.create_task(create_file('three.txt'))

    await t1
    await t2
    await t3

cProfile.run("asyncio.run(main(), debug=True)")
