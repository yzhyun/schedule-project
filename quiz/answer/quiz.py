import sys
sys.stdin=open("input.txt","rt")
n,m = map(int,sys.stdin.readline().split())
ln = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
lm = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

max_length=[]

print(ln)
print(lm)

while ln or lm :

    diff_length = lm[0][0]-ln[0][0]

    if diff_length > 0:
        max_length.append(lm[0][1]-ln[0][1])
        print(max_length)
        ln.pop(0)
        print(ln)
        lm[0][0] = diff_length
    elif diff_length < 0:
        max_length.append(lm[0][1]-ln[0][1])
        lm.pop(0)
        ln[0][0] = -diff_length
    else :
        max_length.append(lm[0][1]-ln[0][1])
        lm.pop(0)
        ln.pop(0)
print(max_length)
print(max(max_length))