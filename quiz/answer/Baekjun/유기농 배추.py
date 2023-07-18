import sys
from collections import deque
sys.stdin = open("../input.txt", "rt")
n = int(input())

def BFS(a, b):
    dq.append((a, b))
    arr[a][b] = 0
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            xx = dx[i] + x
            yy = dy[i] + y

            if 0 <= xx < row and 0 <= yy < col and arr[xx][yy] == 1:

                arr[xx][yy] = 0
                dq.append((xx, yy))


for _ in range(n):
    col, row, k = map(int, input().split())
    #print(f"col{col} row{row} k{k}")

    arr = [[0] * col for _ in range(row)]

    for i in range(k):
        a, b = map(int, input().split())
        arr[b][a] = 1
    dq = deque()
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]


    cnt = 0
    for i in range(row):
        for j in range(col):
            if arr[i][j] == 1:
                BFS(i, j)
                cnt+=1

    print(cnt)
