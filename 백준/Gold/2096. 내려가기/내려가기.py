import sys
from collections import deque
import copy
import pprint

input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())

    dp_min = list(map(int, input().split()))
    dp_max = copy.deepcopy(dp_min)

    for i in range(n - 1):
        cur_nums = list(map(int, input().split()))

        dp_min0 = min(cur_nums[0] + dp_min[0], cur_nums[0] + dp_min[1])
        dp_max0 = max(cur_nums[0] + dp_max[0], cur_nums[0] + dp_max[1])

        dp_min1 = min(cur_nums[1] + dp_min[0], cur_nums[1] + dp_min[1], cur_nums[1] + dp_min[2])
        dp_max1 = max(cur_nums[1] + dp_max[0], cur_nums[1] + dp_max[1], cur_nums[1] + dp_max[2])

        dp_min2 = min(cur_nums[2] + dp_min[1], cur_nums[2] + dp_min[2])
        dp_max2 = max(cur_nums[2] + dp_max[1], cur_nums[2] + dp_max[2])

        dp_min[0] = dp_min0
        dp_min[1] = dp_min1
        dp_min[2] = dp_min2

        dp_max[0] = dp_max0
        dp_max[1] = dp_max1
        dp_max[2] = dp_max2

        # print()
        # pprint.pprint(f'{dp_max}, {dp_min}')

    print(max(dp_max), min(dp_min))




