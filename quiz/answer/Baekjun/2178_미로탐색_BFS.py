import sys
from collections import deque
sys.stdin = open("input.txt", "rt")

n, m = map(int, input().split())
g = [list(map(int, input())) for _ in range(n)]
ch = [[False]*m for _ in range(n)]

dq = deque()

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def BFS(x, y):
    dq.append((x, y))

    while dq:
        x, y = dq.popleft()
        ch[x][y] = True
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0<=xx<=(n-1) and 0<=yy<=(m-1) and not ch[xx][yy] and g[xx][yy] == 1:
                dq.append((xx, yy))
                g[xx][yy] = g[x][y]+1
ch[0][0] = 1
BFS(0, 0)

for x in g:
    print(x)
