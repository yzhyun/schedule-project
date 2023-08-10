import sys
sys.stdin = open("input.txt", "rt")

n = int(input())
lx = [int(input()) for _ in range(n)]

for i in range(n-1):
    for j in range(n-1-i):
        if lx[j] > lx[j+1]:
            temp = lx[j+1]
            lx[j+1] = lx[j]
            lx[j] = temp

print(lx)

