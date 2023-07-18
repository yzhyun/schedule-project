import sys
import itertools as it
sys.stdin=open("../input.txt", "r")

n, m, k = map(int, input().split())
ln = list(map(int, input().split()))

case = it.permutations(ln, n)

minVal = sys.maxsize
for aa in case:
    work = 0
    bucket = 0
    sumVal = 0
    i = 0
    lx = list(aa)
    while work != k:
        if bucket + lx[i] <= m:
            bucket += lx[i]
            lx.append(lx[i])
            i += 1
        else:
            sumVal += bucket
            bucket = 0
            work += 1

    minVal = min(minVal, sumVal)
print(minVal)
