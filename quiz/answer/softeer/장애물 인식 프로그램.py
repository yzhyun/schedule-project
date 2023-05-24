import sys

sys.stdin = open("input.txt", "rt")

n = int(input())

# graph = [list(input().split()) for _ in range(n)]
graph = [list(map(int, input())) for _ in range(n)]

for i in range(n):
    print(graph[i])

print("-----")

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return 0
    if graph[x][y]:
        graph[x][y] = 0

        count = 1

        for i in range(4):
            count += dfs(x + dx[i], y + dy[i])
        return count
    return 0


answer = []
for i in range(n):
    for j in range(n):
        res = dfs(i, j)

        if res:
            answer.append(res)

print(len(answer))
answer.sort()
for a in answer:
    print(a)
