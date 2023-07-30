import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

n = int(input())
ln = list(map(int, input().split()))

ln.sort()
dy = [0] * n
dy[0] = ln[0]

print(ln)
print(dy)

for i in range(1, n):
    dy[i] = ln[i] + dy[i-1]

print(sum(dy))