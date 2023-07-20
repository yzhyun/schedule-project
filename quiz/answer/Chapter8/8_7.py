import sys
sys.stdin = open("../input.txt", "rt")

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]

dp[0][0] = arr[0][0]
# 첫 행과 첫 열에 대한 초기값 셋팅
for i in range(1, n):
    dp[0][i] = dp[0][i-1] + arr[0][i]
    dp[i][0] = dp[i - 1][0] + arr[i][0]

dx = [-1, 0]
dy = [0, -1]

print(dp[1+dx[0]][1])

for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = min( dp[i+dx[0]][j], dp[i][j+dy[1]]) + arr[i][j]

for x in dp:
    print(x)

print(f"result ==> {dp[n-1][n-1]}")
