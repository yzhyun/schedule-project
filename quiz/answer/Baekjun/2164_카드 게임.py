'''
6
'''
'''
4
'''

import sys
from collections import deque
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

n = int(input())
ln = [i for i in range(1, n+1)]

dq = deque(ln)

print(dq)
while len(dq) > 1:
    dq.popleft()
    dq.append(dq.popleft())

print(dq[0])



