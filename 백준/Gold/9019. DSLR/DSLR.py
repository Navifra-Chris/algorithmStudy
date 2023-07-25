import sys
from collections import deque

input = sys.stdin.readline

orders = ['D', 'S', 'L', 'R']
def solve():
    q = deque()
    q.append((a, ''))
    visited = [0] * 10000
    visited[a] = 1

    while q:
        now, now_path = q.popleft()

        if now == b:
            print(now_path)
            break

        next = None

        for i in range(4):
            if i == 0:  # D
                next = (now * 2) % 10000
                next_path = now_path + 'D'

            elif i == 1:  # S
                next = now - 1

                if now == 0:
                    next = 9999

                next_path = now_path + 'S'

            elif i == 2 or i == 3:  # L or R
                # L
                if i == 2:
                    next = (now % 1000) * 10 + (now // 1000)
                    next_path = now_path + 'L'
                # R
                elif i == 3:
                    next = (now % 10) * 1000 + (now // 10)
                    next_path = now_path + 'R'

            if next is not None and visited[next] == 0:
                q.append((next, next_path))
                visited[next] = 1


if __name__ == '__main__':
    T = int(input())

    for test_case in range(T):
        a, b = map(int, input().split())
        solve()

