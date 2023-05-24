import sys
sys.stdin = open("../input.txt", "rt")

n, k = map(int, input().split())
ln = list(map(int, input().split()))
m = int(input())

print(n, k)
print(ln)
print(m)
cnt = 0
ssum = 0

def DFS(L, s, ssum):
    global cnt
    if L == k:
        if ssum % m == 0:
            cnt += 1

    else:
        for i in range(s, n):
            DFS(L+1, i+1, ssum+ln[i])

DFS(0, 0, 0)
print(cnt)