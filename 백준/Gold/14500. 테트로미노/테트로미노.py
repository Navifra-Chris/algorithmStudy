import sys
import pprint

n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
tet = []
ans = 0

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def dfs(now, cnt):
    global ans

    if cnt == 4:
        # pprint.pprint(visited)
        # print(tet)
        # print()
        sum_num = 0
        for t in tet:
            sum_num += board[t[0]][t[1]]

        ans = max(ans, sum_num)
        return

    for i in range(4):
        nr = now[0] + dr[i]
        nc = now[1] + dc[i]

        if 0 <= nr < n and 0 <= nc < m:
            if visited[nr][nc] == 1:
                continue

            visited[nr][nc] = 1
            tet.append((nr, nc))

            dfs((nr, nc), cnt + 1)

            visited[nr][nc] = 0
            tet.pop()

def check_h(r, c):
    global ans
    h_shapes = [
        [(0, 0), (-1, 0), (1, 0), (0, 1)],
        [(0, 0), (0, -1), (0, 1), (-1, 0)],
        [(0, 0), (0, -1), (0, 1), (1, 0)],
        [(0, 0), (-1, 0), (1, 0), (0, -1)]
    ]

    for shape in h_shapes:
        num_sum = 0
        is_valid = True
        for dr, dc in shape:
            nr = r + dr
            nc = c + dc

            if 0 <= nr < n and 0 <= nc < m:
                num_sum += board[nr][nc]
            else:
                is_valid = False
                break

        if is_valid:
            ans = max(ans, num_sum)
def solve():
    for i in range(n):
        for j in range(m):
            # print(f'start {i, j}')
            visited[i][j] = 1
            tet.append((i, j))
            dfs((i, j), 1)
            check_h(i, j)
            visited[i][j] = 0
            tet.pop()

    print(ans)


if __name__ == '__main__':
    solve()