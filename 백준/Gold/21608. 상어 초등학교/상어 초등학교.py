import sys
import pprint

input = sys.stdin.readline

n = int(input())
room = [[0 for _ in range(n)] for _ in range(n)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
def solve():
    bf_list = [[] for _ in range(n**2 + 1)]
    for i in range(n**2):
        input_data = list(map(int, input().split()))
        student = input_data[0]
        bf = input_data[1:]
        bf_list[student] = bf
        seat_info = [-1, -1, -1, -1]


        for r in range(n):
            for c in range(n):
                if room[r][c]: continue  # 자리가 있는 경우 패스

                bf_cnt = 0
                empty_cnt = 0
                for j in range(4):
                    nr = r + dr[j]
                    nc = c + dc[j]

                    if 0 <= nr < n and 0 <= nc < n:
                        if room[nr][nc] in bf:  # 좋아하는 친구면
                            bf_cnt += 1
                        elif room[nr][nc] == 0:  # 빈자리면
                            empty_cnt += 1

                if seat_info[0] < bf_cnt:  # 1번 조건
                    seat_info = [bf_cnt, empty_cnt, r, c]
                elif seat_info[0] == bf_cnt and seat_info[1] < empty_cnt:  # 2번 조건
                    seat_info = [bf_cnt, empty_cnt, r, c]
                elif seat_info[0] == -1:
                    seat_info = [bf_cnt, empty_cnt, r, c]
                    
        room[seat_info[2]][seat_info[3]] = student
        # 
        # for r in room:
        #     print(r)
        # print()
    score = 0

    for r in range(n):
        for c in range(n):
            student = room[r][c]
            cnt = 0
            for j in range(4):
                nr = r + dr[j]
                nc = c + dc[j]

                if 0 <= nr < n and 0 <= nc < n:
                    if room[nr][nc] in bf_list[student]:
                        cnt += 1

            if cnt > 0:
                score += 10 ** (cnt-1)

    print(score)





if __name__ == '__main__':
    solve()