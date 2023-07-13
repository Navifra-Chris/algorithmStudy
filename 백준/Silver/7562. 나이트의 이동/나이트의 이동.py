import sys
from collections import deque
import pprint

def is_out_of_board(r, c, n):
    if 0 <= r < n and 0 <= c < n:
        return False

    return True

t = int(input())

dr = [-2, -1, 1, 2, 2, 1, -1, -2]
dc = [1, 2, 2, 1, -1, -2, -2, -1]

for test_case in range(t):
    n = int(input())

    start_r,  start_c = map(int, input().split())
    target_r, target_c = map(int, input().split())

    board = [[-1 for _ in range(n)] for _ in range(n)]

    q = deque()

    q.append((start_r, start_c))
    board[start_r][start_c] = 0

    while q:
        now_r, now_c = q.popleft()

        if now_r == target_r and now_c == target_c:
            print(board[now_r][now_c])
            break

        for i in range(8):
            nr = now_r + dr[i]
            nc = now_c + dc[i]

            if is_out_of_board(nr, nc, n):
                continue

            if board[nr][nc] > -1:
                continue

            q.append((nr, nc))
            board[nr][nc] = board[now_r][now_c] + 1











