import sys
sys.stdin=open("../input.txt", "rt")
n=int(input())
print(n)
lrslt=list(map(int, range(1,n+1)))
lb=[True]*(n+1)
nRslt=0



print("======================")


for idx, bVal in enumerate(lb):
    if(idx<2):
        lb[idx]=False
        continue
    if(bVal):
        for j in range(idx, (n//idx)+1):
            lb[idx*j]=False

print([i for i, val in enumerate(lb) if val])

lval=list(i for i, val in enumerate(lb) if val)
print(len(lval))