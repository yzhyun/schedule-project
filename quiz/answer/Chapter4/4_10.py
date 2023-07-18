import sys
sys.stdin=open("../input.txt", "rt")

n=int(input())
ln=list(map(int, input().split()))

print(ln)
res = [0] * n

for i in range(n):
    cnt = ln[i]
    for j in range(n):
        if res[j] == 0 and cnt == 0:
            res[j] = i+1
            break
        elif res[j] == 0:
            cnt -= 1
print(res)

