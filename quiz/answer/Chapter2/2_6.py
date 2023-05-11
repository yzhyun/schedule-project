import sys
sys.stdin=open("../input.txt", "rt")

n=int(input())
lq=list(map(str, input().split()))
lrslt=[0]*n

print(n)
print(lq)
rslt=0

def sumString(trgtStr):
    tmpRslt=0
    for j in range(len(trgtStr)):
        tmpRslt+=int(trgtStr[j])
    return tmpRslt

for i in range(len(lq)):
    sTmp=lq[i]
    rslt = sumString(sTmp)
    lrslt[i] = rslt
    rslt=0

maxVal=max(lrslt)

for i in range(len(lrslt)):
    if(maxVal==lrslt[i]):
        print("result:", lq[i])
        break


