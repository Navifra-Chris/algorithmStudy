import sys

input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))
ans = 0

def check_num(new_arr, number):
    global ans
    left = 0
    right = len(new_arr) - 1

    while left < right:
        sum_num = new_arr[left] + new_arr[right]
        if sum_num == number:
            ans += 1
            # print(number, new_arr[left], new_arr[right])
            break
        elif sum_num < number:
            left += 1
        elif sum_num > number:
            right -= 1


def solve():
    arr.sort()
    for i in range(n):
        new_arr = arr[:i] + arr[i+1:]
        number = arr[i]

        check_num(new_arr, number)

    print(ans)


if __name__ == '__main__':
    solve()


