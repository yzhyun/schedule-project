import sys
sys.stdin=open("input.txt", "rt")

n,m = map(int, input().split())
print (n,m)

ln = list(map(int, input().split()))

print(ln)
print(sum(ln))

lt=ln[0]
rt=sum(ln)


while lt <= rt:
    mid=(lt+rt)//2
    max = 0
    cnt = 0
    #체크로직 ( ln 의 val 값을 수용하느냐)
    for i, val in enumerate(ln):
        max += val
        if max > mid :
            cnt += 1

        if cnt >= 3 :
            lt = mid+1
        else :
            rt = mid-1

print(mid)