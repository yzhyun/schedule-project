import sys
sys.stdin = open("../input.txt", "rt")

T = int(input())
k = int(input())

lw = list()
lc = list()

cnt = 0
for i in range(k):
    a, b = map(int, input().split())
    lw.append(a)
    lc.append(b)

def DFS(L, csum):
    global cnt
    if csum > T:
        return
    if L == k:
        if csum == T:
            cnt += 1
    else:
        for i in range(lc[L]+1):
            DFS(L+1, csum + lw[L]*i)

DFS(0,0)
print(cnt)