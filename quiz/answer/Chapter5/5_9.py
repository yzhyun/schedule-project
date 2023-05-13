import sys
sys.stdin = open("../input.txt", "rt")

# AbaAeCe
# baeeACA
sWord = input()
dWord = dict()
for s in sWord:
    dWord[s] = dWord.get(s,0) + 1

sWord = input()
for s in sWord:
    dWord[s] = dWord.get(s,0) - 1

print(dWord)
for key, val in dWord.items():
    if val > 0 :
        print("NO")
        break
else:
    print("YES")

