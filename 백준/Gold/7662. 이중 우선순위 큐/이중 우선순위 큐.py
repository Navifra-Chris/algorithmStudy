import sys
import heapq

input = sys.stdin.readline

t = int(input())

def solve():
    orders = int(input())

    min_heap = []
    max_heap = []
    count = {}

    for _ in range(orders):
        order, n = input().split()
        n = int(n)

        if order == 'I':
            if n not in count:
                count[n] = 1
            else:
                count[n] += 1
            heapq.heappush(min_heap, n)
            heapq.heappush(max_heap, -n)
        elif order == 'D':
            if n == -1 and min_heap:
                while min_heap and (min_heap[0] not in count or count[min_heap[0]] == 0):
                    heapq.heappop(min_heap)
                if min_heap:
                    count[min_heap[0]] -= 1
                    if count[min_heap[0]] == 0:
                        del count[min_heap[0]]
                    heapq.heappop(min_heap)
            elif n == 1 and max_heap:
                while max_heap and (-max_heap[0] not in count or count[-max_heap[0]] == 0):
                    heapq.heappop(max_heap)
                if max_heap:
                    count[-max_heap[0]] -= 1
                    if count[-max_heap[0]] == 0:
                        del count[-max_heap[0]]
                    heapq.heappop(max_heap)

    while min_heap and (min_heap[0] not in count or count[min_heap[0]] == 0):
        heapq.heappop(min_heap)
    while max_heap and (-max_heap[0] not in count or count[-max_heap[0]] == 0):
        heapq.heappop(max_heap)

    if not min_heap or not max_heap:
        print('EMPTY')
    else:
        print(-max_heap[0], min_heap[0])

if __name__ == '__main__':
    for test_case in range(t):
        solve()
