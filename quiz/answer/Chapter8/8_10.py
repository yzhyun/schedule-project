import sys
sys.stdin = open("../input.txt", "rt")

n = int(input())
c = list(map(int, input().split()))
m = int(input())

dy = [1000] * (m+1)
dy[0] = 0

for i in range(n):
    for j in range(c[i], m+1):
        dy[j] = min(dy[j-c[i]]+1, dy[j])
print(dy)