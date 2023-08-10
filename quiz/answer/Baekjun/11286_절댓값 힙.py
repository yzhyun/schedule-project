import sys
from queue import PriorityQueue
sys.stdin = open("input.txt", "rt")

input = sys.stdin.readline

n = int(input())
pq = PriorityQueue()

for i in range(n):
    x = int(input())
    if x == 0:
        if pq.qsize() == 0:
            print(0)
        else:
            print(pq.get()[1])
    else:
        pq.put((abs(x), x))
