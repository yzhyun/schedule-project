# import sys
# from colleciton import deque
# sys.stdin = open("../input.txt", "rt")
#
# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]

#dp로 풀어보기
# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]
# dp = [[0]*n for _ in range(n)]
#
# dp[0][0] = arr[0][0]
# #첫 행과 첫 열의 경우, 한 가지의 길 뿐이므로 먼저 셋팅한다.
# for i in range(1, n):
#     dp[0][i] = dp[0][i-1] + arr[0][i]
#     dp[i][0] = dp[i-1][0] + arr[i][0]
# for i in range(1, n):
#     for j in range(1, n):
#         dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + arr[i][j]

#print(dp[n-1][n-1])

#BPS로 풀어보기
# import sys
# from collections import deque
#
# sys.stdin = open("../input.txt", "rt")
#
# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]
# ch = [[0] * n for _ in range(n)]
#
# dq = deque()
# dq.append((0, 0))
# ch[0][0] = 3
#
# dx = [1, 0]
# dy = [0, 1]
#
# while dq:
#     x, y = dq.popleft()
#     for i in range(2):
#         nx = x + dx[i]
#         ny = y + dy[i]
#
#         if nx > n-1 or ny > n-1:
#             continue
#
#         if ch[nx][ny] == 0 or ch[nx][ny] > arr[nx][ny] + ch[x][y]:
#             ch[nx][ny] = arr[nx][ny] + ch[x][y]
#         dq.append((nx, ny))
# print(ch)

#DFS로 풀어보기
import sys
from collections import deque

sys.stdin = open("../input.txt", "rt")

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [1, 0]
dy = [0, 1]

tmp = []
case = []
a = []

def dfs(x, y):
    global cnt, tmp
    if x == n-1 and y == n-1:
        print(tmp)
        case.append(tmp.copy())
        cnt += 1
        a.append(sum(tmp))

    else:
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < n and ny < n:
                tmp.append(arr[nx][ny])
                dfs(nx, ny)
                tmp.pop()

cnt = 0
tmp.append(arr[0][0])
dfs(0,0)

print(cnt)
print(a)
print(min(a))
print(case)
