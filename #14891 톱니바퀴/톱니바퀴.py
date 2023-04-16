import copy

def rotate(dir, chain):
    if dir == 1:
        tmp = chain.pop()
        chain.insert(0, tmp)
    else:
        tmp = chain.pop(0)
        chain.append(tmp)

    # for i in chains:
    #     print(i)
    # print()

    return chain


def solve(rot):
    global ans

    chain_num = rot[0] - 1
    dir = rot[1]

    chain = chains[chain_num]
    p_c = chain[6]
    n_c = chain[2]
    # print("Rotate0:", chain_num)
    chain = rotate(dir, chain)

    dir1 = copy.deepcopy(dir)
    dir2 = copy.deepcopy(dir)

    for i in range(chain_num - 1, -1, -1):
        p = chains[i]
        p_v = p[2]
        dir1 = -dir1
        if p_c != p_v:
            p_c = p[6]
            # print("Rotate1:", i, dir)
            p = rotate(dir1, p)
        else:
            # print("No rotate1", i)
            break

    for i in range(chain_num + 1, 4):
        n = chains[i]
        n_v = n[6]
        dir2 = -dir2
        if n_v != n_c:
            n_c = n[2]
            # print("Rotate2:", i, dir)
            c = rotate(dir2, n)

        else:
            # print("No rotate2", i)
            break


if __name__ == '__main__':
    chains = [[int(x) for x in list(input())] for _ in range(4)]

    N = int(input())

    rots = [[int(x) for x in input().split()] for _ in range(N)]

    ans = 0

    for rot in rots:
        # print("rot", rot)
        # for i in chains:
        #     print(i)
        solve(rot)

    score = 1

    for chain in chains:
        # print(chain)
        if chain[0] == 1:
            ans += score

        score *= 2

    print(ans)