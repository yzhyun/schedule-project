import sys
sys.stdin = open("../input.txt", "rt")
n = int(input())
print(n)

p = dict()

for i in range(n):
    p[input()] = 1

for i in range(n-1):
    p[input()] = 0

for x in p:
    print(i)
    if p[x] == 1:
        print(x)

for key, val in p.items():
    print(key, val)

p = dict(sorted(p.items(), reverse=True))

for key, val in p.items():
    print(key, val)

