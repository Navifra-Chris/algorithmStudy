import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
ans = float('inf')
ans_left = None
ans_right = None

def solve():
    global ans
    left = 0
    right = len(arr) - 1

    while left < right:
        result = arr[left] + arr[right]
        if abs(result) < ans:
            ans = abs(result)
            ans_left = left
            ans_right = right
        if result < 0:
            left += 1
        elif result > 0:
            right -= 1
        else:
            break

    print(min(arr[ans_left], arr[ans_right]), max(arr[ans_left], arr[ans_right]))

if __name__ == '__main__':
    solve()