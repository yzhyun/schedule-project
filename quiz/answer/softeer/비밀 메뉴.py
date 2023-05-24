import sys
sys.stdin = open("input.txt", "rt")
m,n,k = map(int, input().split())
secret_num = "".join(list(input().split()))
user_num = "".join(list(input().split()))

print(secret_num)

ln = []
for i in range(n-2):
    ln.append(user_num[i:i+len(secret_num)])

if secret_num in ln:
    print("secret")
else :
    print("normal")


print(secret_num)