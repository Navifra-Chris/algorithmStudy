import sys

n, m = map(int, input().split())

nums = []

for i in range(n):
    nums.append(int(input()))


nums.sort()

p1 = 0
p2 = 0
ans = float('inf')


# def solve(p1, p2):
#     global ans
#     if p1 >= p2 or nums[p2] - nums[p1] < m:
#         return
#
#     p1_move_gap = nums[p2] - nums[p1 + 1]
#     p2_move_gap = nums[p2 - 1] - nums[p1]
#     # print(p1_move_gap, p2_move_gap)
#
#     if p2_move_gap > p1_move_gap > m:
#         solve(p1 + 1, p2)
#         # print(1)
#     elif p1_move_gap > p2_move_gap > m:
#         solve(p1, p2 - 1)
#         # print(2)
#     else:
#         if p1_move_gap >= m:
#             solve(p1 + 1, p2)
#             solve(p1, p2 - 1)
#             # print(3)
#
#     if nums[p2] - nums[p1] < ans:
#         ans = nums[p2] - nums[p1]

def solve():
    global ans, p1, p2
    while p1 < n and p2 < n:
        gap = nums[p2] - nums[p1]

        if gap < m:
            p2 += 1
        elif gap > m:
            p1 += 1
            if gap < ans:
                ans = gap
        else:
            ans = m
            break

if __name__ == '__main__':
    solve()
    print(ans)


