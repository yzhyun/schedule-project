import sys
sys.stdin = open("input.txt", "rt")

n, m = map(int, input().split())
print (n, m)

ln = list(map(int, str(n)))
print(ln)
stack=[]

for x in ln:
    while stack and m>0 and stack[-1]<x:
        stack.pop()
        m-=1
    stack.append(x)

stack=stack[:-m]
res=''.join(map(str, stack))
print(m, res)

