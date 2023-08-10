<<<<<<< HEAD
import sys
sys.stdin = open("input.txt", "rt")

a = input()
b = input()
n = len(a) + len(b)

tmp = []
for i in range(len(a)):
    tmp.append((a[i]))
    tmp.append((b[i]))

dy = []
dy.append(tmp)
for _ in range(n-2):
    dy.append([''] * (n))

for i in range(1, n-1):
    for j in range(n-i):
        dy[i][j] = str((int(dy[i-1][j]) + int(dy[i-1][j+1])) % 10)


print(''.join(dy[n-2]))




=======
import sys
sys.stdin = open("input.txt", "rt")

a = input()
b = input()
n = len(a) + len(b)

tmp = []
for i in range(len(a)):
    tmp.append((a[i]))
    tmp.append((b[i]))

dy = []
dy.append(tmp)
for _ in range(n-2):
    dy.append([''] * (n))

for i in range(1, n-1):
    for j in range(n-i):
        dy[i][j] = str((int(dy[i-1][j]) + int(dy[i-1][j+1])) % 10)


print(''.join(dy[n-2]))




>>>>>>> 07dc0218ae8bcd18769e131330563c051c357bee
