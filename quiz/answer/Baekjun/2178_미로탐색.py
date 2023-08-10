import sys
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(100000)

n, m = map(int, input().split())

g = [list(map(int, input())) for _ in range(n)]

for x in g:
    print(x)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cnts = []
cnt = 0
def DFS(x, y):
    global cnt
    cnt += 1
    if x == n-1 and y == m-1:
        cnts.append(cnt)
    else:
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]

            if n-1 >= xx >= 0 and m-1 >= yy >= 0 and g[xx][yy] == 1:
                print(xx, yy)
                g[xx][yy] = 0
                DFS(xx, yy)
                g[xx][yy] = 1
                cnt -= 1

g[0][0] = 0
DFS(0, 0)
print(min(cnts))



