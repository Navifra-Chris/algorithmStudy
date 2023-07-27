import sys

input = sys.stdin.readline

def cal_chicken_dist():
    chicken_dist = 0

    for i in range(len(home)):
        min_dist = float('inf')
        for j in range(len(store)):
            if used[j] is False:
                continue
            dist = dist_info[j][i]
            min_dist = min(dist, min_dist)


        chicken_dist += min_dist

    return chicken_dist


def dfs(cnt, now):
    global ans

    if cnt == m:
        result = cal_chicken_dist()

        ans = min(ans, result)

    for i in range(now, len(store)):
        if used[i] is False:
            used[i] = True
            dfs(cnt+1, i+1)
            used[i] = False


if __name__ == '__main__':
    n, m = map(int, input().split())

    board = [list(map(int, input().split())) for _ in range(n)]
    home = []
    store = []

    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                home.append((i, j))
            elif board[i][j] == 2:
                store.append((i, j))

    dist_info = [[0 for _ in range(len(home))] for _ in range(len(store))]
    used = [False] * len(store)

    ans = float('inf')

    for i in range(len(store)):
        for j in range(len(home)):
            dist_info[i][j] = abs(store[i][0] - home[j][0]) + abs(store[i][1] - home[j][1])

    dfs(0, 0)

    print(ans)





