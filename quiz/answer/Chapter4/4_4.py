import sys
sys.stdin=open("../input.txt", "r")

n, m = map(int, input().split())
ln = [int(input()) for _ in range(n)]
ln.sort()

def Count(mid):
    cnt = 1
    ep = ln[0]
    for i in range(1, n):
        if ln[i] - ep >=  mid:
            cnt += 1
            ep = ln[i]
    return cnt


lt = 1
rt = max(ln)

while lt <= rt:
    mid = (lt + rt) // 2
    if Count(mid) >= m:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(res)


