N = int(input())

matrix = [[0 for _ in range(101)] for _ in range(101)]
ans = 0

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

for i in range(N):
    y, x, d, g = map(int, input().split())

    curve = [d]
    matrix[x][y] = 1
    add_c = [d]

    for j in range(g+1):
        for c in add_c:
            x = x+dx[c]
            y = y+dy[c]
            matrix[x][y] = 1

        add_c.clear()

        for c in curve:
            add_c.append((c+1) % 4)

        add_c.reverse()
        curve += add_c


for i in range(100):
    for j in range(100):
        if matrix[i][j] == 1 and matrix[i][j+1] == 1 and matrix[i+1][j] == 1 and matrix[i+1][j+1] == 1:
            ans += 1

print(ans)