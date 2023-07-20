h, w = map(int, input().split())
world = list(map(int, input().split()))

left, right = 0, w - 1
left_max, right_max = world[left], world[right]
ans = 0

while left < right:
    if world[left] < world[right]:
        if world[left] > left_max:
            left_max = world[left]
        else:
            ans += left_max - world[left]
        left += 1
    else:
        if world[right] > right_max:
            right_max = world[right]
        else:
            ans += right_max - world[right]
        right -= 1

print(ans)
