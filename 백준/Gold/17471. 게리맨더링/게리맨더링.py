import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline
n = int(input())
p_info = list(map(int, input().split()))

area = [[] for _ in range(n+1)]
ans = float('inf')

for i in range(n):
    info = list(map(int, input().split()))
    area[i+1] = info[1:]

def bfs(group):
    q = deque()
    start = group[0]
    visited = [start]
    q.append(start)
    sum_p = 0

    while q:
        now = q.popleft()
        sum_p += p_info[now - 1]

        for i in area[now]:
            if i in visited:
                continue

            if i not in group:
                continue

            visited.append(i)
            q.append(i)

    return sum_p, len(visited)

def solve():
    global ans
    for i in range(1, n//2+1):
        combs = list(combinations(range(1, n+1), i))

        for comb in combs:
            sum1, p1 = bfs(comb)
            sum2, p2 = bfs([i for i in range(1, n+1) if i not in comb])
            if p1+p2 == n:
                ans = min(ans, abs(sum1 - sum2))
    
    if ans == float('inf'):
        print(-1)
    else:
        print(ans)

if __name__ == '__main__':
    solve()