import sys

input = sys.stdin.readline

m, n = map(int, input().split())
multiverse = {}
ans = 0

for i in range(m):
    input_data = list(map(int, input().split()))
    sorted_data = sorted(list(set(input_data)))

    # 중복을 허용한 순위 매기기
    rank = {num: idx for idx, num in enumerate(sorted_data)}

    verse = tuple(rank[num] for num in input_data)

    multiverse[verse] = multiverse.get(verse, 0) + 1


def solve():
    global ans
    for cnt in multiverse.values():
        ans += cnt * (cnt - 1) // 2

    print(ans)


if __name__ == '__main__':
    solve()
