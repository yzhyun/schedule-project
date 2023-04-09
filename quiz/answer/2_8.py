import sys
sys.stdin=open("input.txt", "rt")

n=int(input())
ln=list(map(int,input().split()))
print(n)
print(ln)

def reverse(x):
    sRevs=str(x)[::-1]
    nRtn=int(sRevs)
    return nRtn

def isPrime(x):
    bRtn=True
    if(x==1):   return False
    for i in range (2,x):
        if(x%i == 0):
            return False
    return bRtn

for idx, val in enumerate(ln):
    nRtn=reverse(val)
    if(isPrime(nRtn)):
        print(nRtn, end=' ')