import sys
from collections import deque
sys.stdin = open("../input.txt", "rt")

g = [list(map(int, input().split())) for _ in range(7)]
dis = [[0] * 7 for _ in range(7)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
dq = deque()
g[0][0] = 1
dq.append((0,0))

while dq:
    tmp = dq.popleft()
    for i in range(4):
        xx = tmp[0] + dx[i]
        yy = tmp[1] + dy[i]
        if 0 <= xx < 7 and 0 <= yy < 7 and g[xx][yy] == 0:
            g[xx][yy] = 1
            dis[xx][yy] = dis[tmp[0]][tmp[1]] + 1
            dq.append((xx, yy))

for i in range(7):
    for j in range(7):
        print(dis[i][j], end = '\t')
    print()








