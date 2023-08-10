import sys
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(10000)

n, m = map(int, input().split())

g = [[0] * (n+1) for _ in range(n+1)]
ch = [0] * (n+1)
arrive = False

for _ in range(m):
    a, b = map(int, input().split())
    g[a][b] = 1
    g[b][a] = 1

for x in g:
    print(x)

def DFS(v, L):
    global arrive
    ch[v] = 1
    if L == 5:
        arrive = True
        print(v)
        return
    else:
        for idx, val in enumerate(g[v]):
            if val == 1 and ch[idx] == 0:
                DFS(idx, L+1)
    ch[v] = 0

for i in range(n):
    DFS(i, 1)
    if arrive:
        break

if arrive:
    print(1)
else:
    print(0)




