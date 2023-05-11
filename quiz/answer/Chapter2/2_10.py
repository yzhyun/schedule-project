import sys
sys.stdin=open("../input.txt", "rt")

n=int(input())
ln=list(map(int, input().split()))

print(n)
print(ln)
print("======================================================")

lp=list(0 for i in range(n))
cnt=0
print(lp)

for idx, val in enumerate(ln):
    if(val==1 and cnt==0):
        lp[idx]=1
        cnt += 1
    elif(val==1 and cnt!=0):
        cnt+=1
        lp[idx]=val*cnt
    elif(val==0):
        cnt=0

print(lp)
print(sum(lp))