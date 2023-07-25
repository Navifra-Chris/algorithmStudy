import sys
from collections import deque

input = sys.stdin.readline

orders = ['D', 'S', 'L', 'R']
def solve():
    q = deque()
    q.append((a, ''))
    # path = ''
    visited = [0] * 10000
    visited[a] = 1

    while q:
        now, now_path = q.popleft()

        # if now_path == 'LL':
        #     print(f'{now_path} : {now}')
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
                # d1 = now // 1000
                # now = now % 1000
                #
                # d2 = now // 100
                # now = now % 100
                #
                # d3 = now // 10
                # now = now % 10
                #
                # d4 = now

                # L
                if i == 2:
                    # next = d2 * 1000 + d3 * 100 + d4 * 10 + d1
                    next = int((now % 1000) * 10 + (now / 1000))
                    # print(d1,d2,d3,d4)
                    next_path = now_path + 'L'
                    # print(next, next_path)
                # R
                elif i == 3:
                    # next = d4 * 1000 + d1 * 100 + d2 * 10 + d3
                    next = int((now % 10) * 1000 + (now / 10))
                    next_path = now_path + 'R'

            if next is not None and visited[next] == 0:
                q.append((next, next_path))
                visited[next] = 1


if __name__ == '__main__':
    T = int(input())

    for test_case in range(T):
        a, b = map(int, input().split())
        solve()

