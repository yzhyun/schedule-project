import sys
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(10000)

input = sys.stdin.readline

n, m = map(int, input().split())

g = [[0] * (n+1) for _ in range(n+1)]
ch = [0] * (n+1)
for i in range(m):
    a, b = map(int, input().split())
    g[a][b] = 1
    g[b][a] = 1
def DFS(x):
    ch[x] = 1
    for x2, val in enumerate(g[x]):
        if val == 1 and ch[x2] == 0:
            DFS(x2)

resCnt = 0
for i in range(1, n+1):
    if ch[i] == 0:
        DFS(i)
        resCnt += 1

print(resCnt)

