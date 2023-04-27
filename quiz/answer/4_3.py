import sys

sys.stdin = open("input.txt", "rt")

n, m = map(int, input().split())
print(n, m)

ln = list(map(int, input().split()))
#17

print(ln)
print(sum(ln))
lt=ln[0]
rt=sum(ln)
res=0

while lt<=rt:
    mid = (lt+rt) // 2
    cnt = 1
    sum = 0
    for x in ln :
        if sum+x > mid :
            cnt += 1
            sum = x
        else :
            sum += x
    if cnt <= m:
        rt = mid - 1
        res = mid
    else :
        lt = mid + 1


print(res)


