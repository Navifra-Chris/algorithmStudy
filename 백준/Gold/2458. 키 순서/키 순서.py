import sys

n, m = map(int, input().split())

height = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())

    height[a-1][b-1] = 1

ans = 0

def solve():
    global ans
    for k in range(n):
        for start in range(n):
            for end in range(n):
                if height[start][k] == 1 and height[k][end]:
                    height[start][end] = 1

    for i in range(n):
        know_h = 0
        for j in range(n):
            know_h += height[i][j] + height[j][i]

        if know_h == n - 1:
            ans += 1

    print(ans)

if __name__ == '__main__':
    solve()