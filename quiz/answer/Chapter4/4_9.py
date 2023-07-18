import sys
from collections import deque
sys.stdin = open("../input.txt", "rt")

n = int(input())
ln = list(map(int, input().split()))
dq = deque(ln)

sRslt = ""
val = 0
lVal = 0
while dq:
    a = dq[0]
    b = dq[-1]
    if lVal > dq[0] and lVal > dq[-1]:
        break
    if dq[0] < dq[-1]:
        if dq[0] > lVal:
            lVal = dq.popleft()
            sRslt += "L"
        else:
            lVal = dq.pop()
            sRslt += "R"
    else:
        if dq[-1] > lVal:
            lVal = dq.pop()
            sRslt += "R"
        else:
            lVal = dq.popleft()
            sRslt += "L"
print(sRslt)