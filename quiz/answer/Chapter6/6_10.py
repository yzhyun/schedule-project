import sys
sys.stdin = open("../input.txt", "rt")

n, m = map(int, input().split())
res = [0] * (m+1)

def DFS(L, s):
    if L==m:
        for i in range(m):
            print(res[i], end=' ')
        print()
    else:
        for i in range(s, n+1):
            res[L] = i
            DFS(L+1, i+1)

DFS(0, 1)