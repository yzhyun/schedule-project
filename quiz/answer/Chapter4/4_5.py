import sys
sys.stdin=open("../input.txt", "rt")

n = int(input())
ln = [list(map(int, input().split())) for _ in range(n)]



ln.sort( key = lambda x : x[1] )
print(ln)

res = 0
e = 0

for x, y in ln:
    if e <= x:
        e = y
        res += 1
print(res)