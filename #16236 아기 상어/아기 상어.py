import heapq
from collections import deque


def bfs(_start):
    heap = []
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    visited = set()
    q = deque()
    cnt = 0
    r, c = _start
    q.append((r, c, cnt))
    board[r][c] = 0

    while q:
        r, c, cnt = q.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < N and 0 <= nc < N and (nr, nc) not in visited:
                visited.add((nr, nc))
                if board[nr][nc] in (0, cur_size):
                    q.append((nr, nc, cnt+1))

                elif board[nr][nc] < cur_size:
                    heapq.heappush(heap, (cnt + 1, nr, nc))

    if heap:
        return heap[0]
    else:
        return None


if __name__ == '__main__':
    N = int(input())
    board = [[int(x) for x in input().split()] for _ in range(N)]
    start = (0, 0)
    cur_size = 2
    total_time = 0
    eat = 0

    for r in range(N):
        for c in range(N):
            if board[r][c] == 9:
                start = (r, c)


    while True:
        fish = bfs(start)

        if fish is None:
            break

        time, r, c = fish
        total_time += time
        eat += 1

        if eat == cur_size:
            cur_size += 1
            eat = 0

        start = (r, c)

    print(total_time)
