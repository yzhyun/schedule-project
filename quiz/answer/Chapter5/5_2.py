import sys

sys.stdin = open("../input.txt", "rt")
s = input()

stack = []
sum = 0
for i in range(len(s)):
    if s[i] == '(':
        stack.append('(')
    else:
        if s[i-1] == '(':
            stack.pop()
            sum += len(stack)
        else:
            stack.pop()
            sum += 1
    #print(stack)
print(sum)


