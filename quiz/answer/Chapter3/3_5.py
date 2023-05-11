import sys
sys.stdin=open("../input.txt", "rt")

m,n=map(int,input().split())
ln=list(map(int, input().split()))

print(m,n)
print(ln)

lt=0
rt=1
tot=ln[0]
cnt=0
while True:
    if(tot<n):
        if(rt>=m):   break
        else:
            tot+=ln[rt]
            rt+=1
    elif(tot==n):
        tot-=ln[lt]
        lt+=1
        cnt+=1
    elif(tot>n):
        tot-=ln[lt]
        lt+=1

print(cnt)