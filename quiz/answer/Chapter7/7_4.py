import sys

sys.stdin = open("../input.txt", "rt")

p = int(input())
n = int(input())

lc = list()
ln = list()
cnt = 0
for i in range(n):
    a, b = map(int, input().split())
    lc.append(a)
    ln.append(b)

def DFS(L, csum):
    global cnt
    if csum > p:
        return
    if L == n:
        if csum == p:
            cnt += 1
    else:
        for i in range(ln[L]+1):
            DFS(L+1, csum + lc[L]*i)

DFS(0, 0)
print(cnt)