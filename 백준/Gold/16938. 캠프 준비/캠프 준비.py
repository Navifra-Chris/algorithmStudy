import sys
from itertools import combinations

input = sys.stdin.readline

n, l, r, x = map(int, input().split())

rank = list(map(int, input().split()))

ans = 0

def solve():
    global ans
    for i in range(2, n+1):
        for comb in combinations(rank, i):
            sum_rank = sum(comb)
            max_rank = max(comb)
            min_rank = min(comb)

            if l <= sum_rank <= r and x <= (max_rank - min_rank):
                ans += 1

    print(ans)



if __name__ == '__main__':
    solve()