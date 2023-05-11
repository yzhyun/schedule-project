import sys
sys.stdin=open("../input.txt", "rt")

n,m = map(int, input().split())
ln=list(map(int, input().split()))
ln.sort()
print(n, m)
print(ln)

cnt = 0
while len(ln)>0:
    if ln[0]+ln[len(ln)-1] > m :
        ln.pop(len(ln)-1)
        cnt+=1
    else :
        ln.pop(0)
        ln.pop(len(ln)-1)
        cnt+=1

print(cnt)



