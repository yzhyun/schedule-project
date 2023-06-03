import sys
sys.stdin = open("../input.txt", "rt")

n, m = map(int, input().split())

res = [[0] * (n+1) for _ in range(n+1)]

for _ in range (m):
    a, b, c = map(int, input().split())
    res[a][b] = c

for i in range(1, n+1):
    for j in range(1, n+1):
        print(res[i][j], end = ' ')
    print()