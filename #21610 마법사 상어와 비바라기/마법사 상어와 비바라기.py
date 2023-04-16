import copy


N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
move = [list(map(int, input().split())) for _ in range(M)]

cloud = [(N - 1, 0), (N - 1, 1), (N - 2, 0), (N - 2, 1)]

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

for i in range(M):
    d = move[i][0] - 1
    s = move[i][1]
    tmp_cloud = []
    for j in range(len(cloud)):
        x = cloud[j][0]
        y = cloud[j][1]
        nx = (x + (dx[d] * s)) % N
        ny = (y + (dy[d] * s)) % N
        tmp_cloud.append((nx, ny))
        board[nx][ny] += 1

    for c in tmp_cloud:
        x = c[0]
        y = c[1]
        for k in range(1, 8, 2):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < N and 0 <= ny < N:
                if board[nx][ny] != 0:
                    board[x][y] += 1


    cloud.clear()
    for r in range(N):
        for c in range(N):
            if (r, c) not in tmp_cloud:
                if board[r][c] >= 2:
                    cloud.append((r, c))
                    board[r][c] -= 2


print(sum(sum(board, [])))



