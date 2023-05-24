import sys
sys.stdin = open("../input.txt", "rt")

n = int(input())
ln = list(map(int, input().split()))
tot = sum(ln)

def DFS(L, curSum):
    if curSum > tot // 2:
        return
    if L == n:
        if tot-curSum == curSum:
            print("YES")
            sys.exit(0)

    else:
        DFS(L+1, curSum+ln[L])
        DFS(L+1, curSum)

DFS(0,0)
print("NO")