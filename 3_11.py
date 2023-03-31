import sys
sys.stdin=open("input.txt", "rt")

a=[list(map(int, input().split())) for _ in range(7)]

print("===========================")
for li in a:
    for j in li:
        print(j, end=' ')
    print()
print("===========================")

cnt=0

def rowCheck(b):
    tmpCnt=0
    resCnt=0
    for i in range(3):
        b=li[i:i+5]
        s = 0
        e = 4
        for j in range(2):
            if (b[s] == b[e]):
                s += 1
                e -= 1
                tmpCnt += 1
        if tmpCnt > 1:
            tmpCnt = 0
            resCnt += 1
    return resCnt


lTmp = []
for i in range(7):
    lTmp.append([a[j][i] for j in range(7)])

for li in a:
    n = rowCheck(li)
    cnt += n

for li in lTmp:
    n = rowCheck(li)
    cnt += n

print(cnt)
