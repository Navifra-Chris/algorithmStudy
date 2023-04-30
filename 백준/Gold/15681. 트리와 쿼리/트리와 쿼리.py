import sys
sys.setrecursionlimit(1000000000) #반복제한 늘리기

input = sys.stdin.readline

n, r, q = map(int, input().split())
graph = [[] for i in range(n+1)]
ans = 1
count = [0] * (n+1)

def dfs(start):
    global count
    count[start] = 1
    for value in graph[start]:
        if count[value] > 0:
            continue

        dfs(value)
        count[start] += count[value]

for i in range(n-1):
    p1, p2 = map(int, input().split())
    graph[p1].append(p2)
    graph[p2].append(p1)

dfs(r)
for i in range(q):
    start = int(input())
    # print(count)
    print(count[start])