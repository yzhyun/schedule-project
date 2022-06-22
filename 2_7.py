import sys
sys.stdin=open("input.txt" , "rt")

N=int(input())

rsltCnt=0
cnt=0

for i in range(1,N+1):
    print(i)
    for j in range(1,i+1):
        print("i==>", i ,"j==>" ,j, "==>" ,i%j)                     
        if(i%j)==0:
            cnt+=1       
    if(cnt==2):
        rsltCnt+=1
    
    
    cnt=0
print(rsltCnt)


