import threading
import cProfile

i = 0
lock = threading.Lock()

def test():
    global i
    for x in range(100000):
        lock.acquire()
        i += 1
        lock.release()


def main():
    threads = [threading.Thread(target=test) for t in range(10)]
    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print(i)
    assert i == 1000000, i


cProfile.run("main()")

