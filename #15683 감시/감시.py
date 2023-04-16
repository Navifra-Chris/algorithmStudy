import copy
import sys

dir = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 3], [0, 1], [1, 2], [2, 3]],
    [[0, 2, 3], [0, 1, 3], [0, 1, 2], [1, 2, 3]],
    [[0, 1, 2, 3]]
]

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def fill(r, c, dirs, board):
    for d in dirs:
        nr = r
        nc = c

        while True:
            nr += dr[d]
            nc += dc[d]

            if 0 <= nr < n and 0 <= nc < m:
                if board[nr][nc] == 6:
                    break

                elif board[nr][nc] == 0:
                    board[nr][nc] = '#'

            else:
                break


def cnt_zero(board):
    res = 0
    for i in range(n):
        res += board[i].count(0)


    return res

def dfs(depth, board):
    global min_cnt
    if depth == len(cctv):
        zero = cnt_zero(board)

        min_cnt = min(zero, min_cnt)
        return

    tmp_board = copy.deepcopy(board)
    r, c, num = cctv[depth]

    for dirs in dir[num]:
        fill(r, c, dirs, tmp_board)
        dfs(depth+1, tmp_board)
        tmp_board = copy.deepcopy(board)





if __name__ == '__main__':
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    cctv = []
    min_cnt = float('inf')

    for i in range(n):
        for j in range(m):
            if board[i][j] in [0, 6]:
                continue
            cctv.append((i, j, board[i][j]))
    dfs(0, board)
    print(min_cnt)