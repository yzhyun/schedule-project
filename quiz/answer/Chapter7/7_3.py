import sys
sys.stdin = open("../input.txt", "rt")

k = int(input())
g = list(map(int, input().split()))
s = sum(g)
res = set()

def DFS(L, csum):
    if L == k:
        if 0 < csum <= s:
            res.add(csum)
    else:
        DFS(L+1, csum+g[L])
        DFS(L+1, csum-g[L])
        DFS(L+1, csum)

DFS(0,0)
print(s-len(res))

