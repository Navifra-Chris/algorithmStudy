import sys

n, m = map(int, input().split())

know_input = list(map(int, input().split()))
know_group = set(know_input[1:])
parties = [set(list(map(int, input().split()))[1:]) for _ in range(m)]

ans = 0

def solve():
    global ans, know_group
    for _ in range(m):
        for party in parties:
            if party & know_group:
                know_group = know_group.union(party)

    for party in parties:
        if party & know_group:
            continue
        ans += 1

    print(ans)



if __name__ == '__main__':
    solve()