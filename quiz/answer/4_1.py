import sys
sys.stdin=open("input.txt", "rt")

n, m= map (int, input().split())
print(n,m)
ln=list(map(int, input().split()))
print(ln)

ln.sort()
print(ln)

mid=-1
lt=0
rt=len(ln)-1
# for idx, val in enumerate (ln):
#     nRslt=ln.index(m)
# print(nRslt+1)

while lt<=rt:
    mid = (lt+rt)//2
    if ln[mid] == m :
        print(mid+1)
        break
    elif ln[mid] > m :
        rt=mid-1
    elif ln[mid] < m :
        lt=mid+1
