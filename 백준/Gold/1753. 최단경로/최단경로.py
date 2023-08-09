import sys
import heapq

input = sys.stdin.readline
n, m = map(int, input().split())
start = int(input())
graph = [[] * (n+1) for _ in range(n+1)]
INF = int(1e9)
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            current_cost = distance[now] + i[1]

            if current_cost < distance[i[0]]:
                distance[i[0]] = current_cost
                heapq.heappush(q, (current_cost, i[0]))

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == int(1e9):
        print("INF")
    
    else:
        print(distance[i])