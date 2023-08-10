import sys
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n, m, s = map(int, input().split())
g = [[0] * (n+1) for _ in range(n+1)]
ch = [False] * (n+1)

#인접행렬 만들기
for i in range(m):
    a, b = map(int, input().split())
    g[a][b] = g[b][a] = 1


for x in g:
    print(x)

def DFS(v):
    ch[v] = True
    for i in range(n+1):
       3g





