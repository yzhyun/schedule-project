import sys

sys.stdin = open("../input.txt", "rt")

n, m = map(int, input().split())
g = [[0] * (n + 1) for _ in range(n + 1)]
ch = [0] * (n + 1)
cnt = 0
# print(g)
for _ in range(m):
    a, b = map(int, input().split())
    g[a][b] = 1


def DFS(L):
    global cnt
    if L == n:
        cnt += 1
        for x in path:
            print(x, end=' ')
        print()
    else:
        for i in range(1, n + 1):
            if g[L][i] == 1 and ch[i] == 0:
                ch[i] = 1
                path.append(i)
                DFS(i)
                ch[i] = 0
                path.pop()


path = []
path.append(1)
ch[1] = 1

DFS(1)
print(cnt)
