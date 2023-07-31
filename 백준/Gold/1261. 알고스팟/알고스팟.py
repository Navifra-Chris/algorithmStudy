import sys
from collections import deque

input = sys.stdin.readline

def init():
    global m, n, board, ans
    ans = float('inf')
    m, n = map(int, input().split())
    board = [list(map(int, list(input().strip()))) for _ in range(n)]


def bfs():
    global ans, board
    q = deque()
    q.append([0, 0])
    visited = [[-1 for _ in range(m)] for _ in range(n)]
    visited[0][0] = 0

    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    while q:
        now_r, now_c = q.popleft()

        for i in range(4):
            nr = now_r + dr[i]
            nc = now_c + dc[i]

            if 0 <= nr < n and 0 <= nc < m and visited[nr][nc] < 0:
                if board[nr][nc] == 0:
                    q.appendleft([nr, nc])
                    visited[nr][nc] = visited[now_r][now_c]
                elif board[nr][nc] == 1:
                    q.append([nr, nc])
                    visited[nr][nc] = visited[now_r][now_c] + 1

    ans = visited[n-1][m-1]


if __name__ == '__main__':
    init()
    bfs()
    print(ans)