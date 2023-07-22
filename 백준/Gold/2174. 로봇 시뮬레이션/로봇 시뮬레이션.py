import sys

a, b = map(int, input().split())
n, m = map(int, input().split())

board = [[0 for _ in range(a)] for _ in range(b)]
robots = []
dirs = ['N', 'W', 'S', 'E']
dirs2 = ['N', 'E', 'S', 'W']

drc = {'N': [-1, 0], 'W': [0, -1], 'S': [1, 0], 'E': [0, 1]}

for i in range(n):
    input_data = input().split()
    x, y = map(int, input_data[:2])
    r, c = b-y, x-1
    d = input_data[2]
    robots.append([r, c, d])
    board[r][c] = i+1

for i in range(m):
    input_data = input().split()
    robot_num = int(input_data[0]) - 1
    order = input_data[1]
    times = int(input_data[2])

    cur_robot = robots[robot_num]

    cur_r = robots
    if order == 'L':
        cur_dir = dirs.index(cur_robot[2])
        next_dir_idx = (cur_dir + (times % 4)) % 4
        next_dir = dirs[next_dir_idx]
        robots[robot_num][2] = next_dir

        # print(f'L: {cur_dir} -> {next_dir}')

    elif order == 'R':
        cur_dir = dirs2.index(cur_robot[2])
        next_dir_idx = (cur_dir + (times % 4)) % 4
        next_dir = dirs2[next_dir_idx]
        robots[robot_num][2] = next_dir

        # print(f'R: {cur_dir} -> {next_dir}')

    elif order == 'F':
        next_drc = drc[cur_robot[2]]
        now_r, now_c = cur_robot[0], cur_robot[1]

        for i in range(times):
            cur_robot_num = board[now_r][now_c]
            board[now_r][now_c] = 0

            now_r = now_r + next_drc[0]
            now_c = now_c + next_drc[1]

            # print(now_r, now_c)
            if not (0 <= now_r < b and 0 <= now_c < a):
                print(f'Robot {robot_num+1} crashes into the wall')
                exit()

            if board[now_r][now_c] != 0:
                print(f'Robot {robot_num+1} crashes into robot {board[now_r][now_c]}')
                exit()

            board[now_r][now_c] = cur_robot_num
            robots[cur_robot_num - 1][0] = now_r
            robots[cur_robot_num - 1][1] = now_c

print('OK')

