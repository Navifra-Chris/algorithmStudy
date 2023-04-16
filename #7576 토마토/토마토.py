import sys
from collections import deque

input = sys.stdin.readline

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def out_of_map(r, c):
    if 0 <= r < n and 0 <= c < m:
        return False
    return True


def bfs():
    global tomatoes
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if out_of_map(nr, nc) or box[nr][nc] == '-1' or box[nr][nc] == '1' or visited[nr][nc] == 1:
                continue

            box[nr][nc] = '1'
            visited[nr][nc] = visited[r][c] + 1
            q.append((nr, nc))
            tomatoes -= 1
            if tomatoes == 0:
                return visited[nr][nc]

    return -1


if __name__ == '__main__':
    m, n = map(int, input().split())
    q = deque()

    box = [list(input().split()) for _ in range(n)]
    visited = [[0 for _ in range(m)] for _ in range(n)]
    tomatoes = 0

    for i in range(n):
        for j in range(m):
            if box[i][j] == '0':
                tomatoes += 1
            elif box[i][j] == '1':
                q.append((i, j))

    if tomatoes == 0:
        print(0)
    else:
        result = bfs()
    
        print(result)
