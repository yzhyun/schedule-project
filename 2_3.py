import sys
sys.stdin=open("input.txt", "rt")

n,k=map(int, input().split())
a=list(map(int,input().split()))

res=set()

for i in range(0,n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            res.add(a[i]+a[j]+a[m])

res=list(res)
res.sort(reverse=True)

print(res[k])

'''
a.sort(reverse=True)
print(n,k)
print(a)

rslt=0
cnt=0
for i in range(0, k-1):
    rslt+=a[i]
    cnt+=1
a=a[cnt:len(a)]

print(a)
print(rslt)

rslt=rslt+a[k-1]
print(rslt)
'''