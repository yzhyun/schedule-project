import sys
sys.stdin=open("../input.txt", "rt")

n = int(input())
ln = [list(map(int, input().split())) for _ in range(n)]

ln.sort(reverse=True, key = lambda x:(x[0], x[1]))
print(ln)

mw = 0
cnt = 0
for t, w in ln:
    if w > mw:
        mw = w
        cnt += 1
print(cnt)