import sys
sys.stdin = open("../input.txt", "rt")

n = int(input())
ln = list(map(int, input().split()))
totSum = sum(ln)

def DFS(L, cSum):
    if totSum // 2 > cSum:
        return
    if L == n:
        if cSum == totSum - cSum:
            print("YES")
            sys.exit(0)
    else:
        DFS(L+1, cSum + ln[L])
        DFS(L+1, cSum)

DFS(0,0)
print("NO")
