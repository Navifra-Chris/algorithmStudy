import sys
import pprint

input = sys.stdin.readline

n, m = map(int, input().split())

board = [list(input().strip()) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]

dr = [1, 0, -1, 0]
dc = [0, -1, 0, 1]

dir = {'D': 0, 'L': 1, 'U': 2, 'R': 3}

color = 0

for r in range(n):
    for c in range(m):
        # for i in visited:
        #     print(i)
        # print()
        if visited[r][c] != 0:
            continue

        poses = [(r, c)]

        nr = r + dr[dir[board[r][c]]]
        nc = c + dc[dir[board[r][c]]]

        # color += 1
        # visited[r][c] = color
        is_new = False
        while visited[nr][nc] == 0:
            if (nr, nc) in poses:
                is_new = True
                color += 1
                break
            poses.append((nr, nc))

            ndir = board[nr][nc]

            nr = nr + dr[dir[ndir]]
            nc = nc + dc[dir[ndir]]

        if is_new:
            for pos in poses:
                visited[pos[0]][pos[1]] = color
        else:
            for pos in poses:
                visited[pos[0]][pos[1]] = visited[nr][nc]


# for i in visited:
#     print(i)
print(color)
