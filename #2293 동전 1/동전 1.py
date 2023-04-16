N, K = map(int, input().split())

coin = []
dp = [0] * (K+1)


for i in range(N):
    coin.append(int(input()))

dp[0] = 1
for c in coin:
    for i in range(1, K+1):
        if i-c >= 0:
            dp[i] += dp[i - c]

print(dp[K])
