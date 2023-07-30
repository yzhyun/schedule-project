import sys
sys.stdin = open ("input.txt")

n = int(input())

lt = rt = 1
count = 0
nSum = 1

while lt <= rt :

    if nSum == n:
        print(lt, rt)
        count += 1
        rt += 1
        nSum += rt
    elif nSum > n:
        nSum -= lt
        lt += 1
    else:
        rt += 1
        nSum += rt

print(count)






