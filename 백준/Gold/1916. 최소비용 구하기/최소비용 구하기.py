import sys
from collections import deque
import heapq

input = sys.stdin.readline

n = int(input())
m = int(input())

bus_info = [[] for _ in range(n+1)]

for i in range(m):
    from_city, to_city, cost = map(int, input().split())

    bus_info[from_city].append((cost, to_city))

start, end = map(int, input().split())

distance = [float('inf') for _ in range(n+1)]

def solve():
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        now_cost, now_city = heapq.heappop(q)

        if distance[now_city] < now_cost:
            continue

        for next_cost, next_city in bus_info[now_city]:
            if now_cost + next_cost < distance[next_city]:
                distance[next_city] = now_cost + next_cost
                heapq.heappush(q, (now_cost + next_cost, next_city))

    print(distance[end])

if __name__ == '__main__':
    solve()
