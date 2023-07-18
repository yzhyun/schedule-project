import sys
from collections import deque
quiz = ["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]

arr = []
for i in range(len(quiz)):
    arr.append(quiz[i])

for i in arr:
    print(i)

dq = deque()
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
res = []
def BFS(x, y):
    dq.append((x, y))
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            xx = dx[i] + x
            yy = dy[i] + y

            if 0<=xx<5 and 0<=yy<len(quiz) and (arr[xx][yy] == 'O' or arr[xx][yy] == 'L'):
                arr[xx][yy] = 'X'
                arr[xx][yy].
                dq.append((xx, yy))
    else:
        res.append((x, y))


for i in range(len(quiz)):
    for j in range(5):
        if arr[i][j] == 'S':
            BFS(i, j)

print(res)
