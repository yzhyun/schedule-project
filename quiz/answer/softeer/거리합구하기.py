import sys
sys.stdin = open("../input.txt", "rt")
N = int(input())
node = [[] for _ in range(N+1)]

for i in range(N-1):
    x, y, t = map(int, input().split())
    node[x].append([y, t])
    node[y].append([x, t])

for x in node:
    print(x)