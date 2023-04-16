import sys
from collections import deque

def move(dir):
    if dir == 1:
        dice[0], dice[3], dice[5], dice[2] = dice[2], dice[0], dice[3], dice[5]
    elif dir == 2:
        dice[0], dice[3], dice[5], dice[2] = dice[3], dice[5], dice[2], dice[0]
    elif dir == 3:
        dice[0], dice[1], dice[5], dice[4] = dice[1], dice[5], dice[4], dice[0]
    else:
        dice[0], dice[1], dice[5], dice[4] = dice[4], dice[0], dice[1], dice[5]


def start():
    global y
    global x
    for i in order:
        ny = y + dy[i-1]
        nx = x + dx[i-1]
        if not 0 <= nx < N or not 0 <= ny < M:
            continue
        x, y = nx, ny
        move(i)
        if board[x][y] == 0:
            board[x][y] = dice[0]
        else:
            dice[0] = board[x][y]
            board[x][y] = 0

        print(dice[5])


if __name__ == '__main__':
    # input = sys.stdin.readline
    N, M, x, y, K = map(int, input().split())
    board = [[int(x) for x in input().split()] for _ in range(N)]
    order = [int(x) for x in input().split()]
    dice = [0, 0, 0, 0, 0, 0]

    dy = [1, -1, 0, 0]
    dx = [0, 0, -1, 1]

    start()