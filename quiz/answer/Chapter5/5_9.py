import sys
sys.stdin = open("../input.txt", "rt")

a = input()
b = input()

p = dict()

for i in a:
    p[i] = p.get(i, 0) + 1

for i in b:
    p[i] = p.get(i, 0) - 1

if all( p[i] == 0 for i in p.keys()):
    print("YES")
else:
    print("NO")