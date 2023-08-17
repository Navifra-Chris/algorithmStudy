import sys

input = sys.stdin.readline

n, m = map(int, input().split())
n_paper = int(input())
n_wrong_area = int(input())
wrong_area = [list(map(int, input().split())) for _ in range(n_wrong_area)]
wrong_area.sort(key=lambda x: x[1])
ans = float('inf')

def cal_paper(size):
    cur_x = wrong_area[0][1]
    cnt = 1
    for y, x in wrong_area[1:]:
        if x > cur_x + size - 1:
            cur_x = x
            cnt += 1

    return cnt


def solve():
    global ans
    left = max(wrong_area, key=lambda x:x[0])[0]
    right = min(n, m)

    while left <= right:
        mid = (left + right) // 2
        cnt_paper = cal_paper(mid)
        if cnt_paper <= n_paper:
            ans = min(ans, mid)
        if cnt_paper <= n_paper:
            right = mid - 1
        else:
            left = mid + 1

    print(ans)
if __name__ == '__main__':
    solve()