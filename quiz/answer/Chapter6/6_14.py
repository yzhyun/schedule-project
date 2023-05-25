import sys

sys.stdin = open("../input.txt", "rt")

n, m = map(int, input().split())
a = [[0] * (n + 1) for i in range(n + 1)]

for i in range(m):
    h, y, g = map(int, input().split())
    a[h][y] = g

for i in range(n+1):
    for j in range(n+1):
        print(a[i][j], end=' ')
    print()
