import sys
sys.stdin=open("input.txt", "rt")

n, t=map(int,input().split())
print(n, t)

ln=[ i+1 for i in range(n)]

while 1 < len(ln) :
    for i in range(t-1):
        ln.append(ln.pop(0))
    ln.pop(0)
print(ln[0])

