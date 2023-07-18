import sys
from collections import deque
sys.stdin = open("../input.txt", "rt")


N,M,V = map(int,input().split())

#행렬 만들기
graph = [[0]*(N+1) for _ in range(N+1)]
for i in range (M):
    a,b = map(int,input().split())
    graph[a][b] = graph[b][a] = 1

# for g in graph:
#     print(g)

ch1 = [0]*(N+1)
ch2 = ch1.copy()


def DFS(v):
    ch1[v] = 1
    print(v, end=' ')
    for i in range(1, N+1):
        if graph[v][i] == 1 and ch1[i] == 0:
            DFS(i)

dq = deque()

def BFS(v):

    dq.append(v)
    ch2[v] = 1
    while dq:
        v = dq.popleft()
        print(v, end= ' ')
        for i in range(1, N+1):
            if graph[v][i] == 1 and ch2[i] == 0:
                dq.append(i)
                ch2[i] = 1



DFS(V)
print()
BFS(V)



