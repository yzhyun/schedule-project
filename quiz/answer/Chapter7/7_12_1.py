import sys
sys.stdin = open("../input.txt", "rt")

n = int(input())
g = [list(map(int, input())) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0 , 1, 0, -1]

def DFS(x, y):
    global cnt
    cnt += 1
    g[x][y] = 0
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < n and 0 <= yy < n and g[xx][yy] == 1:
            DFS(xx, yy)

res = list()
for i in range(n):
    for j in range(n):
        if g[i][j] == 1:
            cnt = 0
            DFS(i, j)
            res.append(cnt)

print(len(res))
res.sort()
for x in res:
    print(x)

# for i in range(n):
#     for j in range(n):
#         print(g[i][j], end = '\t')
#     print()