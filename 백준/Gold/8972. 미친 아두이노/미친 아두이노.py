import sys

input = sys.stdin.readline

r, c = map(int, input().split())
board = [list(input().strip()) for _ in range(r)]
orders = list(map(int, list(input().strip())))

dr = [1, 1, 1, 0, 0, 0, -1, -1, -1]
dc = [-1, 0, 1, -1, 0, 1, -1, 0, 1]


def solve():
    global nowR, nowC, crazy
    cnt = 0

    for order in orders:
        nextR = nowR + dr[order - 1]
        nextC = nowC + dc[order - 1]
        cnt += 1

        if board[nowR][nowC] == 'R':
            print(f'kraj {cnt}')
            exit()

        if order != 5:
            board[nextR][nextC] = 'I'
            board[nowR][nowC] = '.'
        nowR, nowC = nextR, nextC

        nCrazy = set()
        boom = set()
        for crazyR, crazyC in crazy:
            min_dir = -1
            min_dist = float('inf')

            for i in range(9):
                tmpR = crazyR + dr[i]
                tmpC = crazyC + dc[i]

                dist = abs(nowR - tmpR) + abs(nowC - tmpC)
                if min_dist > dist:
                    min_dist = dist
                    min_dir = i

            nCrazyR = crazyR + dr[min_dir]
            nCrazyC = crazyC + dc[min_dir]

            if (nCrazyR, nCrazyC) == (nowR, nowC):
                print(f'kraj {cnt}')
                exit()

            board[crazyR][crazyC] = '.'

            if (nCrazyR, nCrazyC) in nCrazy:
                nCrazy.remove((nCrazyR, nCrazyC))
                boom.add((nCrazyR, nCrazyC))
            else:
                if (nCrazyR, nCrazyC) not in boom:
                    nCrazy.add((nCrazyR, nCrazyC))

        for nr, nc in nCrazy:
            board[nr][nc] = 'R'

        for br, bc in boom:
            board[br][bc] = '.'


        crazy = nCrazy

    for i in range(r):
        for j in range(c):
            print(board[i][j], end='')
        print()
    print()

if __name__ == '__main__':
    nowR, nowC = None, None
    crazy = set()

    for i in range(r):
        for j in range(c):
            if board[i][j] == 'I':
                nowR = i
                nowC = j
            elif board[i][j] == 'R':
                crazy.add((i, j))

    solve()
