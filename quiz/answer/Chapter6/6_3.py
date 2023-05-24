import sys
sys.stdin = open("../input.txt", "rt")

n = int(input())
res = [0]*(n+1)
def DFS(L):
    print(res)
    if L == n+1:
        for i in range(1, n+1):
            if res[i]:
                print(i, end = ' ')
        print()
    else:
        res[L] = 1
        DFS(L+1)
        res[L] = 0
        DFS(L+1)

DFS(1)
