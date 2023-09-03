import sys
sys.stdin = open("input.txt", "rt")

n, k = map(int, input().split())
ln = [int(input()) for _ in range(n)]

cnt = 0
for i in range(n-1, -1, -1):
    if k >= ln[i]:
        cnt += k // ln[i]
        k = k % ln[i]

print(cnt)