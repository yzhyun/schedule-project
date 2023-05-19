import sys
sys.stdin = open("input.txt", "rt")

dDec={}
dDec[0] = {1, 2, 3, 5, 6, 7}
dDec[1] = {3, 6}
dDec[2] = {1, 3, 4, 5, 7}
dDec[3] = {1, 3, 4, 6, 7}
dDec[4] = {2, 3, 4, 6}
dDec[5] = {1, 2, 4, 6, 7}
dDec[6] = {1, 2, 4, 5, 6, 7}
dDec[7] = {1, 2, 3, 6}
dDec[8] = {1, 2, 3, 4, 5, 6, 7}
dDec[9] = {1, 2, 3, 4, 6, 7}


n = int(input())

for i in range(n):

    sBef, sAft = map(str, input().split())
    nBef = int(sBef)
    nAft = int(sAft)

    lBef = [ i for i in dDec[nBef]]
    lAft = [ i for i in dDec[nAft]]

    dBef = {}
    for i in range(len(lBef)):
        dBef[i] = i

    cnt = 0
    while lAft :
        if lAft.pop() not in lBef:
            cnt += 1
        else:
            lBef.pop()
    print(cnt + len(lBef))





