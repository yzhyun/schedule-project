import sys
sys.stdin=open("../input.txt", "rt")

ln=[list(map(int, input().split())) for _ in range(7)]
ltmp=[]
print(ln)


cnt=0
for i in range(7):
    for j in range(3):
       ltmp1=ln[i][j:j+5]
       ltmp2=ln[i][j:j+5]
       ltmp2.reverse()
       print(ltmp1)
       if ltmp1==ltmp2 :
           print(ltmp1, ltmp2)
           cnt+=1


print("!!!!!!!!!!!!!!!!!!!!")
ltmp3=[]
k=0
for k in range(3):
    for i in range(7):
        for j in range(k,k+5):
            ltmp3.append(ln[j][i])

        print(ltmp3)
        ltmp4=ltmp3.copy()
        ltmp4.reverse()

        if ltmp3 == ltmp4:
            print(ltmp3, ltmp4)
            cnt+=1
        ltmp3 = []
        ltmp4 = []


print(cnt)