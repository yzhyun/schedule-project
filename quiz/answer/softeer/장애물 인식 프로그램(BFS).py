import sys
from collections import deque
sys.stdin = open("../input.txt", "rt")

n = int(input())
g = [list(map(int, input())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

dq = deque()
res = []
cnt = 0

for x in range(n):
    for y in range(n):
        if g[x][y] == 1:
            g[x][y] = 0
            dq.append((x, y))
            cnt += 1
            subcnt = 1
            while dq:

                tmp = dq.popleft()
                for i in range(4):
                    xx = tmp[0] + dx[i]
                    yy = tmp[1] + dy[i]
                    if 0<=xx<n and 0<=yy<n and g[xx][yy] == 1:
                        g[xx][yy] = 0
                        dq.append((xx, yy))
                        subcnt += 1
            res.append(subcnt)
print(cnt)
print(res)