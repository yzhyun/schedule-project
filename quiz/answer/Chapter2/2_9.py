import sys

sys.stdin = open("../input.txt", "rt")

n = int(input())
ln = list()
lRslt = [0 for i in range(n)]

print(lRslt)


def caseTriple(x):
    sVal = 10000 + (x * 1000)
    return sVal


def caseDouble(x):
    sVal = 1000 + (x * 100)
    return sVal


def caseSingle(x):
    sVal = x * 100
    return sVal


for i in range(n):
    a,b,c = map(int, input().split())
    print(a, b, c)
    if(a==b and b==c):
        ln.append(caseTriple(a))
    elif(a==b or b==c) :
        ln.append(caseDouble(b))
    elif(a==c) :
        ln.append(caseDouble(a))
    else :
        ln.append(caseSingle(max(a,b,c)))

print(max(ln))

