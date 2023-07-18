import sys
from collections import deque
sys.stdin = open("../input.txt", "rt")

n, m = map(int, input().split())
ln = list(map(int, input().split()))
dq = deque()
for i in range(n):
    dq.append((i, ln[i]))
print(dq)

cnt = 0
while True:
    tget = dq.popleft()
    print(tget)
    if any(tget[1] < x[1] for x in dq):
        dq.append(tget)
    else:
        cnt += 1
        if tget[0] == m:
            print(cnt)
            break
