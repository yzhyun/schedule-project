import sys
sys.stdin = open("../input.txt", "rt")

n, m = map(int, input().split())
res = [0]*n
cnt=0
def DFS(L):
    global cnt
    if L == m:
        for i in range(m):
            print(res[i], end=' ')
        cnt += 1
        print()
    else :
        for i in range(1, n+1):
            res[L] = i
            DFS(L+1)

DFS(0)
print(cnt)

print(res)



