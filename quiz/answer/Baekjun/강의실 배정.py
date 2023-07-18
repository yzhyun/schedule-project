import sys
import heapq as hq
sys.stdin = open("../input.txt", "rt")
n = int(input())

classes = [list(map(int, input().split())) for _ in range(n)]
classes.sort(key=lambda x: (x[0], x[1]))

heap = []
hq.heappush(heap, classes[0][1])

for i in range(1, n):
    s, e = classes[i]
    if s >= heap[0]:
        hq.heappop(heap)
        hq.heappush(heap, e)
    else:
        hq.heappush(heap, e)

print(len(heap))




