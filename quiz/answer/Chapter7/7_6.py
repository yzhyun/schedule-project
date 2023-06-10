import sys
sys.stdin = open("../input.txt", "rt")


lc = list(map(int, input()))
lc.append(-1)
print(lc)
res = [0]*len(lc)

def DFS(L, p):
    if L == len(lc)-1:
        for i in range(p):
            print(res[i] , end = ' ')
        print()
    else:
        for i in range(1, 27):
            if i == lc[L]:
                res[p] = i
                DFS(L+1, p+1)
            elif i >= 10 and i//10 == lc[L] and i%10 == lc[L+1]:
                res[p] = i
                DFS(L+2, p+1)

DFS(0, 0)





