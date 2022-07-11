import sys
sys.stdin=open("input.txt","rt")

n=int(input())
arr=[list(map(int, input().split())) for _ in range (n)]

'''
print("================================================")
print(n)

for i in arr:
    for j in i:
        print(j, end = ' ')
    print()
print("================================================")
'''
rSum=-2147000000
for i in range(n):
    sum1=sum2=0
    for j in range(n):
        sum1+=arr[i][j]
        sum2+=arr[j][i]
    if(sum1>rSum):
        rSum=sum1
    if(sum2>rSum):
        rSum=sum2

sum1=sum2=0
for i in range(n):
    sum1+=arr[i][i]
    sum2+=arr[i][n-i-1]
if(sum1>rSum):
    rSum=sum1
if(sum2>rSum):
    rSum=sum2
print(rSum)

