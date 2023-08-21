import sys
import pprint

input = sys.stdin.readline


def check():
    for start in range(1, n+1):
        now_col = start

        for row in range(1, h + 1):
            if info[row][now_col] == 1:
                now_col += 1
            elif info[row][now_col-1] == 1:
                now_col -= 1

        if now_col != start:
            return False

    return True


def solve(cnt, idx):
    global ans

    if check():
        ans = min(ans, cnt)
        # print(info)
        return

    if cnt >= 3:
        return

    for i in range(idx+1, len(bridges)):
        r, c = bridges[i]
        if info[r][c-1] == 0 and info[r][c+1] == 0:
            info[r][c] = 1
            solve(cnt+1, i)
            info[r][c] = 0


if __name__ == '__main__':
    n, m, h = map(int, input().split())

    info = [[0 for _ in range(n + 1)] for _ in range(h + 1)]

    for i in range(m):
        a, b = map(int, input().split())

        info[a][b] = 1

    bridges = []
    for r in range(1, h + 1):
        for c in range(1, n):
            if info[r][c - 1] == 0 and info[r][c] == 0 and info[r][c + 1] == 0:
                bridges.append([r, c])

    # pprint.pprint(info)

    ans = float('inf')
    solve(0, -1)

    if ans == float('inf') or ans > 3:
        print(-1)
    else:
        print(ans)
