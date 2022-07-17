import sys
sys.stdin=open("input.txt", "rt")

n=int(input())
arr=[list(map(int, input().split())) for _ in range(n)]
arr2=[[0] *(n+2) for _ in range(n+2)]

print("=====================================================")
print(n)
for li in arr:
    for i in li:
        print(i, end= ' ')
    print()
print("=====================================================")
for li in arr2:
    for i in li:
        print(i, end= ' ')
    print()
print("=====================================================")

