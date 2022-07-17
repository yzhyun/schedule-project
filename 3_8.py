import sys
sys.stdin=open("input.txt", "rt")

n=int(input())
ln=[list(map(int, input().split())) for _ in range(n)]
m=int(input())
lm=[list(map(int, input().split())) for _ in range(m)]
resLm=[[0]*n for _ in range(n)]

def sorting_l(la, num):
    #print("sorting_l", la, num)
    for i in range(num):
        tmp = la[0]
        for j in range(n-1):
            la[j]=la[j+1]
        la[n-1]=tmp

def sorting_r(la, num):
    #print("sorting_r", la, num)
    for i in range(num):
        tmp=la[n-1]
        for j in range(n-1, 0, -1):
            la[j]=la[j-1]
        la[0]=tmp

'''
print("=====================================================")
print(n)
for li in ln:
    for j in li:
        print(j, end=' ')
    print()

print(m)
for li in lm:
    for j in li:
        print(j, end=' ')
    print()
print("=====================================================")'''

for li in lm:
    #print(li[0], li[1], li[2])
    if(li[1]==0):
        sorting_l(ln[li[0]-1], int(li[2]))
    else:
        sorting_r(ln[li[0]-1], int(li[2]))

'''
for li in ln:
    for j in li:
        print(j, end=' ')
    print()
'''
nRslt=0
s=0
e=n
for i in range(n):
    for j in range(s, e):
       #print(ln[i][j])
       nRslt+=ln[i][j]
    if(i<n//2):
        s+=1
        e-=1
    else:
        s-=1
        e+=1

print(nRslt)
