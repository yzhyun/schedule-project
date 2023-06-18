import sys
sys.stdin = open("../input.txt", "rt")

n, m = map(int, input().split())
lq = [list(map(int, input().split())) for _ in range(n)]
print(lq)

lp = list()
lh = list()

for i in range(n):
    for j in range(n):
        if lq[i][j] == 2:
            lp.append([i, j])
        if lq[i][j] == 1:
            lh.append([i, j])

cb = [0]*m
def DFS(L, s):
    if L == m:
        for i in range(len(lh)):
            x1 = lh[i][0]
            y1 = lh[i][1]
            dis = 2147000000
            for x in cb:
                x2 = lp[x][0]
                y2 = lp[x][1]
                dis = abs(x2-x1) + abs(y2-y1)


    else:
        for i in range(s, len(lp)):
            cb[L] = i
            DFS(L+1, i+1)

DFS(0,0)
