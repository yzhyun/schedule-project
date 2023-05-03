import sys
sys.stdin=open("input.txt", "rt")

n=int(input())
ln=list(map(int, input().split()))

print(n)
print(ln)

lrslt=[n for _ in range(n)]
print(lrslt)

for i in range(n):

    cnt=0
    p = i+1
    for j in range(n):
        if p < lrslt[j]:
            cnt += 1

        if cnt > ln[i]:
            lrslt[j] = p
            break

print(lrslt)