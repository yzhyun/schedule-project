import sys
sys.stdin = open("../input.txt", "rt")

n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]


k = int(input())

for _ in range(k):
    row, way, num = map(int, input().split())
    row = row - 1
    print(row, way, num)
    for i in range(num):
        if way == 0:    #왼쪽
            g[row].append(g[row].pop(0))
        elif way == 1:  #오른쪽
            g[row].insert(0, g[row].pop())

for i in range(n):
    for j in range(n):
        print(g[i][j] , end = ' ')
    print()

sum = 0
s = 0
e = n-1
for i in range(n):
    print(s, e)
    for j in range(s, e+1):
        sum += g[i][j]
    if i < n//2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1

print(sum)
