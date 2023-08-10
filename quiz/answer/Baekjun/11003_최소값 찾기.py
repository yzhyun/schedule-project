'''
12 3
1 5 2 3 6 2 3 7 3 5 2 6
'''
'''
1 1 1 2 2 2 2 2 3 3 2 2
'''
import sys
from collections import deque
sys.stdin = open("input.txt", "rt")

dq = deque()

n, m = map(int, input().split())
ln = list(map(int, input().split()))

for i in range(n):
    while dq and dq[-1][1] > ln[i]:
        dq.pop()
    dq.append((i, ln[i]))
    if dq[0][0] <= i-m:
        dq.popleft()
    print(dq[0][1], end = ' ')