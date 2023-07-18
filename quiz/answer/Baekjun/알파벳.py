import sys
sys.stdin = open("input.txt", "rt")

r, c = map(int, input().split())
arr = [list(input()) for _ in range(r)]
print(arr)

ch = []
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = 0
def DFS(x, y, v):
    global cnt
    ch.append(v)
    cnt += 1
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0<=nx<r and 0<=ny<c and arr[nx][ny] not in ch:
            DFS(nx, ny, arr[nx][ny])

DFS(0,0,arr[0][0])
print(cnt)

