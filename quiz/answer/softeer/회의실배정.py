import sys
sys.stdin = open("input.txt", "rt")

n, m = map(int, sys.stdin.readline().split())

# 회의실 일정표 만들기(n)
rooms = {}
for _ in range(n):
    nm = sys.stdin.readline().strip()
    rooms[nm] = [0] * 18 + [1]

rooms = dict(sorted(rooms.items()))
# 일정이 있는 곳에 '1' 표기
for _ in range(m):
    nm, st, et = sys.stdin.readline().split()
    st = int(st)
    et = int(et)
    for i in range(st, et):

        rooms[nm][i] = 1
# 출력
cnt = 0
for i, nm in enumerate(rooms):
    cnt += 1
    print(f"Room {nm}:")
    current = 1
    temp = []
    start=0
    end=0
    for j in range(9,19):
        if current == 1 and rooms[nm][j] == 0:
            start = j
            current = 0
        elif current == 0 and rooms[nm][j] == 1:
            end = j
            current = 1
            temp.append([start,end])
    if not temp:
        print("Not available")
    else:
        print(f"{len(temp)} avaliable")
    for i, val in enumerate(temp):
        a = str(val[0])
        b = str(val[1])
        a=a.zfill(2)
        b=b.zfill(2)
        print(f"{a}-{b}")

    print(len(rooms), i, cnt)
    if cnt == len(rooms):
        continue
    else :
        print("-----")

#0, 0, 1, 0, 0, 0, 0, 1, 1, 1



