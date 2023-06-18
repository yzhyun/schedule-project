import sys
from collections import deque
sys.stdin = open("../input.txt", "rt")

dq = deque()
n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]
ch = [[0]*n for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
sum = 0

ch[n//2][n//2] = 1
sum += g[n//2][n//2]
dq.append((n//2, n//2))
L = 0
while deque:
    if L == n//2:
        break
    else:
        size = len(dq)
        for i in range(size):
            tmp = dq.popleft()
            for j in range(4):
                xx = tmp[0]+dx[j]
                yy = tmp[1]+dy[j]
                if ch[xx][yy] == 0:
                    sum += g[xx][yy]
                    ch[xx][yy] = 1
                    dq.append((xx, yy))
        print(size)
        for x in ch:
            print(x)
        L+=1
print(sum)



