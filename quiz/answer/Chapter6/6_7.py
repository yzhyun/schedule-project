import sys
sys.stdin = open("../input.txt", "rt")

n = int(input())
ln = list(map(int, input().split()))
ln.sort(reverse=True)
m = int(input())
minVal = 2147000000

def DFS(L, csum):
    global minVal
    if L > minVal :
        return
    if csum > m:
        return
    if csum == m:
        if minVal > L :
            minVal = L
    else:
        for i in range(n):
            DFS(L+1, csum + ln[i])

DFS(0, 0)
print(minVal)