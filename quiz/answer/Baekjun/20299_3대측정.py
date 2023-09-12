import sys
input=sys.stdin.readline
n, k, l = map(int, input().split())
lrslt = []
for _ in range(n):
    lteam = list(map(int, input().split()))
    if sum(lteam) >= k:
        if all(x >= l for x in lteam):
            lrslt.append(lteam)

print(len(lrslt))
for lt in lrslt:
    for i in range(3):
        print(lt[i], end = ' ')
        