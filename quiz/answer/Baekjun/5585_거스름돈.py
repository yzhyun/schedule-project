import sys
sys.stdin = open("input.txt", "rt")

PAY = 1000
price = int(input())
change = PAY - price

# 500엔, 100엔, 50엔, 10엔, 5엔, 1엔
coin_list = [500, 100, 50, 10, 5, 1]

cnt = 0

change1 = change
for coin in coin_list:
    if change >= coin:
        cnt += change // coin
        change = change % coin
        change1 %= coin

print(cnt)
