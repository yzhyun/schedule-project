import sys
sys.stdin = open("../input.txt")

n = int(input())

dp = [0] * (n+1)
dp[1] = 1
dp[2] = 2
dp[3] = 3

for i in range(4, n+1):
    dp[i] = dp[i-2] + dp[i-1]
print(dp[n])
