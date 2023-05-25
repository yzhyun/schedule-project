import sys
sys.stdin = open("../input.txt", "rt")

n, k = map(int, input().split())
ln = list(map(int, input().split()))
m = int(input())
cnt = 0

def DFS(L, s, csum):
    global cnt
    if L == k:
        if csum % m == 0:
            cnt += 1
    else:
        for i in range(s, n):
            DFS(L+1, i+1, csum+ln[i])


DFS(0, 0, 0)
print(cnt)