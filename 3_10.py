import sys
sys.stdin=open("input.txt" , "rt")

a=[list(map(int, input().split())) for _ in range(9)]

print("============================================")
for li in a:
    for j in li:
        print(j , end= ' ')
    print()
print("============================================")

def check(a):
    #전체 ROW/COL 체크
    for i in range(9):
        ch1 = [0] * 10
        ch2 = [0] * 10
        for j in range(9):
            ch1[a[i][j]]=1
            ch2[a[j][i]]=1
        if(sum(ch1)!=9 or sum(ch2)!=9):
            return False
    #구간 3x3 체크
    for i in range(3):
        for j in range(3):
            ch3 = [0] * 10
            for k in range(3):
                for l in range (3):
                    ch3[a[i*3+k][j*3+l]]=1
            if(sum(ch3)!=9):
                return False
    return True


    return True

if check(a):
    print("YES")
else:
    print("NO")