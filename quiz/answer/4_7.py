import sys
sys.stdin=open("input.txt", "rt")

n=int(input())
ln=list(map(int, input().split()))
m=int(input())

print(n)
print(ln)
print(m)
cnt=0
for _ in range(m):
    cnt+=1
    ln.sort()
    print(ln)
    ln[0] += 1
    ln[n-1] -= 1

ln.sort()

print(ln[n-1]-ln[0])
print(ln)