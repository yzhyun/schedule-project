import sys
from itertools import permutations

sys.stdin = open("input.txt", "rt")

cards = list(input())
nums = []
for i in range(len(cards)):
    nums += permutations(list(cards), i+1)
    nums_list = list(map(int, map("".join, nums)))
print(nums_list)

nums2 = []
def getPermutations(cards, n, k):
    if k == n:

    return nums2

for i in range(len(cards)):
    print(getPermutations(cards, i+1))