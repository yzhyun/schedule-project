import sys
sys.stdin = open("../input.txt", "rt")

n = int(input())
meet = [list(map(int, input().split())) for _ in range(n)]

meet.sort(key = lambda x: (x[1], x[0]))

et = 0
cnt = 0
for s, e in meet:
    if s >= et:
        cnt += 1
        et = e

print(cnt)
