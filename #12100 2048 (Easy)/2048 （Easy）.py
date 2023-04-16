import sys
import copy

N = int(input())
board = [[int(x) for x in sys.stdin.readline().split()] for _ in range(N)]
ans = 0

def move(dir):
    if dir == 0: # up
        for j in range(N):
            target = 0
            for i in range(1, N):
                if board[i][j]:
                    num = board[i][j]
                    board[i][j] = 0
                    if board[target][j] == 0:
                        board[target][j] = num
                    elif board[target][j] == num:
                        board[target][j] *= 2
                        target += 1
                    else:
                        target += 1
                        board[target][j] = num

    elif dir == 1: # down
        for j in range(N):
            target = N - 1
            for i in range(N-2, -1, -1):
                if board[i][j]:
                    num = board[i][j]
                    board[i][j] = 0
                    if board[target][j] == 0:
                        board[target][j] = num
                    elif board[target][j] == num:
                        board[target][j] *= 2
                        target -= 1
                    else:
                        target -= 1
                        board[target][j] = num

    elif dir == 2: # left
        for i in range(N):
            target = 0
            for j in range(1, N):
                if board[i][j]:
                    num = board[i][j]
                    board[i][j] = 0
                    if board[i][target] == 0:
                        board[i][target] = num
                    elif board[i][target] == num:
                        board[i][target] *= 2
                        target += 1
                    else:
                        target += 1
                        board[i][target] = num



    elif dir == 3: # right
        for i in range(N):
            target = N - 1
            for j in range(N - 2, -1, -1):
                if board[i][j]:
                    num = board[i][j]
                    board[i][j] = 0
                    if board[i][target] == 0:
                        board[i][target] = num
                    elif board[i][target] == num:
                        board[i][target] *= 2
                        target -= 1
                    else:
                        target -= 1
                        board[i][target] = num


def dfs(cnt):
    global board
    global ans

    if cnt == 5:
        ans = max(ans, max(map(max, board)))
        return

    temp_board = copy.deepcopy(board)
    for i in range(4):
        move(i)
        dfs(cnt + 1)
        board = copy.deepcopy(temp_board)




if __name__ == '__main__':
    dfs(0)
    print(ans)
