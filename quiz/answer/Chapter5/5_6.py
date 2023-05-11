import sys
from collections import deque

sys.stdin=open("../input.txt", "rt")

n, k = map(int, input().split())
lq = [ [i, val] for i, val in enumerate(list(map(int, input().split())))]
Q = deque(lq)

print(n, k)
print(lq)
cnt=0
while True :
    cur = Q.popleft()
    if any(cur[1] < x[1] for x in Q):
        Q.append(cur)
    else :
        cnt+=1
        if(cur[0] == k):
            print(cnt)
            break
