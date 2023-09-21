import math
import sys

from math import gcd

m = int(input())
nums = []
for _ in range(m):
    num = int(input())
    nums.append(num)
nums.sort()
interval = []
ans = []

def solve():
    global ans
    for i in range(1, m):
        interval.append(nums[i] - nums[i-1])

    n_gcd = interval[0]

    for i in range(1, len(interval)):
        n_gcd = gcd(n_gcd, interval[i])

    for i in range(2, int(math.sqrt(n_gcd))+1):
        if n_gcd % i == 0:
            ans.append(i)
            ans.append(n_gcd // i)

    ans.append(n_gcd)
    ans = list(set(ans))
    ans.sort()

    print(*ans)



if __name__ == '__main__':
    solve()
