import sys


input = sys.stdin.readline

dr = [-1, 0 ,1 ,0]
dc = [0, 1, 0, -1]


def out_of_board(row, col):
    if 0 <= row < n and 0 <= col < m:
        return False
    return True


def dfs(row, col, cnt):
    global ans
    ans = max(cnt, ans)
    for i in range(4):
        nr = row + dr[i]
        nc = col + dc[i]

        if out_of_board(nr, nc) is True or check[ord(board[nr][nc]) - ord('A')] == 1:
            continue

        check[ord(board[nr][nc]) - ord('A')] = 1
        dfs(nr, nc, cnt+1)
        check[ord(board[nr][nc]) - ord('A')] = 0




if __name__ == '__main__':
    n, m = map(int, input().split())

    board = [list(input().strip()) for _ in range(n)]
    visited = [[0 for _ in range(m)] for _ in range(n)]
    check = [0] * 30

    visited[0][0] = 1
    check[ord(board[0][0]) - ord('A')] = 1

    ans = 0

    dfs(0, 0, 1)

    print(ans)