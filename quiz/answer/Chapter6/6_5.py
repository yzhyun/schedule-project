import sys

sys.stdin = open("../input.txt", "rt")

def DFS(L, curSum, tSum):
    global totSum
    if curSum + (sum(ln)-tSum)<totSum:
        return
    if curSum > w:
        return
    if L == n:
        if curSum > totSum:
            totSum = curSum
    else:
        DFS(L+1, curSum+ln[L], tSum+ln[L])
        DFS(L+1, curSum, tSum+ln[L])


if __name__ == "__main__":
    w, n = map(int, input().split())
    ln = [int(input()) for i in range(n)]
    curSum = 0
    totSum = 0

    print(w, n)
    print(ln)

    DFS(0, 0, 0)
    print(totSum)

    la = [[1,10],[1,1]]
    la.sort(key=lambda x:x[1])
    print(la)