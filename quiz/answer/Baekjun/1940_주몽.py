import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

n = int(input())
m = int(input())

ln = list(map(int, input().split()))
ln.sort()

lt = 0
rt = len(ln)-1

cnt = 0
tsum = 0
while lt <= rt:
    if ln[lt] + ln[rt] > m:
        rt -= 1
    elif ln[lt] + ln[rt] < m:
        lt += 1
    elif ln[lt] + ln[rt] == m:
        rt -= 1
        lt += 1
        cnt += 1

print(cnt)




