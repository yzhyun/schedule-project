import itertools as it
def solution(numbers):
    answer = 0
    ln = list(numbers)
    n = len(ln)
    ch = [0] * n

    for i in range(1, len(ln) + 1):  # numbers의 각 숫자들을 순열로 모든 경우 만들기
        per = it.permutations(ln, i)
        for perm in per:
            print(perm)
            num = int(''.join(perm))



    return answer

solution("17")