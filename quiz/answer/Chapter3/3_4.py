import sys
sys.stdin = open("../input.txt", "rt")

n = int(input())
ln = list(map(int, input().split()))

m = int(input())
lm = list(map(int, input().split()))

a = ln + lm
a.sort()

print(a)