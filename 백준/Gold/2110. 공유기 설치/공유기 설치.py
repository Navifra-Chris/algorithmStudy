import sys

input = sys.stdin.readline

def init():
    global n, c, homes, ans

    n, c = map(int, input().split())
    homes = []
    ans = 0
    for i in range(n):
        homes.append(int(input()))
    homes.sort()

def can_install(dist):
    cnt = 1
    curr = homes[0]

    for i, v in enumerate(homes[1:]):
        # print(curr)
        if v - curr >= dist:
            cnt += 1
            curr = v
        else:
            continue

    if cnt >= c:
        return True
    else:
        return False

def solve():
    global ans
    start = 1
    end = homes[-1] - homes[0]

    while start <= end:
        mid = (start + end) // 2
        if can_install(mid):
            ans = max(ans, mid)
            start = mid + 1
        else:
            end = mid - 1




if __name__ == '__main__':
    global ans
    init()
    solve()

    print(ans)
