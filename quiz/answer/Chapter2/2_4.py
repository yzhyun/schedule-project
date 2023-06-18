import sys
sys.stdin = open("../input.txt", "rt")

N = int(input())
lScore = list(map(int, input().split()))
avg = sum(lScore) / N
avg = int(avg + 0.5)
minVal = 2147000000

for idx, val in enumerate(lScore):
    tmp = abs(val - avg)
    if tmp < minVal:
        minVal = tmp
        score = val
        res = idx+1
    elif tmp == minVal:
        if val > score:
            score = val
            res = idx+1
print(avg, res)



