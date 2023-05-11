import sys
sys.stdin=open("../input.txt", "rt")

n=int(input())
ln=[list(map(int, input().split())) for _ in range (n)]

print(n)


ln.insert(0, [0 for _ in range(n+2)])
ln.append([0 for _ in range(n+2)])

dx=[-1,0,1,0]
dy=[0,1,0,-1]
for i in range(1,n+1):
    ln[i].insert(0, 0)
    ln[i].append(0)

for i,val in enumerate (ln):
    print(val)

cnt=0
for i in range(1, n+1):
    for j in range(1, n+1):
        if all([ln[i][j] > ln[i+dx[k]][j+dy[k]] for k in range(4)]):
            cnt += 1

print(cnt)
