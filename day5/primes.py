import math
import threading
result = [0]
result_lock = threading.Lock()
import cProfile


def is_prime(n: int) -> bool:
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def count_primes(start: int, end: int, result) -> int:
    count = sum(is_prime(n) for n in range(start, end))
    with result_lock:
        result[0] += count
    return count


def count(ranges: list[tuple[int, int]]):
    ts = []
    for start, end in ranges:
        t = threading.Thread(target=count_primes, args=(start, end, result))
        t.start()
        ts.append(t)

    for t in ts: t.join()





cProfile.run("count([(2, 250_000), (250_000, 500_000), (500_000, 750_000), (750_000, 1_000_000)])")
cProfile.run("count([(2, 500_000), (500_000, 1_000_000)])")
cProfile.run("count([(2, 1_000_000)])")
