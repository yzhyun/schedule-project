import sys
sys.stdin = open("../input.txt", "rt")

n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]
lrslt = list()
print(g)
# 행의 합
# 열의 합
# 대각선의 합
maxVal = -2147000000
for i in range(n):
    sum1 = sum2 = 0
    for j in range(n):
        sum1 += g[i][j]
        sum2 += g[j][i]
    if sum1 > maxVal:
        maxVal = sum1
    if sum2 > maxVal:
        maxVal = sum2

sum1 = sum2 = 0
for i in range(n):
    sum1 += g[i][i]
    sum2 += g[i][n-i-1]
if sum1 > maxVal:
    maxVal = sum1
if sum2 > maxVal:
    maxVal = sum2

print(maxVal)