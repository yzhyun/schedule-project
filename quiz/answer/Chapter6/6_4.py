import sys
sys.stdin = open("../input.txt", "rt")

def DFS(L, curSum):
    if L == n:
        if totSum == totSum - curSum:
            print("YES")
            sys.exit(0)
    else:
        DFS(L+1, curSum+a[L])
        DFS(L+1, curSum)

if __name__ == "__main__" :
    n = int(input())
    a = list(map(int, input().split()))

    totSum = sum(a)
    DFS(0, 0)
    print("NO")



