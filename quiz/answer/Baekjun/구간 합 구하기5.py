import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

n, m = map(int, input().split())
a = [0] * (n+1)
ln = [[0] + list(map(int, input().split())) for _ in range(n)]
ln.insert(0, a)
dy = [[0] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        dy[1][j] = dy[1][j-1] + ln[1][j]
        dy[i][1] = dy[i-1][1] + ln[i][1]

for i in range(2, n+1):
    for j in range(2, n+1):
        dy[i][j] = dy[i-1][j] + dy[i][j-1] - dy[i-1][j-1] + ln[i][j]

# for x in dy:
#     for i in x:
#         print(i, end = '\t')
#     print()


for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())

    print(dy[x2][y2] - dy[x1-1][y2]-dy[x2][y1-1]+dy[x1-1][y1-1])

# for x in ln:
#     print(x)
#
#




