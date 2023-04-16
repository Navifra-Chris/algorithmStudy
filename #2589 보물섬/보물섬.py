from itertools import combinations
from collections import deque


def bfs(start):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    q = deque()
    q.append(start)

    d_board = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    visited[start[0]][start[1]] = True

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny] == False and board[nx][ny] == "L":
                    q.append((nx, ny))
                    d_board[nx][ny] += d_board[x][y] + 1
                    visited[nx][ny] = True

    return max(map(max, d_board))


N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

lands = []
max_d = 0

for r in range(N):
    for c in range(M):
        if board[r][c] == "L":
            d = bfs((r, c))
            max_d = max(max_d, d)


print(max_d)



