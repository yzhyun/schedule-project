import sys
sys.stdin = open("../input.txt", "rt")

n,m = map(int, input().split())
res = [0]*m
cnt = 0
def DFS(L, s):
    global cnt
    if L == m:
        for i in range(m):
            print(res[i], end = ' ')
        print()
        cnt += 1
    else:
        for i in range(s, n+1):
            res[L] = i
            DFS(L+1, i+1)

DFS(0, 1)
print(cnt)
