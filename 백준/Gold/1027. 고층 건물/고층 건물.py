n = int(input())

buildings = list(map(int, input().split()))


def can_view(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    a = (y2 - y1) / (x2 - x1)
    b = y1 - (a * x1)

    for x in range(min(x1, x2) + 1, max(x1, x2)):
        cur_h = buildings[x]
        limit_h = a * x + b

        if cur_h >= limit_h:
            return False

    return True


if __name__ == '__main__':
    ans = 0

    for i in range(n):
        sum = 0
        for j in range(n):
            if i == j:
                continue
            if can_view((i, buildings[i]), (j, buildings[j])):
                sum += 1

            if sum >= ans:
                ans = sum
    print(ans)