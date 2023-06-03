import sys
from collections import deque
sys.stdin = open("../input.txt", "rt")

n = int(input())
lt = deque()
lp = deque()

maxP = -1247000000

for _ in range(n):
    a, b = map(int, input().split())
    lt.append(a)
    lp.append(b)
lt.appendleft(0)
lp.appendleft(0)

def DFS(L, sumP):
    global maxP
    if L == n+1:
        if maxP < sumP:
            maxP = sumP
    else:
        if L + lt[L] <= n+1:
            DFS(L+lt[L], sumP + lp[L])
        DFS(L+1, sumP)

DFS(1, 0)
print(maxP)
