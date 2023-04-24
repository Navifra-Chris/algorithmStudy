import sys

input = sys.stdin.readline


def dfs(depth, start):
    global answer
    # print(visited)
    if depth == 5 or answer == 1:
        answer = 1
        # print(visited)
        return

    # print(graph[start])
    for i in graph[start]:
        # print(i, visited[i])
        if not visited[i]:
            visited[i] = True
            dfs(depth + 1, i)
            visited[i] = False

    visited[start] = True

if __name__ == '__main__':
    n, m = map(int, input().split())

    graph = [[] for _ in range(n)]
    for i in range(m):
        p1, p2 = map(int, input().split())
        graph[p1].append(p2)
        graph[p2].append(p1)

    visited = [False] * n

    answer = 0
    for i in range(n):
        visited[i] = True
        dfs(1, i)
        visited[i] = False
        if answer == 1:
            break

    print(answer)





