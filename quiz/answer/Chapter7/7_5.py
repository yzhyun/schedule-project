import sys
sys.stdin = open("../input.txt")

n = int(input())
ln = [int(input()) for _ in range(n)]


lp = [0]*3

minDiff = 2147000000

def DFS(L):
    global minDiff
    if L == n:
        diff = max(lp)-min(lp)
        if diff < minDiff:
            res = set()
            for v in lp:
                res.add(v)
            if len(res) == 3:
                minDiff = diff
    else:
        for i in range(3):
            lp[i] += ln[L]
            DFS(L+1)
            lp[i] -= ln[L]
DFS(0)
print(minDiff)
