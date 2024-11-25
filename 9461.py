# 파도반 수열
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    p = [0]*(N+3)

    p[0], p[1], p[2] = 1, 1, 1

    for i in range(2, N+1):
        p[i] = p[i-2] + p[i-3]

    print(p[N-1])