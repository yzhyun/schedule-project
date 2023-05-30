import sys
sys.stdin = open("../input.txt", "rt")

n = int(input())
ln = [i for i in range(n+1)]
res = []


def DFS(L):
    if L == n+1:
        for i in range(len(res)):
            print(res[i], end= ' ')
        print()
    else:
        res.append(ln[L])
        DFS(L+1)
        res.pop()
        DFS(L+1)
DFS(1)