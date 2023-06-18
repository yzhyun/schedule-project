import sys
from collections import deque

sys.stdin = open("../input.txt", "rt")

n = int(input())
g = [list(map(int, input())) for _ in range(n)]
a = [[0] * n for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

dq = deque()


def BFS(x, y):
    global nh
    dq.append((x, y))
    g[x][y] = 0
    while dq:
        tmp = dq.popleft()
        for i in range(4):
            xx = tmp[0] + dx[i]
            yy = tmp[1] + dy[i]
            if 0 <= xx < n and 0 <= yy < n and g[xx][yy] == 1:
                nh += 1
                g[xx][yy] = 0
                dq.append((xx, yy))
                a[xx][yy] = 1


cnt = 0
home = list()
for i in range(n):
    for j in range(n):
        if g[i][j] == 1:
            nh = 0
            cnt += 1
            BFS(i, j)
            home.append(nh)

print(cnt)
home.sort()
for x in home:
    print(x)
#
# for i in range(n):
#     for j in range(n):
#         print(a[i][j], end='\t')
#     print()
