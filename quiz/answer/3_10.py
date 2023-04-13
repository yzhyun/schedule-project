import sys

sys.stdin = open("input.txt", "rt")


def fAnswer(ln):
    a = ln.copy()

    for i in range(9):
        xTmp = set(a[i])
        print(xTmp)
        if len(xTmp) < 9:
            return False

    yTmp = set()
    for i in range(9):
        for j in range(9):
            yTmp.add(ln[j][i])
        if len(yTmp) < 9:
            return False




    return True


ln = [list(map(int, input().split())) for _ in range(9)]
print(ln)
if fAnswer(ln):
    print("YES")
else:
    print("NO")
