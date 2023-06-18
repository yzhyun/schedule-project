import sys
sys.stdin = open("../input.txt", "rt")
from collections import deque

dq = deque()
s, e = map(int, input().split())
MAX = 10000
ch = [0] * (MAX+1)
dis = [0] * (MAX+1)
dq.append(s)
while dq:
    now = dq.popleft()
    if now == e:
        break
    else:
        for next in (now-1, now+1, now+5):
            if 0 < next <= MAX:
                if ch[next] == 0:
                    dq.append(next)
                    ch[next] = 1
                    dis[next] = dis[now] + 1
print(dis[e])
