#1 2 3 4 10 9 8 7 13 12 11 5 6 14 15 16 17 18 19 20

import sys
sys.stdin=open("input.txt", "rt")

lrslt=[i for i in range(0,21)]
#lq=list(map(int, input().split()))
#print(lq)

print(lrslt)
a,b=2,8
ltemp=lrslt[a:b+1]
print(ltemp)
ltemp=lrslt[a:b+1].reverse()
print(ltemp)