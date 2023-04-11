import sys

sys.stdin = open("input.txt", "rt")

n = int(input())
ln = [list(map(int, input().split())) for i in range(n)]

print(n)
print(ln)

val = 0
# tmp = 0
sum1 = 0
sum2 = 0
for i in range(n):
    sum1 = sum2 = 0
    for j in range(n):
        sum1 += ln[i][j]
        sum2 += ln[j][i]
    if sum1 > val:
        val = sum1
    if sum2 > val:
        val = sum2

sum1 = 0
sum2 = 0
for i in range(n):
    sum1 += ln[i][i]
    sum2 += ln[i][n - i - 1]

if val < sum1:
    val = sum1
if val < sum2:
    val = sum2
print(val)
