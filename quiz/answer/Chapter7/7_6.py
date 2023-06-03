import sys
sys.stdin = open("../input.txt", "rt")

sN = str(input())
ch=[]
sVal = ""

def DFS(L, n):
    global sVal
    if L == len(sN):
        sVal = ""
        for i, val in enumerate(ch):
            sVal += val
        print(sVal)
    else:
        ch.append(sN[L])
        DFS(L+1, sN[L])
        ch.pop()
        DFS(L+1, sN[L])
DFS(0, 0)
