import sys
sys.stdin=open("../input.txt", "rt")

n = int(input())



for i in range(1, n+1):
    word = input()
    word = word.upper()
    c = len(word) // 2
    cnt = 0
    for j in range(c):
        if word[j] != word[-1-j]:
            print(f"#{i} NO")
            break
    else:
        print(f"#{i} YES")

        # print(word[j], word[len(word)-(j+1)])
        # print(j, len(word) - (j+1))

