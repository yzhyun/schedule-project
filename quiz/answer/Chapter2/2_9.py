import sys
sys.stdin = open("../input.txt", "rt")

n = int(input())
lrslt = list()

for i in range(n):
    a, b, c = map(int, input().split())

    if a == b == c:
        res = a*1000+10000
    elif a != b != c:
        maxVal = -217000000
        if a > maxVal:
            maxVal = a
        if b > maxVal:
            maxVal = b
        if b > maxVal:
            maxVal = c
        res = c*100
    else:
        if a == b and a != c:
            res = a * 100 + 1000
        if a == c and a != b:
            res = a * 100 + 1000
        if b == c and b != a:
            res = b * 100 + 1000
    lrslt.append(res)
print(lrslt)
print(max(lrslt))
