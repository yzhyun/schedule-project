# import sys
# sys.stdin = open("../input.txt", "rt")
#
# n = int(input())
# bricks = []
# dp = [0] * n
# for i in range(n):
#     a, b, c = map(int, input().split())
#     bricks.append((a, b, c))
# print(bricks)
# bricks.sort(key = lambda x: (-x[0], -x[1], -x[2]))
#
# dp[0] = bricks[0][1]
#
# for i in range(1, n):
#     maxVal = 0
#     for j in range(i-1, -1, -1):
#         if bricks[j][2] > bricks[i][2] and dp[j] > maxVal:
#             maxVal = dp[j]
#     dp[i] = maxVal + bricks[i][1]
#
# print(dp)

import sys
sys.stdin = open("../input.txt", "rt")

n = int(input())
bricks = []

for i in range(n):
    a, b, c = map(int, input().split())
    bricks.append((a, b, c))

bricks.sort(key=lambda x: (-x[0], -x[1]))  # 넓이 기준 내림차순 정렬
#bricks.sort(reverse = True)
dp = [0] * n
dp[0] = bricks[0][1]

for i in range(1, n):
    maxVal = 0
    for j in range(i-1, -1, -1):
        if bricks[i][2] < bricks[j][2] and maxVal < dp[j]:
        #if bricks[j][2] > bricks[i][2] and dp[j] > maxVal:
            maxVal = dp[j]
    dp[i] = maxVal + bricks[i][1]

print(dp)
print(max(dp))

