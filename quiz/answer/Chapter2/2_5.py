import sys
sys.stdin=open("../input.txt", "rt")

n, k=map(int,input().split())
print(n,k)
ln=list(map(int, range(1,n+1)))
lk=list(map(int, range(1,k+1)))
print(ln)
print(lk)


lrslt=list(0 for i in range(n+k+1))
print(lrslt)
maxVal=0

for i in range(1,n+1):
    for j in range(1,k+1):
        lrslt[i+j]=lrslt[i+j]+1

maxVal=max(lrslt)

print("정답:", end= ' ')
for i in range(len(lrslt)):
    if(maxVal==lrslt[i]):
        print(i, end=' ')