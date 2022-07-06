import sys
sys.stdin=open("input.txt", "rt")

sInput=input()
print(sInput)

sRslt=""
nRslt=0
nAns=0
for i in range(0, len(sInput)):
    if(48 <= ord(sInput[i]) and ord(sInput[i]) <= 57):
#        print(sInput[i])
        sRslt+=(sInput[i])


nRslt=int(sRslt)
print(nRslt)

for i in range(1,nRslt+1):
    if(nRslt%i==0):
        #print(i)
        nAns+=1

print(nAns)









