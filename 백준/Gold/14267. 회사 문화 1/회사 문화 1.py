import sys

n, m = map(int, input().split())

superior = [0] + list(map(int, input().split()))
ans = [0 for _ in range(n+1)]

for _ in range(m):
    i, w = map(int, input().split())
    ans[i] += w

for i in range(2, n+1):
    ans[i] += ans[superior[i]]

for i in range(1, n+1):
    print(ans[i])


