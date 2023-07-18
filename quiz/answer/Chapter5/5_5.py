import sys
from collections import deque
sys.stdin=open("../input.txt", "rt")

n, k = map(int, input().split())
ln = [ i for i in range(1, n+1)]

dq = deque(ln)
print(dq)

while dq:
    if len(dq) == 1:
        print(dq[0])
        break
    else:
        for i in range(k-1):
            dq.append(dq.popleft())
        dq.popleft()
