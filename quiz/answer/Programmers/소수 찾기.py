def solution(numbers):
    answer = 0
    ln = list(numbers)
    n = len(ln)
    ch = [0] * n

    permutations = set()
    res = [''] * n
    def DFS(L, m):
        if L == m:
            permutations.add(int(''.join(res)))
        else:
            for i in range(0, n):
                if ch[i] == 0:
                    ch[i] = 1
                    res[L] = ln[i]
                    DFS(L+1, m)
                    ch[i] = 0

    for i in range(1, n+1):
        DFS(0, i)
    print(permutations)

    def isPrime(maxVal):
        ch = [0] * (maxVal+1)
        cnt = 0
        for i in range(2, maxVal+1):
            if ch[i] == 0:
                primes.append(i)
                for j in range(i, maxVal+1, i):
                    ch[j]=1



    primes = []
    isPrime(max(permutations))
    res = 0
    for x in permutations:
        if x in primes:
            res+=1
    #print(primes)
    answer = res

    return answer

solution("17")