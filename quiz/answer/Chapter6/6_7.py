import sys
sys.stdin = open("../input.txt", "rt")

n = int(input())
ln = list(map(int, input().split()))
ln.sort(reverse=True)
m = int(input())
res = 2147000000

def DFS(L, csum):
    global res
    if L >= res:
        return
    if csum > m:
        return
    if csum == m:
        if res > L:
            res = L

    else:
        for i in range(n):
            DFS(L+1, csum + ln[i])

DFS(0, 0)
print(res)
