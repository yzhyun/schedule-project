import sys
sys.stdin=open("input.txt", "rt")

n=int(input())

lScore=list(map(int, input().split()))

lSum=[0 for i in range(n)]

for i in range(n):
    if(0==i):
        if(1==lScore[i]):
            lSum[i]=1
        else:
            lSum[i]=0
    else:
        if(1==lScore[i]):
            if(0<lSum[i-1]):
                lSum[i]=lSum[i-1]+1
            else:
                lSum[i]=lScore[i]
        else:
            lSum[i]=0


print(sum(lSum))    

lsum=[0 for i in range (n)]
    
    