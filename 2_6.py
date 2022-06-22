import sys
sys.stdin = open("input.txt", "rt")


def digit_sum(x):
    sx=str(x)
    sum=0

    for i in range(0,len(sx)):
        sum += int(sx[i])
    return sum

##print(digit_sum(input()))

n=int(input())
ln=list(map(int,input().split()))
lres=list[n] 
##print(ln)
temp=0
nRslt=0
for i, x in enumerate(ln) :
    
    rSum=digit_sum(x)
    if(rSum > temp) :
        temp=rSum
        nRslt=x

print(nRslt)
