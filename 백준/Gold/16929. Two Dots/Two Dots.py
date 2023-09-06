import sys

input = sys.stdin.readline

n, m = map(int, input().split())

board = [list(input()) for _ in range(n)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# visited = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(4)]
visited = [[0 for _ in range(m)] for _ in range(n)]

def dfs(r, c, dir):
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < n and 0 <= nc < m:
            if dir != -1 and (dir + 2) % 4 == i:
                continue

            if board[nr][nc] != board[r][c]:
                continue

            if visited[nr][nc] == 1:
                print("Yes")
                exit()

            visited[nr][nc] = 1
            dfs(nr, nc, i)
            visited[nr][nc] = 0




if __name__ == '__main__':
    for i in range(n):
        for j in range(m):
            dfs(i, j, -1)
    print("No")