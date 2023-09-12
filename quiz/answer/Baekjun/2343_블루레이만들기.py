import sys
sys.stdin = open("input.txt", "rt")

n, m = map(int, input().split())
ln = list(map(int, input().split()))


st = max(ln)
et = sum(ln)

while st <= et:
    mid = (st + et) // 2
    sum = 0
    cnt = 1

    for val in ln:
        # sum + 다음 값이 기준(mid) 보다 큰 경우, 카운팅 및 sum 초기화
        if sum + val > mid:
            cnt += 1
            sum = 0
        sum += val
    if cnt > m:
        st = mid + 1
    else:
        et = mid - 1

print(st)

