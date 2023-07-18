import sys
sys.stdin=open("../input.txt", "rt")

x = int(input())
lx = list(map(int, input().split()))
n = int(input())

lx.sort()
print(lx)

for i in range(n):
    lx[0] += 1
    lx[x-1] -=1
    lx.sort()
print(max(lx)-min(lx))