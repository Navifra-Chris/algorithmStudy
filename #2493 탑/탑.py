N = int(input())

arr = list(map(int, input().split()))
answer = [0] * N
stack = []

for i, t in enumerate(arr):
    while stack:
        if stack[-1][1] > t:
            answer[i] = (stack[-1][0]+1)
            break
        else:
            stack.pop()
    stack.append((i, t))

print(*answer)


