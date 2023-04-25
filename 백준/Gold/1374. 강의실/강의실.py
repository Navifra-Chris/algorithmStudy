import sys
import heapq

input = sys.stdin.readline


n = int(input())
lectures = []
for i in range(n):
    num, start, end = map(int, input().split())
    lectures.append((start, end))

lectures.sort()


rooms = []

heapq.heappush(rooms, (lectures[0][1], lectures[0][0]))

for lecture in lectures[1:]:
    n_start, n_end = lecture
    end, start = rooms[0]
    if end <= n_start:
        heapq.heappop(rooms)
        heapq.heappush(rooms, (n_end, n_start))
    else:
        heapq.heappush(rooms, (n_end, n_start))

print(len(rooms))


