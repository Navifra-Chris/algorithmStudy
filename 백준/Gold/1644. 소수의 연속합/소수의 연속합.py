import sys
from itertools import combinations
import math


input = sys.stdin.readline

n = int(input())

is_prime = [True for _ in range(n+1)]
ans = 0


def make_is_prime():
    for i in range(2, int(math.sqrt(n))+1):
        if is_prime[i] is True:
            j = 2
            while i * j <= n:
                is_prime[i*j] = False
                j += 1


def solve():
    global ans
    make_is_prime()
    primes = [i for i in range(2, n+1) if is_prime[i] is True]

    start, end = 0, 0

    while end <= len(primes):
        if sum(primes[start:end]) < n:
            end += 1
        elif sum(primes[start:end]) > n:
            start += 1
        else:
            # print(primes[start:end])
            ans += 1
            end += 1

    print(ans)


if __name__ == '__main__':
    solve()