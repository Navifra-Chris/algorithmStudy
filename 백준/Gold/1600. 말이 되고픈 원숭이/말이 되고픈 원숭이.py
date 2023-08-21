import sys
from collections import deque
input = sys.stdin.readline

k = int(input())
w, h = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(h)]

def solve():
    q = deque()
    q.append((0, 0, 0))

    visited = [[[-1 for _ in range(w)] for _ in range(h)] for _ in range(k+1)]

    visited[0][0][0] = 0

    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    dr2 = [-2, -1, 1, 2, 2, 1, -1, -2]
    dc2 = [1, 2, 2, 1, -1, -2, -2, -1]

    while q:
        now_r, now_c, now_k = q.popleft()
        now_dist = visited[now_k][now_r][now_c]

        if now_r == h-1 and now_c == w-1:
            print(visited[now_k][now_r][now_c])
            exit()

        for i in range(4):
            nr = now_r + dr[i]
            nc = now_c + dc[i]

            if 0 <= nr < h and 0 <= nc < w:
                if visited[now_k][nr][nc] >= 0:
                    continue

                if board[nr][nc] == 1:
                    continue

                visited[now_k][nr][nc] = now_dist + 1
                q.append((nr, nc, now_k))

        if now_k < k:
            for i in range(8):
                nr = now_r + dr2[i]
                nc = now_c + dc2[i]

                if 0 <= nr < h and 0 <= nc < w:
                    if visited[now_k+1][nr][nc] >= 0:
                        continue

                    if board[nr][nc] == 1:
                        continue

                    visited[now_k+1][nr][nc] = now_dist + 1
                    q.append((nr, nc, now_k+1))

    print(-1)


if __name__ == '__main__':
    solve()