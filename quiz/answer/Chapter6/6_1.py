import sys
sys.stdin = open("../input.txt","rt")

def DFS(x):
    if x == 0:
        return
    else:
        a = x//2
        print(x,a)
        DFS(a)
        print(x%2, end='')
DFS(int(input()))

