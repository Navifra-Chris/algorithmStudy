from collections import deque

w, h = map(int, input().split())
board = [list(input().strip()) for _ in range(h)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def bfs(start, end):
    q = deque()
    visited = [[[float('inf')] * 4 for _ in range(w)] for _ in range(h)]

    for i in range(4):
        q.append((start[0], start[1], i, 0))
        visited[start[0]][start[1]][i] = 0

    while q:
        r, c, dir, cnt = q.popleft()

        while True:
            r, c = r + dr[dir], c + dc[dir]

            if r < 0 or r >= h or c < 0 or c >= w or board[r][c] == '*':
                break

            if visited[r][c][dir] <= cnt:
                continue

            visited[r][c][dir] = cnt

            if (r, c) == end:
                return cnt

            for nd in range(4):
                if nd != dir and visited[r][c][nd] > cnt + 1:
                    q.append((r, c, nd, cnt + 1))


start, end = None, None
for i in range(h):
    for j in range(w):
        if board[i][j] == 'C':
            if start is None:
                start = (i, j)
            else:
                end = (i, j)

print(bfs(start, end))
