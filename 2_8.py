import sys
sys.stdin=open("input.txt", "rt")

n=input()
ln=list(map(int, input().split()))

print("갯수: ",n, " / 리스트: ", ln)


def reverse(x):
#    print("입력숫자: ", x)
    rtnVal=str(x)[::-1]
    rtnVal=int(rtnVal)
#    print(rtnVal)
    return rtnVal
    
def isPrime(x):
    for i in range(2,x):
        
        if (x%i)==0 :
            print(x ,i, x%i)
            return False        


    return True

lrtn=[]
for i, x in enumerate(ln):
    val=reverse(x)   
    if(isPrime(val)):
        lrtn.append(val)

print(lrtn)