import sys,os

print(os.getcwd())
sys.stdin = open("../input.txt", "rt")

n=int(input())
la=list(map(int, input().split()))
avg=round(sum(la)/n)
print(n)
print(la)
print(avg)

diff=0
tmp=1000
resVal=-1000
resIdx=-1
for idx, val in enumerate(la):
    diff=abs(avg-val)
    if(diff<tmp):
        tmp=diff
        resVal=val
        resIdx=idx
    elif(diff==tmp):
        if(resVal<val):
            resVal=val
            resIdx=idx
        elif(resVal==val):
            if(idx<resIdx):
                resVal=val
                resIdx=idx


print(avg, resIdx+1)

