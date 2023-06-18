import sys
from collections import deque
sys.stdin=open("../input.txt", "rt")

n = int(input())
g  = [list(map(int, input().split())) for _ in range(n)]
ch = [[0]*n for _ in range(n)]

# sum = 0
# s = e = n // 2
# for i in range(n):
#     for j in range(s, e+1):
#         print(i, j)
#         sum += g[i][j]
#     if i < n // 2:
#         s -= 1
#         e += 1
#     else:
#         s += 1
#         e -= 1
# print(sum)


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

dq = deque()
dq.append((n//2, n//2))
sum = g[n//2][n//2]
ch[n//2][n//2] = 1
L=0

while dq:
    x, y = dq.popleft()
    if x == 0 or x == (n // 2) * 2 or y == 0 or y == (n // 2) * 2:
        break
    for i in range(4):
        xx = dx[i] + x
        yy = dy[i] + y
        if ch[xx][yy] == 0:
            ch[xx][yy] = 1
            dq.append((xx, yy))
            sum += g[xx][yy]
print(ch)
print(sum)



