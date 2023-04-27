import sys
sys.stdin=open("input.txt", "rt")

n  = int(input())
ln = [list(map(int, input().split())) for _ in range(n)]

print(n)
print(ln)

ln.sort(reverse=True, key=lambda x: (x[0], x[1]))

for x,y in ln:
    print(x, y)

nMax = ln[0][1]
cnt = 1

for x, y in ln:
    if y > nMax :
        cnt+=1
        nMax=y

print(cnt)