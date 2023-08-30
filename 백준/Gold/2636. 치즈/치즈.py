import sys
import copy
from collections import deque
import pprint

input = sys.stdin.readline

n, m = map(int, input().split())

cheese = [list(map(int, input().split())) for _ in range(n)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def bfs(r, c):
    q = deque()
    q.append((r, c))
    visited = [[0 for _ in range(m)] for _ in range(n)]
    future_cheese = copy.deepcopy(cheese)
    num_delete_cheese = 0
    num_empty_area = 0

    while q:
        now_r, now_c = q.popleft()

        for i in range(4):
            nr = now_r + dr[i]
            nc = now_c + dc[i]

            if 0 <= nr < n and 0 <= nc < m:
                if visited[nr][nc] == 1:
                    continue

                if cheese[nr][nc] == 1:
                    num_delete_cheese += 1
                    future_cheese[nr][nc] = 0
                else:
                    num_empty_area += 1
                    q.append((nr, nc))

                visited[nr][nc] = 1

    return future_cheese, num_empty_area, num_delete_cheese

def solve():
    global cheese
    past_num_delete_cheese = 0
    time = 0
    while True:
        future_cheese, num_empty_area, num_delete_cheese = bfs(0, 0)

        # print(num_empty_area)
        # pprint.pprint(cheese)

        if num_empty_area == n * m:
            print(time, past_num_delete_cheese)
            exit()

        cheese = future_cheese
        time += 1
        past_num_delete_cheese = num_delete_cheese

if __name__ == '__main__':
    solve()