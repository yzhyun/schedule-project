import sys
from collections import deque

sys.stdin = open("input.txt", "rt")

n, m = map(int, input().split())

standard =  [list(map(int, input().split())) for _ in range(n)]
quiz =      [list(map(int, input().split())) for _ in range(m)]

ds = deque(standard)
dq = deque(quiz)

lmax = []
while dq:
    temp_q = dq.popleft()
    temp_s = ds.popleft()

    if temp_q[0] - temp_s[0] > 0:   #q 가 더 큰 경우, 차이 값을 q로 업데이트 한다. s 항목은 삭제
        dq.appendleft([temp_q[0] - temp_s[0], temp_q[1]])
        lmax.append(temp_q[1]-temp_s[1])
    elif temp_q[0] - temp_s[0] < 0: #s 가 더 큰 경우, 차이 값을 s로 업데이트 한다. q 항목은 삭제
        ds.appendleft([temp_s[0]- temp_q[0], temp_s[1]])
        lmax.append(temp_q[1]-temp_s[1])
    else:
        lmax.append(temp_q[1]-temp_s[1])

if max(lmax) >= 0 :
    print(max(lmax))
else :
    print(0)
