import cProfile


def create_file(name):
    with open(name, mode='w') as f:
        for i in range(1_000):
            f.write('hello async\n')
        print(f"File {name} is ready")


async def main():
    create_file("one.txt")
    create_file("two.txt")
    create_file("three.txt")

cProfile.run("main()")

