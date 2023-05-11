import sys
sys.stdin = open("../input.txt", "rt")

n = int(input())
ln = list(map(int, input().split()))

print(n)
print(ln)

lt=0
rt=n-1
p=0
ltmp=[]
sRes=""

print(lt, rt)
#print(ln[rt])
while lt <= rt :
    if ln[lt] > p :
        ltmp.append([ln[lt], 'L'])

    if ln[rt] > p :
        ltmp.append([ln[rt], 'R'])

    ltmp.sort()

    if len(ltmp) == 0 :
        break
    else :
        sRes += ltmp[0][1]
        p = ltmp[0][0]

        if ltmp[0][1] == 'L' :
            lt+=1
        else :
            rt-=1
    ltmp.clear()

print(sRes)