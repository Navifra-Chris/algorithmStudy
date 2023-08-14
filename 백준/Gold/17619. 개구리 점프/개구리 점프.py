import sys

n, q = map(int, input().split())

trees = [list(map(int, input().split())) + [i+1] for i in range(n)]

trees.sort()

parent = [i for i in range(n+1)]

def find_parent(x):
    if parent[x] == x:
        return x
    parent[x] = find_parent(parent[x])
    return parent[x]


def union(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def solve():
    now_start, now_end, _, now_idx = trees[0]

    for i in range(1, n):
        next_start, next_end, _, next_idx = trees[i]

        if now_start <= next_start <= now_end:
            union(now_idx, next_idx)

            if next_end >= now_end:
                now_start, now_end, now_idx = next_start, next_end, next_idx

        else:
            now_start, now_end, now_idx = next_start, next_end, next_idx

    for _ in range(q):
        a, b = map(int, input().split())
        if parent[a] == parent[b]:
            print(1)
        else:
            print(0)


if __name__ == '__main__':
    solve()



