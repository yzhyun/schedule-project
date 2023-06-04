import sys
sys.stdin = open("../input.txt", "rt")

n = int(input())
ln = list()
money = [0]*3
[ln.append(int(input())) for _ in range(n)]
res = 2147000000
def DFS(L):
    global res
    if L == n:
        diff = max(money)-min(money)
        if diff < res:
            tmp = set()
            for x in money:
                tmp.add(x)
            if len(tmp) == 3:
                res = diff
    else:
        for i in range(3):
            money[i] += ln[L]
            DFS(L+1)
            money[i] -= ln[L]

DFS(0)
print(res)
