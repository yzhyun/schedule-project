import sys
sys.stdin = open("input.txt", "rt")

n = int(input())
tree = list(map(int, input().split()))
k = int(input())

def DFS(v):
