import sys
sys.stdin = open("../input.txt", "rt")

n, m = map(int, input().split())
ls = list()
lt = list()
for _ in range(n):
    a, b = map(int,input().split())
    ls.append(a)
    lt.append(b)
maxScore = -1247000000

res = list()
def DFS(L, sumS, sumT):
    global maxScore
    if sumT > m:
        return
    if L == n:
        if maxScore < sumS:
            maxScore = sumS
        for x in res:
            print(x, end= ' ')
        print()
    else:
        res.append(ls[L])
        DFS(L+1, sumS + ls[L], sumT + lt[L])
        res.pop()
        DFS(L+1, sumS, sumT)


DFS(0, 0 , 0)
print(maxScore)
print(res)


