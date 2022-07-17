import sys
sys.stdin=open("input.txt", "rt")

n=int(input())
arr=[list(map(int, input().split())) for _ in range(n)]
arr.insert(0, [0]*n)
arr.append([0]*n)

for li in arr:
    li.insert(0,0)
    li.append(0)

dx=[-1,0,1,0]
dy=[0,1,0,-1]
print("=====================================================")
print(n)
for li in arr:
    for i in li:
        print(i, end= ' ')
    print()
print("=====================================================")

cnt=0
for i in range(1, n+1):
    for j in range(1, n+1):
        if(all(arr[i][j]>arr[i+dx[k]][j+dy[k]] for k in range(4))):
            cnt+=1
print(cnt)


