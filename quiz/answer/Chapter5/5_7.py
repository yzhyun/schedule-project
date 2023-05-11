import sys
from collections import deque
sys.stdin=open("../input.txt", "rt")

sMandatory = input()
n = int(input())

print(sMandatory, n)
for i in range(n):
    plan = input()
    dQ = deque(sMandatory)

    for s in plan:
        if s in dQ :
            if s != dQ.popleft() :
                print("#%d NO" %(i+1))
                break
    else :
        if len(dQ) == 0:
            print("#%d YES" %(i+1))
        else :
            print("#%d NO" % (i + 1))


