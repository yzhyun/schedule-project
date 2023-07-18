import sys
from collections import deque

sys.stdin = open("../input.txt", "rt")

n = int(input())
ln = list(map(int, input().split()))


dp = [1]*n

for i in range(n):
    for j in range(0, i):

        if ln[i] > ln[j]: # 만약 이전 돌보다 현재 돌이 높다면
            # 건널 수 있음. dp값 업데이트!
            dp[i] = max(dp[i], dp[j]+1)

print(dp)
