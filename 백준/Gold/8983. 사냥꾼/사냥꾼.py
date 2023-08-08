import sys

m, n, l = map(int, input().split())
gun = list(map(int, input().split()))
gun.sort()
animal = []
ans = 0

for i in range(n):
    x, y = map(int, input().split())
    animal.append((x, y))

def solve():
    global ans
    for a, b in animal:
        min = a + b - l     # 사대 위치 x와 (a, b)간의 거리는 |x-a| + b 이므로 이 값이 l보다 작거나 같아야 함
        max = a - b + l     # |x-a| + b <= l 을 풀어서 x의 최소, 최대값 구함

        left = 0
        right = len(gun) - 1

        while left <= right:
            mid = (left + right) // 2
            if min <= gun[mid] <= max:  # 최소, 최대값 안이면 잡을 수 있음
                ans += 1
                break
            elif gun[mid] < min:    # 잡지 못하고 사로가 min 값보다 작을 떄
                left = mid + 1
            elif gun[mid] > max:    # 잡지 못하고 사로가 max 값보다 클 때
                right = mid - 1

    print(ans)

if __name__ == '__main__':
    solve()