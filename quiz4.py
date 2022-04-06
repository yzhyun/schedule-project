#평균에 가장 가까운
#점수가 높은 학생의 번호
#학생번호가 빠른
#출력은 평균과 평균에 가장 가까운 학생의 번호
#74 7

import sys
sys.stdin=open("input.txt", "rt")

n=int(input())
ln=list(map(int, input().split()))
avg=round(sum(ln)/len(ln))
print("평균: %d" %avg)
print(ln)

rslt = 1000
ridx = -1;
diff = 1000
for idx, val in enumerate(ln):

    if(abs(val-avg)<diff):
        rslt=val
        ridx=idx
        diff=abs(val-avg)
    elif(abs(val-avg)==diff):
        if(val>rslt):
            rslt = val
            ridx = idx
        elif(val==rslt):
            if(idx<ridx):
                rslt=val
                ridx=idx

print(avg, ridx+1)



