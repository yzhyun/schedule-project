import sys
sys.stdin = open("../input.txt", "rt")
input = sys.stdin.readline

n, m = map(int, input().split())

ln = [int(input().rstrip()) for _ in range(n)]
ln.sort()

lt = 1
rt = ln[-1] - ln[0]

result=0

while lt <= rt:
    mid = (lt + rt) // 2
    cnt = 1
    cur = ln[0]
    for i in range(1, n):
        if ln[i]-cur >= mid:
            cnt += 1
            cur = ln[i]
    if cnt >= m:
        result = mid
        lt = mid + 1
    else:
        rt = mid - 1
print(result)




