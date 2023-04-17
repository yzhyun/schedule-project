import sys

sys.stdin = open("input.txt", "rt")


def fAnswer(ln):
    a = ln.copy()

    for i in range(9):
        xTmp = set(a[i])
        if len(xTmp) < 9:
            return False

    yTmp = set()
    for i in range(9):
        for j in range(9):
            yTmp.add(ln[j][i])
        if len(yTmp) < 9:
            return False


    zTmp = set()
    k=l=0
    for i in range(2+k):
        for j in range(2+l):
            zTmp.add(ln[i][j])



    return True


ln = [list(map(int, input().split())) for _ in range(9)]
print(ln)
if fAnswer(ln):
    print("YES")
else:
    print("NO")
