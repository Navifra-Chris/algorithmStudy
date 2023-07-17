import sys

input = sys.stdin.readline

n, k = map(int, input().split())
nums = list(map(int, input().split()))

check = [0] * 100001
ans = 0
sum = 0

p1 = p2 = 0

for num in nums:
    check[num] += 1
    p2 += 1

    while check[num] > k:
        if sum > ans:
            ans = sum


        check[nums[p1]] -= 1
        p1 += 1
        sum -= 1

    sum += 1

if sum > ans:
    ans = sum

print(ans)


