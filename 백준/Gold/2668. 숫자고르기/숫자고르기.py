import sys

input = sys.stdin.readline




n = int(input())

nums = [0]

visited = [False] * n
visited2 = [False] * n

ans = []
for i in range(1, n+1):
    num = int(input())
    nums.append((i, num))

for i in range(1, n+1):
    v = nums[i]
    start = v[0]
    for k in range(n):
        n_num = v[1]
        if n_num == start:
            ans.append(start)
            break
        v = nums[n_num]

print(len(ans))
for v in ans:
    print(v)









