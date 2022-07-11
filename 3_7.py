import sys
sys.stdin=open("input.txt", "rt")

n=int(input())
arr=[list(map(int, input().split())) for _ in range(n)]

print("================================================")
print(n)
for i in arr :
    for j in i:
        print(j, end=' ')
    print()
print("================================================")

res=0
s=e=n//2

for i in range(n):
    for j in range(s, e+1):
        res+=arr[i][j]
    if(i<n//2):
        s-=1
        e+=1
    else:
        s+=1
        e-=1

print(res)






