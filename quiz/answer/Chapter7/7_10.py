import sys
sys.stdin = open("../input.txt", "rt")

g = [list(map(int, input().split())) for _ in range(7)]
g[0][0] = 1
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
cnt = 0
# for i in range(7):
#     for j in range(7):
#         print(g[i][j] , end = ' ')
#     print()


def DFS(x, y):
    global cnt
    if x == 6 and y == 6:
        cnt+=1
    else:
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx <= 6 and 0 <= yy <= 6 and g[xx][yy] == 0:
                g[xx][yy] = 1
                DFS(xx, yy)
                g[xx][yy] = 0




DFS(0, 0)
print(cnt)
