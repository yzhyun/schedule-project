import sys
from collections import deque

sys.stdin = open("input.txt", "rt")
n = int(input())
ln = [i for i in range(1, n+1)]

dq = deque(ln)

while len(dq) > 1:
    dq.popleft()
    dq.append(dq.popleft())

print(dq.pop())