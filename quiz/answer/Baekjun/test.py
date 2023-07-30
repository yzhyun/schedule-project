import sys


a, b =map(int, input().split())


result = 0
def DFS(x, y):
    if x % y == 0:
        return y
    else:
        return DFS(y, x % y)



print(DFS(a, b))


