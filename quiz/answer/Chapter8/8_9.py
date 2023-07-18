import sys
sys.stdin = open("../input.txt", "rt")

n = int(input())
coin = list(map(int, input().split()))
m = int(input())
dp = [1000] * (m + 1)
dp[0] = 0

for i in range(n):
    for j in range(coin[i], m+1):
        dp[j] = min(dp[j-coin[i]]+1, dp[j])

print(dp)
print(dp[m])


