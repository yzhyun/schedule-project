import sys

sys.stdin = open("../input.txt", "rt")

n, m  = map(int, input().split())

dp = [0] * (m + 1)
dp[0] = 0

for i in range(n):
    s, t = map(int, input().split())
    for j in range(m, t-1, -1):
        dp[j] = max(dp[j - t] + s, dp[j])

print(dp[m])


