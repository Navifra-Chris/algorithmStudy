from collections import deque


def bfs(start, rain):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    q = deque()
    q.append(start)

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] == 0 and board[nx][ny] > rain:
                    q.append((nx, ny))
                    visited[nx][ny] = True


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
max_h = max(map(max, board))
min_h = min(map(min, board))
max_area = 0

for rain in range(max_h):
    visited = [[False]*N for _ in range(N)]
    area = 0
    for r in range(N):
        for c in range(N):
            if board[r][c] > rain and visited[r][c] is False:
                bfs((r, c), rain)
                visited[r][c] = True
                area += 1

    max_area = max(max_area, area)

print(max_area)

