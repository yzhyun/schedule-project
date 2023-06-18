import sys
sys.stdin=open("../input.txt", "rt")

n, m = map(int, input().split())
res = [0 for i in range(0, n+m+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        res[i+j] = res[i+j]+1

for idx, val in enumerate(res):
    if val == max(res):
        print(idx, end=' ')
