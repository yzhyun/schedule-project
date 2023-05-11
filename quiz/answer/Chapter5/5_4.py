import sys
sys.stdin=open("../input.txt", "rt")

s=input()
print(s)
stack=[]

nRslt=0
for x in s:
    if x.isdecimal():
        stack.append(x)
    else :
        if x=='+':
            j = int(stack.pop())
            k = int(stack.pop())
            stack.append(j+k)
        elif x=='-':
            j = int(stack.pop())
            k = int(stack.pop())
            stack.append(k-j)
        elif x=='*':
            j = int(stack.pop())
            k = int(stack.pop())
            stack.append(j*k)
        elif x=='/':
            j = int(stack.pop())
            k = int(stack.pop())
            stack.append(j//k)

print(stack.pop())