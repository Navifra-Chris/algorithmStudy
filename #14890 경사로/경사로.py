
def solve():
    global ans

    for r in range(N):
        check = [False for _ in range(N)]
        for c in range(N):
            if c == N-1:
                ans += 1
                break

            if abs(board[r][c] - board[r][c+1]) > 1:
                break

            if abs(board[r][c] - board[r][c+1]) == 0:
                continue

            if board[r][c] - board[r][c+1] == -1:
                flag = True
                for i in range(c, c - L, -1):
                    if i < 0 or i >= N or board[r][i] != board[r][c] or check[i] is True:
                        flag = False
                        break
                    check[i] = True

                if flag is False:
                    break


            elif board[r][c] - board[r][c+1] == 1:
                flag = True
                for i in range(c + 1, c + 1 + L):
                    if i < 0 or i >= N or board[r][i] != board[r][c+1] or check[i] is True:
                        flag = False
                        break
                    check[i] = True

                if flag is False:
                    break



if __name__ == '__main__':
    N, L = list(map(int, input().split()))
    board = [[int(x) for x in input().split()] for _ in range(N)]
    ans = 0

    solve()

    board = list(map(list, zip(*board)))

    solve()

    print(ans)