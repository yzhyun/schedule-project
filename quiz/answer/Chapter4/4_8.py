import sys
from collections import deque
sys.stdin=open("../input.txt", "rt")

n, m = map(int, input().split())
ln = list(map(int, input().split()))
ln.sort()
dq = deque(ln)

cnt = 0
while dq:
    if len(dq) == 1:
        cnt += 1
        break
    if dq[0]+dq[-1] > m:
        dq.pop()
        cnt += 1
    else:
        dq.popleft()
        dq.pop()
        cnt += 1

print(cnt)





