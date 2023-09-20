from multiprocessing import Pool
from math import sqrt
import cProfile

def isprime(n: int):
    for i in range(2, int(sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

def main():
    p = Pool(5)
    print(sum(p.map(isprime, range(2, 1_000_000))))


if __name__ == "__main__":
    cProfile.run("main()")