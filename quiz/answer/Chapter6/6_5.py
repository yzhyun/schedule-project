import sys
sys.stdin = open("../input.txt", "rt")

c , n = map(int, input().split())
ln = [ int(input()) for _ in range(n)]
tot = sum(ln)
res = 0
def DFS(L, curSum, tSum):
    global res
    if tot-tSum+res < res:
        return
    if curSum > c:
        return
    if L == n:
        if curSum <= c:
            if curSum > res :
                res = curSum

    else:
        DFS(L+1, curSum + ln[L], curSum+ln[L])
        DFS(L+1, curSum, curSum+ln[L])

DFS(0,0,0)
print(res)