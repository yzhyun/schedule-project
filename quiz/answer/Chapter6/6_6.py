import sys
sys.stdin=open("../input.txt", "r")

n ,m = map(int, input().split())
res = [0]*m
cnt = 0
def DFS(L):
    global cnt
    if L == m:
        for i in range(m):
           print(res[i], end = ' ')
        print()
        cnt += 1
    else:
        for i in range(1, n+1):
            res[L] = i
            DFS(L+1)

DFS(0)
print(cnt)