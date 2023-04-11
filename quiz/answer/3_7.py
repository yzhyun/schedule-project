import sys
sys.stdin=open("input.txt", "rt")

n=int(input())
ln=[list(map(int, input().split())) for _ in range (n)]
s=e=n//2
print(n)
print(ln)
nRslt=0
for i in range(n):
    for j in range(s, e+1):
        print(i,j)
        nRslt += ln[i][j]
    if i < n//2:
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1
print(nRslt)
