import sys
sys.stdin=open("../input.txt", "rt")

n = int(input())
ln = list(map(str, input().split()))
maxVal = -214700000
pindex = -1
print(ln)

def digit_sum(x):
    cnt = 0
    for i in range(len(x)):
        cnt += int(x[i])
    return cnt


for idx, val in enumerate(ln):

    retVal = digit_sum(val)
    if retVal > maxVal:
        maxVal = retVal
        pindex = idx

print(ln[pindex])





