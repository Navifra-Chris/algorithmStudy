import sys
from collections import deque

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

q = deque()


def BFS():
    while q:
        now = q.popleft()
        if MAP[goal_r][goal_c] == 'S':
            return visited[goal_r][goal_c]
        for i in range(4):
            nr = now[0] + dr[i]
            nc = now[1] + dc[i]

            if 0 <= nr < R and 0 <= nc < C:
                if (MAP[nr][nc] == '.' or MAP[nr][nc] == 'D') and MAP[now[0]][now[1]] == 'S':
                    MAP[nr][nc] = 'S'
                    q.append((nr, nc))
                    visited[nr][nc] = visited[now[0]][now[1]] + 1
                elif (MAP[nr][nc] == '.' or MAP[nr][nc] == 'S') and MAP[now[0]][now[1]] == '*':
                    MAP[nr][nc] = '*'
                    q.append((nr, nc))

    return 'KAKTUS'


if __name__ == '__main__':
    R, C = map(int, input().split())

    MAP = [list(input().strip()) for _ in range(R)]
    visited = [[0 for _ in range(C)] for _ in range(R)]

    start_r, start_c = None, None
    goal_r, goal_c = None, None

    for r in range(R):
        for c in range(C):
            if MAP[r][c] == 'S':
                start_r = r
                start_c = c
                q.append((r, c))
            elif MAP[r][c] == 'D':
                goal_r = r
                goal_c = c
    for r in range(R):
        for c in range(C):
            if MAP[r][c] == '*':
                q.append((r, c))

    result = BFS()
    print(result)
