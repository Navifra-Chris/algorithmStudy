import copy


def spread_virus(r, c, board):
    global N
    global M

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    for i in range(4):
        n_r = r + dr[i]
        n_c = c + dc[i]
        if (0 <= n_r < N) and (0 <= n_c < M):
            if board[n_r][n_c] == 0:
                board[n_r][n_c] = 2
                spread_virus(n_r, n_c, board)


def select_wall(start, cnt):
    global board
    global N
    global M
    global answer
    global virus_pos

    if cnt == 3:
        temp_board = copy.deepcopy(board)
        for virus in virus_pos:
            r = virus[0]
            c = virus[1]
            spread_virus(r, c, temp_board)
        answer = max(answer, sum(i.count(0) for i in temp_board))
        return

    else:
        for i in range(start, N*M):
            r = i // M
            c = i % M
            if board[r][c] == 0:
                board[r][c] = 1
                select_wall(i, cnt+1)
                board[r][c] = 0


def count_virus(N, M):
    global virus_pos

    for i in range(0, N*M):

        r = i // M
        c = i % M
        if board[r][c] == 2:
            virus_pos.append((r, c))


if __name__ == '__main__':
    N, M = map(int, input().split())
    board = [[int(x) for x in input().split()] for _ in range(N)]
    answer = 0
    virus_pos = []

    count_virus(N, M)
    select_wall(0, 0)

    print(answer)
