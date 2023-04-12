import sys

sys.stdin = open("input.txt", "rt")

n = int(input())
ln = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
lm = [list(map(int, input().split())) for _ in range(m)]
print(n)
print(ln)

for i, val in enumerate(ln):
    print(val)

print(m)
print(lm)

# la=ln[0]
# la.append(la.pop(0))
# la.insert(0, la.pop((len(la)-1)))
# print(la)

for i in range (m):
    a=lm[i][0]-1
    b=lm[i][1]
    c=lm[i][2]

    print("=====" ,ln[a])
    if b==0:
        for _ in range (c):
            ln[a].append(ln[a].pop(0))
    if b==1:
        for _ in range (c):
            ln[a].insert(0, ln[a].pop(len(ln[a])-1))

for i, val in enumerate(ln):
    print(val)

p = n//2
s=0
e=n
nRslt=0

for i in range(n):
    for j in range(s,e):
        nRslt += ln[i][j]
    if i<p:
        s+=1
        e-=1
    else :
        s-=1
        e+=1
print(nRslt)

#
#
# def lShift(la, n):
#     print(n, la)
#     la = la
#     for _ in range(n):
#         tmp = la[0]
#         for i in range(1, len(la)):
#             la[i - 1] = la[i]
#         la[len(la) - 1] = tmp
#     return la
#
#
# def rShift(la, n):
#     print(n, la)
#     la = la
#     for _ in range(n):
#         tmp = la[len(la) - 1]
#         for i in range(len(la) - 1, -1, -1):
#             la[i] = la[i - 1]
#         la[0] = tmp
#     return la
#
# # ln[lm[0][0]] = lShift(ln, lm[i][2])
#
# for i in range(m):
#     if lm[i][1] == 0:
#         ln.pop(i) = lShift(ln, lm[i][2])
#     elif lm[i][1] == 1:
#         ln[lm[i][0]] = rShift(ln, lm[i][2])
#
# print(ln)