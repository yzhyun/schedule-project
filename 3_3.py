import sys
sys.stdin=open("input.txt", "rt")

lcards=[(i+1)*1 for i in range(20)]
print("lcards ")
print(lcards)


def setList(st, ed):
    ltemps=lcards[st:ed]
    ltemps.reverse()

    lcards[st:ed]=ltemps


for i in range(10):
    ln=list(map(int, input().split()))
    setList(ln[0]-1, ln[1])

print(lcards)



