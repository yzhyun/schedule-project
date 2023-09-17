import sys
import itertools as it
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

while 1:
    ln = list(map(int, input().split()))
    if ln[0] == 0:
        break
    ln = ln[1:ln[0] + 1]
    for x in it.combinations(ln, 6):
        for i in x:
            print(i, end = ' ')
        print()
    print()


