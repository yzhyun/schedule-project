import sys
sys.stdin = open("input.txt", "rt")

n, m = map(int, input().split())
print(n,m)

ln = []
for _ in range(n):
    ln.append(int(input()))
ln.sort()
print(ln)

lt = ln[0]
rt = ln[len(ln)-1]
cnt = 0
def Count(mid):
    cnt = 1
    ep = ln[0]
    for i in range(1,n):
        if ln[i]- ep >= mid :
            cnt+=1
            ep =ln[i]

    return cnt

while lt <= rt :
    mid = (lt+rt)//2

    if Count(mid) >= m :
        lt = mid + 1
        res = mid
    else :
        rt = mid - 1

print(res)