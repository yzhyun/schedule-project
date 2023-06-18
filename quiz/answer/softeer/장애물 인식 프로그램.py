import sys
sys.stdin = open("../input.txt", "rt")

n = int(input())
g = [list(map(int, input())) +[0] for _ in range(n)]
#g.insert(0, [0] * (n+2))
#g.append([0] * (n+2))

for x in g:
    print(x)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

res = []
def DFS(x, y):
    global cnt
    if x < 0 or y < 0 or x > n-1 or y > n-1:
        return
    if g[x][y] == 1:
        cnt += 1
        g[x][y] = 0
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]

            if 0 <= xx < n and 0 <= yy < n and g[xx][yy] == 1:
                DFS(xx, yy)

for i in range(n):
    for j in range(n):
        cnt = 0
        DFS(i, j)
        if cnt != 0:
            res.append(cnt)
res.sort()
print(len(res))
for n in res:
    print(n)



