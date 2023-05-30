import sys
sys.stdin = open("../input.txt", "rt")

C, N = map(int, input().split())
a = [int(input()) for _ in range(N)]
maxVal = -2147000000
totSum = sum(a)
def DFS(L, csum, tsum):
    global maxVal
    if csum + (totSum-tsum) < maxVal:
        return
    if csum > C:
        return
    if L == N:
        if maxVal < csum:
            maxVal = csum

    else:
        DFS(L+1, csum+a[L], tsum+a[L])
        DFS(L+1, csum, tsum+a[L])

DFS(0, 0,0)
print(maxVal)