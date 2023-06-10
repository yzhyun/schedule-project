import sys
sys.stdin = open("../input.txt", "rt")

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
ch = [[0]*n for _ in range(n)]
maxVal = -2147000000
minVal = 2147000000
sx = sy = ex = ey = -1

for i in range(n):
    for j in range(n):
        if maxVal < board[i][j]:
            maxVal = board[i][j]
            ex = i
            ey = j
        if minVal > board[i][j]:
            minVal = board[i][j]
            sx = i
            sy = j

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = 0
def DFS(x, y):
    global cnt
    if x == ex and y == ey:
        print(x, y)
        cnt += 1
    else:
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if (0 <= xx < n) and (0 <= yy < n) and (ch[xx][yy] == 0) and (board[x][y] < board[xx][yy]):
                ch[xx][yy] = 1
                DFS(xx, yy)
                ch[xx][yy] = 0

ch[sx][sy] = 1
DFS(sx, sy)
print(cnt)
