import sys
sys.stdin=open("../input.txt", "rt")

sQuiz = input()
sQuiz = sQuiz.lower()
str2 = ""

for idx, val in enumerate(sQuiz):
    if 97 <= ord(val) <= 122:
        continue
    else:
        str2 += val

num = int(str2)
print(num)
cnt = 0
for i in range(1, num+1):
    if num % i == 0:
        cnt += 1

print(cnt)