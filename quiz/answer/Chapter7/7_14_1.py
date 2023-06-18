import sys
from collections import deque
sys.stdin = open("../input.txt", "rt")

dq = deque()
n = int(input())

q = [list(map(int, input().split())) for _ in range(n)]

maxVal = -2147000000
minVal = 2147000000
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
res = list()

def DFS(x, y):

for