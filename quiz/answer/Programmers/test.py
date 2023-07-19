from itertools import permutations
ln = "123"
ln = list(ln)


num = 0
allNums = set()
for i in range(1, len(ln)+1):            # numbers의 각 숫자들을 순열로 모든 경우 만들기
    per = permutations(ln, i)
    for perm in per:
        print(perm)
        num = int(''.join(perm))

print(num)
# for i in range(1, len(numbers) + 1):
#     permutationList = permutations(li, i)
#     for perm in permutationList:
#         num = int(''.join(perm))
#         allNums.add(num)

