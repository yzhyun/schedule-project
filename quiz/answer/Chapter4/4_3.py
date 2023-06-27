import sys
sys.stdin = open("../input.txt", "rt")

n, m = map(int, input().split())
ln = list(map(int, input().split()))

maxTime = sum(ln)
print(maxTime)

lt = 0
rt = maxTime
minVal = 2147000000
while lt <= rt:
    mid = (lt+rt) // 2
    totVal = 0
    cnt = 1
    for val in ln:
        if totVal+val > mid:
            totVal = val
            cnt += 1
        else:
            totVal += val

    if cnt <= m :
        minVal = mid
        rt = mid - 1
    elif cnt > m :
        lt = mid+1


print(minVal)







