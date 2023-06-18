import sys
sys.stdin=open("../input.txt", "rt")

n = int(input())
g = [[0] + list(map(int, input().split())) + [0] for _ in range(n) ]
g.insert(0, [0] * (n+2))
g.append([0] * (n+2))

for i in range(n+2):
    for j in range(n+2):
        print(g[i][j], end = '\t')
    print()

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        # if all(g[i][j] > g[i + dx[k]][j + dy[k]] for k in range(4)):
        #     cnt += 1
        cnt2 =0
        for k in range(4):
            x = i + dx[k]
            y = j + dy[k]
            if g[i][j] > g[x][y]:
                cnt2 += 1

        if cnt2 == 4:
            cnt += 1
print(cnt)