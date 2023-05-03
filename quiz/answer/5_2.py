import sys

sys.stdin = open("input.txt", "rt")

ln = list(map(str, str(input())))
print(''.join(map(str, ln)))

stack = []
sum = 0

for i in range (len(ln)):
    if ln[i] == '(':
        stack.append('(')
    else :
        stack.pop()
        if ln[i-1] == '(':
            sum+=len(stack)
        else :
            sum+=1

print(sum)
