from collections import deque

n = None
tree = None
remove_node = None
root = None
ans = 0
def init():
    global n
    global tree
    global remove_node, root
    n = int(input())
    tree = [[] for _ in range(n)]
    info = list(map(int, input().split()))
    for i, v in enumerate(info):
        if v == -1:
            root = i
            continue
        tree[v].append(i)

    remove_node = int(input())
    # print(tree)
def remove(target):
    global tree
    # print(target)
    q = deque()
    q.append(target)
    for t in tree:
        if target in t:
            t.remove(target)
    while q:
        now = q.popleft()
        for v in tree[now]:
            q.append(v)

        tree[now].clear()


    # print(tree)

def find_leaf():
    global tree
    global n
    global ans
    q = deque()
    q.append(root)
    
    while q:
        now = q.popleft()
        # print(now)
        if now == remove_node:
            continue
        if not tree[now]:
            ans += 1
        for v in tree[now]:
            if v == remove_node:
                continue
            q.append(v)
    
def main():
    global remove_node
    remove(remove_node)
    find_leaf()
    print(ans)



if __name__ == '__main__':
    init()
    main()
