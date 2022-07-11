import sys
sys.stdin=open("input.txt", "rt")

n, m=map(int,input().split())
ln=list(map(int, input().split()))
print("=============================================")
print(n)
print(m)
print(ln)
print("=============================================")
'''
#tot, lt, rt 로 구분
lt=0
rt=1
tot=ln[0]
cnt=0
cn2=0
while True:
    print(lt, rt, tot)
    if(tot<m):
        if rt<n:
            tot+=ln[rt]
            rt+=1
        else:
            break
    elif(tot==m):
        cnt+=1
        tot-=ln[lt]
        lt+=1
    else:
        tot-=ln[lt]
        lt+=1

'''
#lt가 n을 가르킬 때까지
#tot가 m보다
#작은경우
#rt 이동, tot 증가
#같은 경우
#lt 이동, tot 0
#큰 경우
#lt 이동, tot 0

lt=0
rt=1
cnt=0
tot=ln[0]

while True:
    #세가지 경우, tot 작은 경우, 같은 경우, 큰 경우
    print(lt, rt, cnt)
    if(tot<m):
        if(rt<n):
            tot+=ln[rt]
            rt+=1
        else:
            break
    elif(tot==m):
        cnt+=1
        tot-=ln[lt]
        lt+=1
    else:
        tot-=ln[lt]
        lt += 1

print(cnt)



