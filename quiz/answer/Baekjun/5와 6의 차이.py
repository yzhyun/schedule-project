import sys
sys.stdin = open("../input.txt", "rt")

a, b = map(str, input().split())

#최소값 6 을 5로 볼 때
mina = a.replace('6', '5')
minb = b.replace('6', '5')

#print(mina, minb)
#최대값 5 를 6으로볼 떄
maxa = a.replace('5', '6')
maxb = b.replace('5', '6')
#print(maxa, maxb)

print(f"{int(mina)+int(minb)} {int(maxa)+int(maxb)}")

