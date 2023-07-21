import sys
sys.stdin = open("input.txt", "rt")

T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())

    dy = [[0] * (n+1) for _ in range(k+1)]

    for i in range(n+1):
        dy[0][i] = i
    for i in range(k+1):
        dy[i][0] = 0

    for k in range(1, k+1):
        for n in range(1, n+1):
            dy[k][n] = dy[k-1][n] + dy[k][n-1]

    print(dy[k][n])
