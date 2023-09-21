import sys
from collections import deque


n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(m)]
dr = [0, -1, 0, 1]
dc = [-1, 0, 1, 0]

def bfs(r, c):
    q = deque()
    q.append((r,c))
    visited[r][c] = 1
    size = 1

    while q:
        now_r, now_c = q.popleft()

        for i in range(4):
            nr = now_r + dr[i]
            nc = now_c + dc[i]

            if 0 <= nr < m and 0 <= nc < n:
                mask = 1 << i
                if board[now_r][now_c] & mask:
                    continue

                if visited[nr][nc] == 1:
                    continue

                visited[nr][nc] = 1
                q.append((nr, nc))
                size += 1

    return size



if __name__ == '__main__':
    visited = [[0 for _ in range(n)] for _ in range(m)]
    room_cnt = 0
    max_room_size = 0

    for i in range(m):
        for j in range(n):
            if visited[i][j] == 1:
                continue

            room_size = bfs(i, j)
            room_cnt += 1
            max_room_size = max(max_room_size, room_size)

    # visited.clear()
    max_room_size_crush = 0
    for r in range(m):
        for c in range(n):
            for i in range(4):
                visited = [[0 for _ in range(n)] for _ in range(m)]

                mask = 1 << i
                board[r][c] -= mask
                size = bfs(r, c)
                board[r][c] += mask

                max_room_size_crush = max(max_room_size_crush, size)


    print(room_cnt, max_room_size, max_room_size_crush)
