import sys
input = sys.stdin.readline
n = int(input())

dp = [0 for _ in range(n+1)]

day = []
pay = []

for i in range(n):
    t, p = map(int, input().split())
    day.append(t)
    pay.append(p)

for i in range(0, n):
    if i + day[i] <= n:
        dp[i+day[i]] = max(dp[i+day[i]], dp[i] + pay[i])
    if i+1 <= n:
        dp[i + 1] = max(dp[i], dp[i + 1])

print(max(dp))
