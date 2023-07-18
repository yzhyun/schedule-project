import sys
sys.stdin = open("../input.txt")

n = int(input())
ln = [0] + list(map(int, input().split()))

dp = [0] * (n+1)
dp[1] = 1

for i in range(2, n+1):
    mmax = 0
    for j in range(i-1, 0, -1):
        if ln[j] < ln[i] and dp[j] > mmax:
            mmax = dp[j]
    dp[i] = mmax + 1
print(max(dp))

