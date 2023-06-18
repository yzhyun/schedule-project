import sys
sys.stdin = open("../input.txt", "rt")

g = [list(map(int, input().split())) for _ in range(9)]

#가로, 세로 체크
for i in range(9):
    ch1 = [1] + [0] * 9
    ch2 = [1] + [0] * 9
    for j in range(9):
        ch1[g[i][j]] = 1
        ch2[g[j][i]] = 1
    if sum(ch1) < 10 or sum(ch2) < 10:
        print("NO1")
        sys.exit(0)

for i in range(3):
    for j in range(3):
        ch3 = [1] + [0] * 9
        for k in range(3):
            for s in range(3):
                ch3[g[i*3+k][j*3+s]] = 1
        print(ch3)
        if sum(ch3) < 10:
            print("NO2")
            sys.exit(0)
print("YES")
