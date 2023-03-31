import sys
sys.stdin = open("input.txt", "rt")

N, K = map(int, input().split())

print("%d %d" %(N,K))
la = list()

for i in range(1,N+1) :

    a = int(N%i)
    if  a==0 :
        la.append(i)

la.sort()

if len(la) < K :
    nRslt = -1
else :
    nRslt = la[K-1]

print(nRslt)