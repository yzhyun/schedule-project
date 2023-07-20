import sys
sys.stdin = open("../input.txt")

n = int(input())
arr = [i for i in range(n+1)]
dy = [0] * (n+1)

dy[0] = 0
dy[1] = 1
dy[2] = 2

for i in range(3, n+1):
    dy[i] = dy[i-2] + dy[i-1]

print(dy[n])
