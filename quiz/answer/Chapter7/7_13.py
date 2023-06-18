import sys
from collections import deque
sys.stdin = open("../input.txt", "rt")

n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]
dq = deque()
dx = [-1, -1, 0, 1, 1,  1,  0, -1]
dy = [ 0,  1, 1, 1, 0, -1, -1, -1]
cnt = 0

for i in range(n):
    for j in range(n):
        if g[i][j] == 1:
            cnt += 1
            g[i][j] = 0
            dq.append((i, j))
            while dq:
                tmp = dq.popleft()
                for k in range(8):
                    x = tmp[0] + dx[k]
                    y = tmp[1] + dy[k]
                    if 0<=x<n and 0<=y<n and g[x][y] == 1:
                        dq.append((x, y))
                        g[x][y] = 0
print(cnt)


