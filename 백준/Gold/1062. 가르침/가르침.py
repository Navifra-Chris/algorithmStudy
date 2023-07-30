import sys

input = sys.stdin.readline

def init():
    global n, k, words, ans

    n, k = map(int, input().split())

    words = []
    for i in range(n):
        word = input().strip()
        word = word[4:]
        word = word[:-4]
        words.append(word)

    ans = 0
def count_can_read(read):
    global ans
    cnt_read = 0

    for word in words:
        is_read = True
        for w in word:
            # print(word, w)
            try:
                if read[ord(w) - ord('a')] is False:
                    is_read = False
                    break

            except Exception as e:
                print(e, word, w)

        if is_read:
            cnt_read += 1

    ans = max(ans, cnt_read)


def dfs(cnt, now, read):
    if cnt == k:
        count_can_read(read)
        return
        
    for i in range(now, 26):
        if read[i] is True:
            continue

        read[i] = True
        dfs(cnt+1, i+1, read)
        read[i] = False
def solve():
    read = [False] * 26

    read[ord('a') - ord('a')] = True
    read[ord('n') - ord('a')] = True
    read[ord('t') - ord('a')] = True
    read[ord('i') - ord('a')] = True
    read[ord('c') - ord('a')] = True
    
    if k < 5:
        print(0)
        exit()
    
    dfs(5, 0, read)

if __name__ == '__main__':
    init()
    solve()

    print(ans)