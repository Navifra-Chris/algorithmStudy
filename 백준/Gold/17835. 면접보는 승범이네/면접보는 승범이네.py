import sys
import heapq


input = sys.stdin.readline

n, m, k = map(int, input().split())

city = [[] for _ in range(n+1)]
distance = [float('inf') for _ in range(n+1)]


for i in range(m):
    start, end, dist = map(int, input().split())

    city[end].append((dist, start))

targets = list(map(int, input().split()))

def solve():
    pq = []
    for target in targets:
        heapq.heappush(pq, (0, target))
        distance[target] = 0

    while pq:
        dist, now = heapq.heappop(pq)

        if distance[now] < dist:
            continue

        for nDist, next in city[now]:
            if dist + nDist < distance[next]:
                distance[next] = dist + nDist
                heapq.heappush(pq, (dist+nDist, next))
    # print(distance)
    print(distance.index(max([x for x in distance if x != float('inf')])))
    print(max([x for x in distance if x != float('inf')]))



if __name__ == '__main__':
    solve()