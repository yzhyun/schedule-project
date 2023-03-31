import sys,os

#print(os.getcwd());
sys.stdin = open("./../input.txt", "rt")

n=int(input())
la=list(map(int, input().split()))
avg=round(sum(la)/n)
print(n)
print(la)
print(avg)
minVal=la[0]
idx=0
res=0


for i in range(len(la)-1, -1,-1):
    print(i)
    tmp=abs(la[i] - avg)
    print( "차이값", tmp )
    if(minVal >= tmp):
        minVal=tmp
        res=la[i]
        idx=i


print(avg, idx)


