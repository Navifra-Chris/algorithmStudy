import sys
import copy
import pprint

input = sys.stdin.readline

n, m, k = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

rotations = [list(map(int, input().split())) for _ in range(k)]

used = [False for _ in range(k)]

ans = float('inf')


def rotate(selected, rotation_board):
    r, c, s = selected
    ori_board = copy.deepcopy(rotation_board)

    start_r = r - s - 1
    start_c = c - s - 1

    end_r = r + s
    end_c = c + s

    size = s * 2 + 1

    for i, vr in enumerate(range(start_r, end_r)):
        for j, vc in enumerate(range(start_c, end_c)):
            if i <= j and i + j < size - 1:    # right
                # print(f'{vr, vc} : right')
                rotation_board[vr][vc + 1] = ori_board[vr][vc]
            elif i < j and i + j >= size - 1:  # down
                # print(f'{vr, vc} : down')
                rotation_board[vr + 1][vc] = ori_board[vr][vc]
            elif i >= j and i + j > size - 1:  # left
                # print(f'{vr, vc} : left')
                rotation_board[vr][vc - 1] = ori_board[vr][vc]
            elif i > j and i + j <= size - 1:  # up
                # print(f'{vr, vc} : up')
                rotation_board[vr - 1][vc] = ori_board[vr][vc]

    # pprint.pprint(ori_board)
    # pprint.pprint(rotation_board)
    # print()
    return rotation_board


def permutation(selected):
    global ans
    if len(selected) == k:
        # print(used)
        rotation_board = copy.deepcopy(board)
        for i in range(k):
            rotation_board = rotate(selected[i], rotation_board)
            # pprint.pprint(rotation_board)
        value = float('inf')
        for line in rotation_board:
            value = min(value, sum(line))

        ans = min(ans, value)

        return

    for i in range(k):
        if used[i] is False:
            used[i] = True
            selected.append(rotations[i])
            permutation(selected)
            selected.pop()
            used[i] = False



if __name__ == '__main__':
    permutation([])
    print(ans)



