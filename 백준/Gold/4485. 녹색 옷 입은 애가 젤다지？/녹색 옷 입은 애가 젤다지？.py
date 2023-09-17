import sys
import heapq

input = sys.stdin.readline

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

cnt = 1
def solve():
    pq = []
    distance = [[float('inf') for _ in range(n)] for _ in range(n)]

    heapq.heappush(pq, (board[0][0], 0, 0))
    distance[0][0] = 0

    while pq:
        cost, r, c = heapq.heappop(pq)

        if r == n-1 and c == n-1:
            print(f'Problem {cnt}: {distance[r][c]}')
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < n and 0 <= nc < n:
                new_cost = cost + board[nr][nc]
                if new_cost < distance[nr][nc]:
                    distance[nr][nc] = new_cost
                    heapq.heappush(pq, (new_cost, nr, nc))

if __name__ == '__main__':
    while True:
        n = int(input())
        if n == 0:
            break

        board = [list(map(int, input().split())) for _ in range(n)]
        solve()
        cnt += 1