import sys
import heapq

INF = float('inf')


def Dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)

        if dist > distance[now]:
            continue

        for next in graph[now]:
            idx = next[0]
            cost = next[1]

            new_dist = distance[now] + cost
            if new_dist < distance[idx]:
                distance[idx] = new_dist
                heapq.heappush(q, (new_dist, idx))


if __name__ == '__main__':
    input = sys.stdin.readline
    V, E = map(int, input().split())
    start = int(input())

    graph = [[] for _ in range(V + 1)]
    distance = [INF for _ in range(V + 1)]


    distance[start] = 0


    for _ in range(E):
        fromN, toN, weight = map(int, input().split())
        graph[fromN].append([toN, weight])

    Dijkstra(start)

    for c in distance[1:]:
        if c == INF:
            print("INF")
        else:
            print(c)
