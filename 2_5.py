import sys
sys.stdin=open("input.txt", "rt")

n,m=map(int, input().split())
#lcon=list(map(int, range(n+m)))
ln=list(map(int, range(1, n+1)))
lm=list(map(int, range(1, m+1)))
lcon=list(0 for i in range(n+m))


for i in range(1,n+1):
    for j in range(1,m+1):

        lcon[(i+j)-1]+=1

print(lcon)
##print(lcon.index(max(lcon)))
##print(lcon.count(max(lcon)))

lrslt=[0]*(lcon.count(max(lcon)))

for i in range(lcon.count(max(lcon))):
    lrslt[i]=lcon.index(max(lcon))+1
    lcon[lcon.index(max(lcon))]=0
rslt=""
for j in lrslt:
    rslt+=str(j) + " "
print(rslt)

