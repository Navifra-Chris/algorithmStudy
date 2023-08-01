import sys
from collections import deque

input = sys.stdin.readline


def init():
    n, k = map(int, input().split())
    belts = deque(list(map(int, input().split())))

    return n, k, belts


def solve(n, k, belts):
    cnt = 0
    robot = deque([0 for _ in range(n)])

    while belts.count(0) < k:
        cnt += 1

        # 컨베이어 벨트 회전
        # print(f'### cnt: {cnt}')
        belts.rotate(1)
        robot.rotate(1)
        robot[n - 1] = 0
        # print('회전')
        # print(belts)
        # print(robot, end='\n')

        for i in range(n - 2, -1, -1):
            if robot[i] and robot[i + 1] == 0 and belts[i + 1] > 0:  # i번쨰 로봇이 있고 i+1번째 로봇이 없고 i+1번째 벨트 내구도가 0이상일 때
                robot[i + 1] = 1
                robot[i] = 0
                belts[i + 1] -= 1

            robot[n - 1] = 0

        # print('로봇 움직임')
        # print(belts)
        # print(robot, end='\n')

        if robot[0] == 0 and belts[0] > 0:
            robot[0] = 1
            belts[0] -= 1

        # print('로봇 올림')
        # print(belts)
        # print(robot, end='\n')

        # print('로봇 내림')
        # print(belts)
        # print(robot)
        # print()

    print(cnt)


if __name__ == '__main__':
    n, k, belts = init()
    solve(n, k, belts)
