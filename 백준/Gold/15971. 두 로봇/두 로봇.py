import sys
sys.setrecursionlimit(10**5)

input = sys.stdin.readline

n, start, target = map(int, input().split())

room_info = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for _ in range(n-1):
    r1, r2, cost = map(int, input().split())

    room_info[r1].append((cost, r2))
    room_info[r2].append((cost, r1))



def solve(start, total_cost, max_cost):
    visited[start] = True

    if start == target:
        # print(start, target)
        print(total_cost - max_cost)
        exit(0)

    for next_room in room_info[start]:
        next_cost, next = next_room
        if visited[next] == True:
            continue
        solve(next, total_cost+next_cost, max(max_cost, next_cost))





if __name__ == '__main__':
    solve(start, 0, 0)

