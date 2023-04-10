import sys
sys.stdin=open("input.txt", "rt")

sQuiz=input()
print(sQuiz)
sRslt=""
nRslt=0
for i,val in enumerate(sQuiz):
    if(ord(val) >= 48 and ord(val) <=57):
        sRslt+=val
nRslt=int(sRslt)
cnt=0
for i in range(1,nRslt+1):
    if((nRslt%i)==0):
        print(i)
        cnt+=1



#answer
print(nRslt)
print(cnt)
