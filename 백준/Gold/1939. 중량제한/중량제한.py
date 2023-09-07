import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
weight = [[] for _ in range(n+1)]
ans = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    weight[a].append((b, c))
    weight[b].append((a, c))

start, target = map(int, input().split())

def bfs(w):
    q = deque()
    q.append(start)
    visited = [0 for _ in range(n+1)]
    visited[start] = 1

    while q:
        now = q.popleft()

        if now == target:
            return True

        for next, cost in weight[now]:
            if visited[next]:
                continue

            if w > cost:
                continue

            q.append(next)
            visited[next] = 1

    return False


def solve():
    global ans
    min_w, max_w = 0, 1000000000

    while min_w <= max_w:
        mid = (min_w + max_w) // 2
        # print(f"cost: {mid}")
        if bfs(mid):
            min_w = mid+1
            ans = mid
        else:
            max_w = mid-1

    print(ans)


if __name__ == '__main__':
    solve()
