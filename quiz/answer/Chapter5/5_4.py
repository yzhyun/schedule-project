import sys
sys.stdin=open("../input.txt", "rt")

s=input()
print(s)
stack=[]

for x in s:
    if x.isdecimal():
        stack.append(int(x))
    if x == '+':
        n1 = stack.pop()
        n2 = stack.pop()
        stack.append(n2 + n1)
    elif x == '-':
        n1 = stack.pop()
        n2 = stack.pop()
        stack.append(n2 - n1)
    elif x == '*':
        n1 = stack.pop()
        n2 = stack.pop()
        stack.append(n2 * n1)
    elif x == '/':
        n1 = stack.pop()
        n2 = stack.pop()
        stack.append(n2 / n1)

print(stack[0])