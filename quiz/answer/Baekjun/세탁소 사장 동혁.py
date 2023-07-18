import sys
sys.stdin = open("../input.txt", "rt")

n = int(input())

for i in range(n):
    res = []
    m = int(input())

    res.append(m // 25)
    m = m % 25

    res.append(m // 10)
    m = m % 10

    res.append(m // 5)
    m = m % 5

    res.append(m // 1)
    m = m % 1

    for j in res:
        print(j, end=' ')
    print()

