import copy

def move_fish():
    # print("MOVE")
    for i in range(1, 17):  # fish 1 to 16
        if i not in fish:
            continue

        f = fish[i]
        r = f[0]
        c = f[1]
        dir = MAP[r][c][1]

        for j in range(8):  # dir 1 to 8
            nd = (dir+j) % 8
            nr = r + dr[nd]
            nc = c + dc[nd]

            if not 0 <= nr < 4 or \
                    not 0 <= nc < 4 or \
                    MAP[nr][nc][0] == -1:  # If out or Shark
                continue

            fish[MAP[nr][nc][0]] = (r, c)
            fish[i] = (nr, nc)
            MAP[r][c], MAP[nr][nc] = MAP[nr][nc], MAP[r][c]
            MAP[nr][nc][1] = nd
            break


def dfs(_shark_pos, _shark_dir, cnt):
    global ans, MAP, fish

    r = _shark_pos[0]
    c = _shark_pos[1]
    d = _shark_dir

    move_fish()

    while True:
        nr = r + dr[d]
        nc = c + dc[d]
        if not 0 <= nr < 4 or not 0 <= nc < 4:
            ans = max(ans, cnt)
            # print("RETURN")
            return

        if MAP[nr][nc][0] == 0:
            # print("PASS")
            r, c = nr, nc
            continue

        tmp_MAP = copy.deepcopy(MAP)
        tmp_fish = copy.deepcopy(fish)
        nd = MAP[nr][nc][1]
        eat = MAP[nr][nc][0]
        # print(fish)
        fish.pop(eat)
        MAP[_shark_pos[0]][_shark_pos[1]] = [0, 0]
        MAP[nr][nc] = [-1, nd]

        dfs((nr, nc), nd, cnt+eat)
        MAP = copy.deepcopy(tmp_MAP)
        fish = copy.deepcopy(tmp_fish)
        r, c = nr, nc


if __name__ == '__main__':
    MAP = [[0 for _ in range(4)] for _ in range(4)]
    fish = dict()

    r, c = 0, 0
    for i in range(4):
        arr = list(map(int, input().split()))
        for j in range(0, len(arr), 2):
            f, dir = arr[j], arr[j+1] - 1
            MAP[r][c] = [f, dir]
            fish[f] = (r, c)
            c += 1
        r += 1
        c = 0

    dr = [-1, -1, 0, 1, 1, 1, 0, -1]  # idx 0 == buffer
    dc = [0, -1, -1, -1, 0, 1, 1, 1]

    shark_pos = (0, 0)
    shark_dir = MAP[0][0][1]
    fish.pop(MAP[0][0][0])
    ans = MAP[0][0][0]
    MAP[0][0] = [-1, MAP[0][0][1]]

    dfs(shark_pos, shark_dir, ans)

    print(ans)