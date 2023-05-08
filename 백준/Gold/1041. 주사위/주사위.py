import sys

input = sys.stdin.readline

pair = [[0, 5], [1, 4], [2, 3]]

n = int(input())

nums = list(map(int, input().split()))
if n == 1:
    print(sum(nums) - max(nums))
    exit()

def is_pair(i, j):
    for p in pair:
        if i in p and j in p:
            return True

def min2():
    min_n = float('inf')
    for i, v in enumerate(nums):
        for j, v2 in enumerate(nums):
            if is_pair(i, j):
                continue

            if v+v2 < min_n:
                min_n = v+v2

    return min_n

def min3():
    min_n = float('inf')

    for i, v in enumerate(nums):
        for j, v2 in enumerate(nums):
            for k, v3 in enumerate(nums):
                if is_pair(i, j) or is_pair(j, k) or is_pair(i, k):
                    continue

                if v+v2+v3 < min_n:
                    min_n = v+v2+v3

    return min_n

surface1_cnt = (n - 2) * (n - 1) * 4 + (n - 2) * (n - 2)
surface2_cnt = (n-1) * 4 + (n-2) * 4
surface3_cnt = 4

surface1_num = min(nums)
surface2_num = min2()
surface3_num = min3()

# print(surface1_num, surface1_cnt)
# print(surface2_num, surface2_cnt)
# print(surface3_num, surface3_cnt)



ans = surface1_num * surface1_cnt + surface2_num * surface2_cnt + surface3_num * surface3_cnt

print(ans)


