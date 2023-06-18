import sys
sys.stdin = open("../input.txt", "rt")

n, k = map(int, input().split())

ln = list()

for i in range(1, n+1):
    if n % i == 0:
        ln.append(i)

if len(ln) < k :
    print(-1)
else:
    print(ln[k-1])