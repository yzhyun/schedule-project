#1 2 3 4 10 9 8 7 13 12 11 5 6 14 15 16 17 18 19 20

import sys
sys.stdin=open("../input.txt", "rt")

n = 10
cards = [ i for i in range(21)]

for _ in range(n):
    s, e = map(int, input().split())
    for i in range((e-s+1) // 2):
        cards[s+i], cards[e-i] = cards[e-i], cards[s+i]

cards.pop(0)
print(cards)