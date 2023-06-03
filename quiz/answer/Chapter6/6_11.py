import sys
sys.stdin = open("../input.txt", "rt")

n, k = map(int, input().split())
ln = list(map(int, input().split()))
m = int(input())
cnt = 0
res = [0]*(m+1)
def DFS(L, s):
    global cnt
    if L == k:
        if sum(res) % m ==0:
            cnt += 1
    else:
        for i in range(s, n):
            res[L] = ln[i]
            DFS(L+1, i+1)

DFS(0, 0)
print(cnt)