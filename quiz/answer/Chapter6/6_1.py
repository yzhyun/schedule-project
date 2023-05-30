import sys
sys.stdin = open("../input.txt", "rt")

n = int(input())

def DFS(n):
    if n == 0:
        return
    else:
        DFS(n//2)
        print(n%2, end=' ')

DFS(n)
