import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

n = int(input())
matrix = [list(map(int, input().split())) for _ in range (n)]

for x in matrix:
    print(x, end=' ')
    print()

b_cnt = 0   #1 블루
w_cnt = 0   #0 화이트
def dfs(x, y, n):
    global b_cnt, w_cnt
    color = matrix[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if matrix[i][j] != color:
                dfs(x, y, n//2)
                dfs(x, y+n//2, n//2)
                dfs(x+n//2, y, n//2)
                dfs(x+n//2, y+n//2, n//2)
                return
    if color == 1:
        b_cnt += 1
    else:
        w_cnt += 1

dfs(0,0,n)
print(w_cnt)
print(b_cnt)




