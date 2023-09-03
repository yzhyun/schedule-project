import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

exp = input().split('-') #식: expression
print(exp)
ans = 0
for i in exp[0].split('+'):
    print(i)
    ans += int(i)
for i in exp[1:]:
    for j in i.split('+'):
        ans -= int(j)

print(ans)