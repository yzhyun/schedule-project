import sys
sys.stdin=open("../input.txt", "rt")

n = int(input())
ln = list(map(int, input().split()))
ch = [0]*n
preVal = 0
for i in range(n):
    if ln[i] == 1:
        if preVal == 0:
            ch[i] = 1
            preVal = 1
        else:
            ch[i] = preVal + 1
            preVal = ch[i]
    else:
        preVal = 0

print(sum(ch))
