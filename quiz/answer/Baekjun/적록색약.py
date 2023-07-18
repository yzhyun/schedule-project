import sys
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(10**6)

n = int(input())
arr = [list(input()) for _ in range(n)]
ch  = [[0] * n for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def DFS(x, y, color):
    ch[x][y] = 1
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0 <= nx < n and 0 <= ny < n and ch[nx][ny] == 0:
            if arr[nx][ny] == color:
                DFS(nx, ny, color)

cnt = 0
for i in range(n):
    for j in range(n):
        if ch[i][j] == 0:
            DFS(i, j, arr[i][j])
            cnt += 1
cnt2 = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == 'G':
            arr[i][j] = 'R'

ch  = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if ch[i][j] == 0:
            DFS(i, j, arr[i][j])
            cnt2 += 1

print(cnt, cnt2)