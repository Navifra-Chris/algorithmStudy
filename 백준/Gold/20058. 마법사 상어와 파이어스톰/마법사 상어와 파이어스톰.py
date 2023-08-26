import sys
import copy
import pprint
from collections import deque

input = sys.stdin.readline

n, q = map(int, input().split())
board_size = 2 ** n
board = [list(map(int, input().split())) for _ in range(2 ** n)]
rot_board = copy.deepcopy(board)
q_list = list(map(int, input().split()))

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def rotation(start, end):
    global rot_board
    start_r, start_c = start
    end_r, end_c = end
    size = end_r - start_r
    for r in range(size):
        for c in range(size):
            rot_board[start_r + c][start_c + size - 1 - r] = board[start_r + r][start_c + c]

def bfs(r, c, visited):
    global board
    q = deque()
    ice_cnt = board[r][c]
    ice_size = 1

    q.append((r, c))
    visited[r][c] = 1

    while q:
        now_r, now_c = q.popleft()

        for i in range(4):
            nr = now_r + dr[i]
            nc = now_c + dc[i]

            if 0 <= nr < board_size and 0 <= nc < board_size:
                if visited[nr][nc] == 1 or board[nr][nc] == 0:
                    continue

                ice_cnt += board[nr][nc]
                ice_size += 1

                q.append((nr, nc))
                visited[nr][nc] = 1
    return ice_cnt, ice_size
def solve():
    # FireStorm
    for cur_q in q_list:
        cur_q_size = 2 ** cur_q

        for r_start in range(0, board_size, cur_q_size):
            for c_start in range(0, board_size, cur_q_size):
                r_end, c_end = r_start + cur_q_size, c_start + cur_q_size
                rotation((r_start, c_start), (r_end, c_end))

        for r in range(board_size):
            for c in range(board_size):
                cnt_ice = 0
                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]

                    if 0 <= nr < board_size and 0 <= nc < board_size:
                        if rot_board[nr][nc] > 0:
                            cnt_ice += 1

                if cnt_ice < 3 and rot_board[r][c] > 0:
                    board[r][c] = rot_board[r][c] - 1
                else:
                    board[r][c] = rot_board[r][c]

    # 정답 계산
    total_ice = 0
    max_size = 0
    visited = [[0 for _ in range(board_size)] for _ in range(board_size)]
    for r in range(board_size):
        for c in range(board_size):
            if board[r][c] == 0:
                visited[r][c] = 1

            if visited[r][c] == 1:
                continue

            ice_cnt, ice_size = bfs(r, c, visited)
            total_ice += ice_cnt
            max_size = max(max_size, ice_size)

    print(total_ice)
    print(max_size)




if __name__ == '__main__':
    solve()
