import sys
sys.stdin=open("../input.txt", "rt")

n = int(input())
ln = list(map(int, input().split()))

print(ln)
def reverse(x):
    res = 0
    while x > 0:
        tmp = x % 10
        x = x // 10
        res = res * 10 + tmp
    return res

def isPrime(x):
    if x == 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

for idx, val in enumerate(ln):
    retVal = reverse(val)
    if isPrime(retVal):
        print(retVal, end = ' ')
