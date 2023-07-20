import sys
sys.stdin = open("../input.txt", "rt")

n = int(input())
bricks = [list(map(int, input().split())) for _ in range(n)]

#널이 기준으로 내림차순 sorting
bricks.sort(reverse=True)

dy = [0] *(n)
dy[0] = bricks[0][1]

'''
1. 돌의 갯수 만큼 탐색
2. 타겟 돌의 앞부터 순차적 탐색
    무게가 작은 경우, [i][2]
    높이 값을 기록한다. (기존 값보다 높이가 큰 경우 찾기)    
'''
for i in range(1, n):
    max_h = 0
    for j in range(i-1, -1, -1):
        if bricks[i][2] < bricks[j][2] and dy[j] > max_h:
            max_h = dy[j]
        dy[i] = max_h + bricks[i][1]

print(max(dy))

