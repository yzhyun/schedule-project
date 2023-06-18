import sys
sys.stdin = open("../input.txt", "rt")

n, k = map(int, input().split())
ln = list(map(int, input().split()))
a = set()
b = list()

for i in range(n):
    for j in range(n):
        for m in range(n):
            a.add(ln[i]+ln[j]+ln[m])
b = list(a)
b.sort(reverse=True)
print(b[k-1])
