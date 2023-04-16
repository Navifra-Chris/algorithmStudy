from collections import deque

N, M = map(int, input().split())

board = [list(input().strip()) for _ in range(N)]
check = [[[[False]*M for _ in range(N)] for _ in range(M)] for _ in range(N)]

q = deque()
dx, dy = (1, 0, -1, 0), (0, 1, 0, -1)
rx, ry, bx,by = [0]*4

def init():
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'R':
                rx, ry = i, j
            elif board[i][j] == 'B':
                bx, by = i, j
    q.append((rx, ry, bx, by, 0))
    check[rx][ry][bx][by] = True

def move(x, y, dx, dy, c):
    while board[x + dx][y + dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        c += 1
    return x, y, c

def bfs():
    while q:
        rx, ry, bx, by, d = q.popleft()
        if d >= 10:
            break
        for i in range(4):
            nrx, nry, cr = move(rx, ry, dx[i], dy[i], 0)
            nbx, nby, cb = move(bx, by, dx[i], dy[i], 0)
            
            if board[nbx][nby] == 'O':
                continue
            if board[nrx][nry] == 'O':
                print(d+1)
                return

            if nrx == nbx and nry == nby:
                if cr > cb:
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]
            
            if not check[nrx][nry][nbx][nby]:
                check[nrx][nry][nbx][nby] = True
                q.append((nrx, nry, nbx, nby, d+1))
    print(-1)
init()
bfs()


