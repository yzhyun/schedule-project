import sys
sys.stdin=open("../input.txt", "rt")

m, n=map(int,input().split())
a = list(map(int, input().split()))

cnt = s = e = 0
#print(a[s:e+1])

while s < m and e < m:
    if sum(a[s:e+1]) == n:
        s += 1
        e += 1
        cnt += 1
    elif sum(a[s:e+1]) < n:
        e += 1
    elif sum(a[s:e+1]) > n:
        s += 1

print(cnt)
