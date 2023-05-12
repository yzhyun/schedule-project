import sys
sys.stdin = open("../input.txt", "rt")
n = int(input())
print(n)

p=dict()

for _ in range(n):
    p[input()] = 1

for _ in range(n-1):
    p[input()] = 0

for key, val in p.items():
    if val == 1:
        print(key)
