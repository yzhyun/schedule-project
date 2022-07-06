'''
import sys
sys.stdin=open("input.txt", "rt")

n1=int(input())
l1=list(map(int, input().split()))
n2=int(input())
l2=list(map(int, input().split()))
l3=[0 for i in range(n1+n2)]
print(l1)
print(l2)
print(l3)
cnt=0

for i in range(n1):
    l3[i]=l1[i]
    cnt+=1
for j in range(n2):
    l3[cnt]=l2[j]
    cnt+=1

l3.sort()

for i in l3:
    print(i, end=' ')
'''

import sys
sys.stdin=open("input.txt", "rt")

n1=int(input())
l1=list(map(int, input().split()))

n2=int(input())
l2=list(map(int, input().split()))

print("========================")
print(n1, l1)
print(n2, l2)
print("========================")

l3=[]
p1=p2=0

while(p1<n1 and p2<n2):

    if(l1[i]<=l2[i]):
        l3.append(l1[i])
        l3.append(l2[i])
        p1+=1
    else:
        l3.append(l2[i])
        l3.append(l1[i])
        p2+=1

print(l3)

