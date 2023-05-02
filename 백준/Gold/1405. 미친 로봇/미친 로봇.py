import sys

input = sys.stdin.readline

n, p1, p2, p3, p4 = map(int, input().split())

probs = [p1 / 100, p2 / 100, p3 / 100, p4 / 100]
length = n * 2 + 1
visited = [[False for _ in range(length)] for _ in range(length)]

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

start = (n, n)
ans = 0

def dfs(depth, prob, pos):
    global ans
    # print(depth, prob, pos)
    if depth == n:
        # print(depth, prob, pos)
        ans += prob
        return

    for i in range(4):
        nr = pos[0] + dr[i]
        nc = pos[1] + dc[i]
        if 0 <= nr < length and 0 <= nc < length:
            if visited[nr][nc] is True:
                continue
            if depth == 0:
                np = probs[i]
            else:
                np = prob * probs[i]

            visited[nr][nc] = True
            dfs(depth+1, np, (nr, nc))
            visited[nr][nc] = False

visited[n][n] = True
dfs(0, 0, start)
print(ans)