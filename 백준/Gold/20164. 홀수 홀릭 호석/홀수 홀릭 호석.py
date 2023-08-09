import sys

n = int(input())
odd = 0
min_odd = float('inf')
max_odd = 0


def solve(n, odd_cnt):
    global max_odd, min_odd
    str_n = str(n)

    if n // 10 < 1:
        if n % 2 == 1:
            odd_cnt += 1
        max_odd = max(max_odd, odd_cnt)
        min_odd = min(min_odd, odd_cnt)
        return

    for i in map(int, str_n):
        if i % 2 == 1:
            odd_cnt += 1

    if n // 100 >= 1:   # 3자리 이상
        for i in range(1, len(str_n)-1):
            for j in range(i+1, len(str_n)):
                next = int(str_n[:i]) + int(str_n[i:j]) + int(str_n[j:])
                solve(next, odd_cnt)

    elif n // 10 >= 1:  # 2자리
        next = int(str_n[0]) + int(str_n[1])
        solve(next, odd_cnt)


if __name__ == '__main__':
    solve(n, 0)
    print(min_odd, max_odd)


