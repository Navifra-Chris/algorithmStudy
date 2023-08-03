import sys
import heapq

input = sys.stdin.readline

def init():
    global n, m, x, roads

    n, m, x = map(int, input().split())
    roads = [[] for _ in range(n+1)]
    for i in range(m):
        start, end, cost = map(int, input().split())

        roads[start].append([end, cost])


def cal_dist(start, target):
    # print(f"==={start}번 노드 시작")
    global roads

    distance = [float('inf') for _ in range(n+1)]
    q = []
    heapq.heappush(q, [0, start])
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for next, d in roads[now]:
            if distance[next] > dist + d:
                distance[next] = dist + d
                heapq.heappush(q, [dist+d, next])

    # print(f'{start} -> {target} {distance}')
    return distance[target]





def solve():
    result = [0 for _ in range(n+1)]
    for start in range(1, n+1):
        # print(start)
        if start == x:
            continue

        dist_go = cal_dist(start, x)
        dist_back = cal_dist(x, start)

        result[start] = dist_go + dist_back


    # print(result)
    print(max(result))

if __name__ == '__main__':
    init()
    solve()