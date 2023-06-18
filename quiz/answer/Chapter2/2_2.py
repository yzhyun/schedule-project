import sys
sys.stdin = open("../input.txt", "rt")

q = int(input())

for i in range(1, 1+q):
    n, s, e, k = map(int, input().split())
    ln = list(map(int, input().split()))
    a = ln[s-1: e]
    a.sort()
    print(f"#{i} {a[k-1]}")
