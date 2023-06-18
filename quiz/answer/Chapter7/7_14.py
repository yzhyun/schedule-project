import sys
from collections import deque
sys.stdin = open("../input.txt", "rt")

dq = deque()
n = int(input())

q = [list(map(int, input().split())) for _ in range(n)]

maxVal = -2147000000
minVal = 2147000000
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
res = list()

for row in q:
    tmpMax = max(row)
    tmpMin = min(row)
    if tmpMax > maxVal:
        maxVal = tmpMax
    if tmpMin < minVal:
        minVal = tmpMin

for z in range(minVal+1, maxVal):
    g = [[0] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if g[i][j] == 0 and z < q[i][j]:
                dq = deque()
                dq.append((i, j))
                g[i][j] = 1
                while dq:
                    tmp = dq.popleft()
                    for ii in range(4):
                        x = tmp[0] + dx[ii]
                        y = tmp[1] + dy[ii]
                        if 0<=x<n and 0<=y<n and g[x][y] == 0 and q[x][y] > z:
                            g[x][y] = 1
                            dq.append((x,y))
                cnt += 1
    res.append(cnt)
print(res)





