import sys
sys.stdin = open("input.txt", "rt")

n = int(input())
a = list(input())
print(a)

for i in range(n-1):
    b = input()
    for j in range(len(a)):
        if a[j] != b[j]:
            a[j] = '?'

print(''.join(a))


