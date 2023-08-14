import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]
visited = [[-1 for _ in range(m)] for _ in range(n)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

ans = 0

def dfs(now_r, now_c):
    global ans

    if now_r == n-1 and now_c == m-1:
        return 1

    if visited[now_r][now_c] != -1:  
        return visited[now_r][now_c]

    visited[now_r][now_c] = 0

    for i in range(4):
        nr = now_r + dr[i]
        nc = now_c + dc[i]

        if 0 <= nr < n and 0 <= nc < m:
            if board[nr][nc] >= board[now_r][now_c]:
                continue

            visited[now_r][now_c] += dfs(nr, nc)

    return visited[now_r][now_c]


if __name__ == '__main__':
    dfs(0, 0)
    print(visited[0][0])