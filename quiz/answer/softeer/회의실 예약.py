import sys
sys.stdin = open("input.txt", "rt")

n, m = map(int, input().split())
rooms = {input(): [0] * 18 + [1] for _ in range(n)}
rooms = dict(sorted(rooms.items()))

for _ in range(m):
    nm, st, et = input().split()
    st = int(st)
    et = int(et)

    for i in range(st, et):
        rooms[nm][i] = 1

# print(rooms)
k = 0
for nm in rooms:
    k += 1
    print(f"Room {nm}:")

    empty = []
    curr = 1
    for i in range(9, 19):
        if curr == 1 and rooms[nm][i] == 0:
            start = i
            curr = 0
        elif curr == 0 and rooms[nm][i] == 1:
            end = i
            curr = 1
            empty.append([start, end])

    if empty:
        print(f"{len(empty)} available:")
    else:
        print("Not available")
    for start, end in empty:
        print(f"{str(start).zfill(2)}-{str(end).zfill(2)}")

    if k < len(rooms):
        print("-----")