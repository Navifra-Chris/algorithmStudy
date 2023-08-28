import sys
from collections import deque
import heapq

input = sys.stdin.readline
ans = 0


def solve(times, indegree, prev, dp_time, w):
    global ans
    q = []
    for i, degree in enumerate(indegree):
        if degree == 0:
            heapq.heappush(q, (times[i], i))
            dp_time[i] += times[i]

    while q:
        now_cost, now = heapq.heappop(q)
        for next in prev[now]:
            indegree[next] -= 1
            dp_time[next] = max(dp_time[next], dp_time[now] + times[next])
            if indegree[next] == 0:
                heapq.heappush(q, (times[next], next))



    print(dp_time[w])




if __name__ == '__main__':
    t = int(input())
    for test_case in range(t):
        n, k = map(int, input().split())
        times = [0] + list(map(int, input().split()))

        prev = [[] for _ in range(n + 1)]
        indegree = [-1] + [0 for _ in range(n)]
        dp_time = [0 for _ in range(n + 1)]
        for i in range(k):
            pre, next = map(int, input().split())
            prev[pre].append(next)
            indegree[next] += 1

        w = int(input())

        # print(prev)

        solve(times, indegree, prev, dp_time, w)
