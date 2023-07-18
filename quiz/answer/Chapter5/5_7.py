import sys
from collections import deque
sys.stdin=open("../input.txt", "rt")

s = input()
n = int(input())

# for i in range(n):
#     schedule = input()
#     dq = deque(schedule)
#     cnt = 0
#     while dq:
#         if s[cnt] == dq.popleft():
#             cnt += 1
#         if cnt == len(s):
#             print(f" #{i+1} YES")
#             break
#     if cnt != len(s) and not dq:
#         print(f" #{i + 1} NO")

for i in range(n):
    plan = input()
    dq = deque(s)
    for x in plan:
        if x in dq:
            if x != dq.popleft():
                print(f"#{i+1} NO")
                break
    else:
        if not dq:
            print(f"#{i+1} YES")
        else:
            print(f"#{i+1} NO")



