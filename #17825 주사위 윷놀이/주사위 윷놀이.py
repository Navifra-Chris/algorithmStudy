
def dfs(depth, res):
    global arr, stone, ans
    global dice
    # print("DFS", depth, res)
    if depth == 10:
        ans = max(ans, res)
        # print("RETURN")
        return

    for num, info in enumerate(stone):
        branch, loc = info

        if (branch == 0 and loc == 21) or (branch == 4 and loc == 4):
            continue

        di = dice[depth]
        nbranch = branch
        nloc = loc + di

        if branch == 0:
            if nloc == 5:
                nbranch = 1
                nloc = 0
            elif nloc == 10:
                nbranch = 2
                nloc = 0
            elif nloc == 15:
                nbranch = 3
                nloc = 0
            else:
                if nloc > 21:
                    nloc = 21

        elif branch == 1:
            if nloc >= 4:
                nbranch = 4
                nloc -= 4

        elif branch == 2:
            if nloc >= 3:
                nbranch = 4
                nloc -= 3

        elif branch == 3:
            if nloc >= 4:
                nbranch = 4
                nloc -= 4

        elif branch == 4:
            if nloc > 3:
                nloc = 4

        if (nbranch, nloc) == (0, 21) or (nbranch, nloc) == (4,4):
            score = arr[nbranch][nloc]
            stone[num] = (nbranch, nloc)
            dfs(depth + 1, res + score)
            stone[num] = (branch, loc)
            continue
        if (nbranch, nloc) in stone:
            continue
        if (nbranch, nloc) == (0, 20) and (4, 3) in stone:
            continue
        if (nbranch, nloc) == (4, 3) and (0, 20) in stone:
            continue

        score = arr[nbranch][nloc]
        stone[num] = (nbranch, nloc)
        dfs(depth+1, res+score)
        stone[num] = (branch, loc)



if __name__ == '__main__':
    dice = list(map(int, input().split()))

    arr = [[], [], [], [], []]
    arr[0] = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 0]
    arr[1] = [10, 13, 16, 19, 25]
    arr[2] = [20, 22, 24, 25]
    arr[3] = [30, 28, 27, 26, 25]
    arr[4] = [25, 30, 35, 40, 0]

    stone = [(0, 0), (0, 0), (0, 0), (0, 0)]
    ans = 0

    dfs(0, 0)

    print(ans)