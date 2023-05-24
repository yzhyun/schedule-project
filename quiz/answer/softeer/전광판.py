import sys
sys.stdin = open("input.txt", "rt")

dict_q = {"0": [1, 1, 1, 0, 1, 1, 1],
          "1": [0, 0, 1, 0, 0, 1, 0],
          "2": [1, 0, 1, 1, 1, 0, 1],
          "3": [1, 0, 0, 1, 0, 1, 1],
          "4": [1, 0, 1, 1, 0, 1, 0],
          "5": [1, 1, 0, 1, 0, 1, 1],
          "6": [1, 1, 0, 1, 1, 1, 1],
          "7": [1, 1, 1, 0, 0, 1, 0],
          "8": [1, 1, 1, 1, 1, 1, 1],
          "9": [1, 1, 1, 1, 0, 1, 1],
          " ": [0, 0, 0, 0, 0, 0, 0]}

n = int(input())
for i in range(n):
    x, y = map(str, input().split())
    # x = " " * (5 - len(x)) + x
    # y = " " * (5 - len(y)) + y

    x = x.rjust(5, " ")
    y = y.rjust(5, " ")

    print(x, y)
    cnt = 0
    for j in range(5):
        if x[j] == y[j]:
            continue
        else:
            for k in range(7):
                if dict_q[x[j]][k] != dict_q[y[j]][k] :
                    cnt += 1
    print(cnt)
print(dict_q["9"][0])
