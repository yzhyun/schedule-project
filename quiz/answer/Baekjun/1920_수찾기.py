import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

n = int(input())
ln = list(map(int, input().split()))
ln.sort()
m = int(input())
lm = list(map(int, input().split()))

def findNum(x):
    s = 0
    e = n-1
    while s <= e:
        mid = (s + e) // 2
        if ln[mid] > x:
            e = mid-1
        elif ln[mid] < x:
            s = mid+1
        else:
            return True
    return False



for i, val in enumerate(lm):
    if findNum(val):
        print(1)
    else:
        print(0)


