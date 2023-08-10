import sys
sys.stdin = open("input.txt", "rt")

a = int(input())
n = 10 ** a -1

m = int(n**0.5)

# arr = [False, False]+[True] * (n-1)
# for i in range(2, m+1):
#     for j in range(i*2, n+1, i):
#         arr[j] = False

def isPrime(a):
    for i in range(2, int(a**0.5 + 1)):
        if a % i == 0:
            return False
    return True

def DFS(x):
    if len(str(x)) == a:
        print(x)
    else:
        for i in range(1, 10):
            if i % 2 == 0:
                continue
            else:
                if isPrime(x * 10 + i):
                    DFS(x * 10 + i)

DFS(2)
DFS(3)
DFS(5)
DFS(7)