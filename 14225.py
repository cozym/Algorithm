# 부분수열의 합
import sys
input = sys.stdin.readline

N = int(input())
S = list(map(int,input().split()))
possible = [False for _ in range(sum(S)+2)]

def recursion(idx, s):
    possible[s] = True
    if idx == N:
        return

    recursion(idx+1, s)
    recursion(idx+1, s+S[idx])

recursion(0,0)

for i in range(sum(S)+2):
    if not possible[i]:
        print(i)
        break