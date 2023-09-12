ln = [1, 7]

res =""
def perm(str, levl, k):
    global res
    if levl == k:
        res+=str
    else:
        for i in range(len(ln)):
            perm(ln[i], levl + 1, k)

    print(res)
perm("", 0, 2)
