import sys
sys.stdin = open("input.txt", "rt")

n = int(input())
ln = list(map(int, input()))
sum = 0
for i in range(n):
    sum += ln[i]

print(sum)