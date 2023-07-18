import sys
sys.stdin=open("../input.txt", "rt")

s=input()
print(s)

stack = []
res = ""
for x in s:
    if x.isdecimal():
        res += x
    if x == '*' or x == '/':
        while stack and (stack[-1] == '*' or stack[-1] == '/'):
            res += stack.pop()
        stack.append(x)
    elif x == '+' or x == '-':
        while stack and stack[-1] != '(':
            res += stack.pop()
        stack.append(x)
    elif x == '(':
        stack.append(x)
    elif x == ')':
        while stack and stack[-1] != '(':
            res += stack.pop()
        stack.pop()

print(res)