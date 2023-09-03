import sys
sys.stdin = open("input.txt", "rt")

n = int(input())
#tree = dict()
tree = {}

for i in range(n):
    n, l, k = map(str, input().split())
    tree[n] = (l, k)

def DFS(root):
    if root == '.':
        return
    else:
        print(root, end = '')
        DFS(tree[root][0])
        DFS(tree[root][1])

DFS('A')
