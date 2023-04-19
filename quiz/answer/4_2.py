import sys
sys.stdin=open("input.txt", "rt")

#150
k, n = map(int, input().split())
print(k,n)
ln=[]
for _ in range(k):
   ln.append(int(input()))

ln.sort()
print(ln)

lt=ln[0]
rt=ln[len(ln)-1]
print(lt, rt)

'''
1. mid(평균값)으로 검증 진행
2. 각 자리의 수를 mid로 나눈 값의 총합이 n인지 체크로직
3. n이 넘으면 작은 쪽으로 반복, 넘지 않으면 큰 쪽으로 반복 체크
'''
while lt<=rt:
    mid=(lt+rt)//2
    cnt=0
    for idx, val in enumerate(ln):
        cnt += val//mid
    if cnt >= n :
        lt=mid+1
    elif cnt < n :
        rt=mid-1

print(mid)
