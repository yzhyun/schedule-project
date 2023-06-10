#사다리타기
import sys
sys.stdin = open("../input.txt", "rt")

board = [list(map(int, input().split())) for _ in range(10)]
ch = [[0] * 10 for _ in range(10)]

def DFS(x, y):
    ch[x][y] = 1
    if x == 0:
        print(y)
    else :
        if y-1 >= 0 and board[x][y-1] == 1 and ch[x][y-1] == 0:
            DFS(x, y-1)
        elif y+1 < 10 and board[x][y+1] == 1 and ch[x][y+1] == 0:
            DFS(x, y+1)
        else:
            DFS(x-1, y)



for y in range(10):
    if board[9][y] == 2:
        DFS(9, y)



# ex = ey = -1
# # 우, 좌, 아래
# dx = [0, 0, 1]
# dy = [1, -1, 0]
#
# for i in range(10):
#     for j in range(10):
#         if board[i][j] == 2:
#             ex = i
#             ey = j
#
# def DFS(x, y, a):
#
#     if x == 9:
#         if board[x][y] == 2:
#             print(a)
#     else:
#         for i in range(3):
#             xx = x + dx[i]
#             yy = y + dy[i]
#             if 0 <= xx < 10 and 0 <= yy < 10 and ch[xx][yy] == 0 \
#                     and (board[xx][yy] == 1 or board[xx][yy] == 2 ):
#                 ch[xx][yy] = 1
#                 ch[x+1][y+0] = 1
#                 DFS(xx, yy, a)
#
# board[1][0] = 1
# for i in range (10):
#     if board[0][i] == 1:
#         ch = [[0] * 10 for _ in range(10)]
#         DFS(0, i, i)






