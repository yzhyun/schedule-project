import sys
sys.stdin=open("../input.txt", "rt")

n=int(input())
ln = [list(map(int, input().split())) for _ in range(n)]


print(n)
print(ln)

ln.sort(key=lambda x: (x[1], x[0]))
print(ln)

cnt=1
idx=0
ed = ln[0][1]
for i in range(1, n):

    if  ln[i][0] >= ed:
        ed = ln[i][1]
        cnt += 1
print(cnt)
# while idx < n :
#     a= ln[0][idx]
#     print(a)
#     idx+=1
#     if nTrgt == a:
#         nTrgt = ln[idx][1]
#         cnt+=1


# et=0
# cnt=0
# for s, e in ln :
#     print(s,e)
#     if s >= et :
#         et=e
#         cnt+=1
#
# print(cnt)

