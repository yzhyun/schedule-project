import sys
sys.stdin = open("../input.txt", "rt")

def DFS(L, curr_sum):
    if L == n:
        if m > sum:
    else:
        DFS(L + 1, curr_sum + a[L])
        DFS(L + 1, curr_sum)


if __name__ == "__main__":
    m, n = map(int, input().split())
    a = list(map(int, input().split()))
    maxSum=1
    DFS(0, 0)
