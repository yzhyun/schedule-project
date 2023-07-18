import sys
sys.stdin = open("../input.txt", "rt")

num, n = map(int, input().split())
num = list(map(int, str(num)))
print(num)

stack = []
for x in num:
    while stack and n > 0 and stack[-1] < x:
        stack.pop()
        n -= 1
    stack.append(x)

if n != 0:
    stack = stack[:-n]

res = ''.join(map(str, stack))
print(res)



