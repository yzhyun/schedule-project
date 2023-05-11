import sys
sys.stdin=open("../input.txt", "rt")

s=input()
print(s)

stack=[]
res=""
for x in s:
    # 숫자인지 판단
    if x.isdecimal() :
        res+=x
    else :
        if x=='(':
            stack.append(x)
        elif x==')':
            while stack and stack[-1]!='(':
                res+=stack.pop()
            stack.pop()
        elif x=='*' or x=='/':
            if stack and (stack[-1]=='*' or stack[-1]=='/'):
                res+=stack.pop()
            stack.append(x)
        elif x=='+' or x=='-':
            while stack and stack[-1]!='(':
                res+=stack.pop()
            stack.append(x)


while stack :
    res+=stack.pop()



    # '('인 경우 무조건 stack
    # ')'인 경우 '(' 뒤 쪽 모두 처리
print(res)