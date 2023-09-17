import sys

sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

def DFS(L, s):
    if L == 6:
        for val in res:
            print(val, end= ' ')
        print()
        return
    else:
        for i in range(s, k):
            res[L] = ln[i+1]
            DFS(L + 1, i + 1)
while 1:
    ln = list(map(int, input().split()))
    if ln[0] == 0:
         break;
    k = ln[0]
    res = [0] * 6

    DFS(0, 0)
    print()
