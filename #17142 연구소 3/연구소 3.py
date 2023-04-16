from collections import deque
from itertools import combinations


N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]


def spread(comb):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    virus_board = [[-1] * N for _ in range(N)]
    q = deque()

    for c in comb:
        q.append(c)
        virus_board[c[0]][c[1]] = 0

    max_time = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if virus_board[nx][ny] == -1 and board[nx][ny] != 1:
                    virus_board[nx][ny] = virus_board[x][y] + 1
                    if board[nx][ny] == 0:
                        max_time = max(max_time, virus_board[nx][ny])
                    q.append((nx, ny))

    not_visited = sum(virus_board, []).count(-1)
    num_wall = sum(board, []).count(1)


    if not_visited == num_wall:
        ans.append(max_time)


virus = []

for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            virus.append((i, j))

ans = []

for comb in combinations(virus, M):
    spread(comb)

if ans:
    print(min(ans))
else:
    print(-1)

