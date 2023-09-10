import sys

n, m, l = map(int, input().split())

stations = [0] + list(map(int, input().split())) + [l]
stations.sort()
ans = 0
def solve():
    global ans
    start = 1
    end = l-1
    while start <= end:
        mid = (start+end) // 2
        cnt = 0
        for i in range(1, len(stations)):
            if stations[i] - stations[i-1] > mid:
                cnt += (stations[i] - stations[i-1] - 1) // mid

        if cnt > m:
            start = mid + 1
        # elif cnt < m:

        else:
            end = mid - 1
            ans = mid

    print(ans)

if __name__ == '__main__':
    solve()