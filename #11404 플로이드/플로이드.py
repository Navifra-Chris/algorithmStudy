import sys
input = sys.stdin.readline
inf = float('inf')

if __name__ == '__main__':
    n = int(input())
    m = int(input())
    gp = [[inf for _ in range(n)] for _ in range(n)]

    for i in range(m):
        start, end, cost = map(int, input().split())
        if gp[start-1][end-1] > cost:
            gp[start-1][end-1] = cost

    for k in range(n):
        for r in range(n):
            for c in range(n):
                if r == c:
                    continue
                if gp[r][c] > gp[r][k] + gp[k][c]:
                    gp[r][c] = gp[r][k] + gp[k][c]
                    # if r == 0 and c == 0:
                    #     print(k, gp[r][c], gp[r][k], gp[k][c])

    for r in range(n):
        for c in range(n):
            if gp[r][c] == inf:
                print(0, end=' ')
            else:
                print(gp[r][c], end=' ')

        print()




